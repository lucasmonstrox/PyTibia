import numpy as np
import pyautogui
from scipy.spatial import distance
from time import sleep
from . import config, extractors, locators
import utils.core
import utils.image
import utils.mouse


# TODO: add unit tests
# TODO: get by cached images coordinates hashes
def getCoordinate(screenshot, previousCoordinate=None):
    floorLevel = getFloorLevel(screenshot)
    cannotGetFloorLevel = floorLevel is None
    if cannotGetFloorLevel:
        return None
    radarToolsPos = locators.getRadarToolsPos(screenshot)
    cannotGetRadarToolsPos = radarToolsPos is None
    if cannotGetRadarToolsPos:
        return None
    radarImg = extractors.getRadarImg(screenshot, radarToolsPos)
    radarHashedImg = utils.core.hashitHex(radarImg)
    shouldGetCoordinateByCachedRadarHashedImg = radarHashedImg in config.coordinates
    if shouldGetCoordinateByCachedRadarHashedImg:
        return config.coordinates[radarHashedImg]
    shouldGetCoordinateByPreviousCoordinateArea = previousCoordinate is not None
    if shouldGetCoordinateByPreviousCoordinateArea:
        (previousCoordinateXPixel, previousCoordinateYPixel) = utils.core.getPixelFromCoordinate(
            previousCoordinate)
        paddingSize = 20
        yStart = previousCoordinateYPixel - \
            (config.dimensions["halfHeight"] + paddingSize)
        yEnd = previousCoordinateYPixel + \
            (config.dimensions["halfHeight"] + 1 + paddingSize)
        xStart = previousCoordinateXPixel - \
            (config.dimensions["halfWidth"] + paddingSize)
        xEnd = previousCoordinateXPixel + \
            (config.dimensions["halfWidth"] + paddingSize)
        areaImgToCompare = config.floorsImgs[floorLevel][yStart:yEnd, xStart:xEnd]
        areaFoundImg = utils.core.locate(
            areaImgToCompare, radarImg, confidence=0.9)
        if areaFoundImg:
            currentCoordinateXPixel = previousCoordinateXPixel - \
                paddingSize + areaFoundImg[0]
            currentCoordinateYPixel = previousCoordinateYPixel - \
                paddingSize + areaFoundImg[1]
            (currentCoordinateX, currentCoordinateY) = utils.core.getCoordinateFromPixel(
                (currentCoordinateXPixel, currentCoordinateYPixel))
            return [currentCoordinateX, currentCoordinateY, floorLevel]
    imgCoordinate = utils.core.locate(
        config.floorsImgs[floorLevel], radarImg, confidence=0.75)
    cannotGetImgCoordinate = imgCoordinate is None
    if cannotGetImgCoordinate:
        return None
    xImgCoordinate = imgCoordinate[0] + config.dimensions["halfWidth"]
    yImgCoordinate = imgCoordinate[1] + config.dimensions["halfHeight"]
    xCoordinate, yCoordinate = utils.core.getCoordinateFromPixel(
        (xImgCoordinate, yImgCoordinate))
    return [xCoordinate, yCoordinate, floorLevel]


# TODO: add unit tests
def getFloorLevel(screenshot):
    radarToolsPos = locators.getRadarToolsPos(screenshot)
    radarToolsPosIsEmpty = radarToolsPos is None
    if radarToolsPosIsEmpty:
        return None
    left, top, width, height = radarToolsPos
    left = left + width + 8
    top = top - 7
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = utils.core.hashit(floorLevelImg)
    hashNotExists = not floorImgHash in config.floorsLevelsImgsHashes
    if hashNotExists:
        return None
    floorLevel = config.floorsLevelsImgsHashes[floorImgHash]
    return floorLevel


def getClosestWaypointIndexFromCoordinate(coordinate, waypoints):
    (xOfCoordinate, yOfCoordinate, floorLevel) = coordinate
    currentCoordinateWithoutFloor = [xOfCoordinate, yOfCoordinate]
    waypointsCoordinatesWithoutFloor = waypoints['coordinate'][:, :-1]
    waypointsCoordinatesDistances = distance.cdist(
        waypointsCoordinatesWithoutFloor, [currentCoordinateWithoutFloor]).flatten()
    waypointsIndexesOfCurrentFloor = np.nonzero(
        waypoints['coordinate'][:, 2] == floorLevel)[0]
    waypointsCoordinatesDistancesOfCurrentFloor = waypointsCoordinatesDistances[
        waypointsIndexesOfCurrentFloor]
    lowestWaypointIndex = np.argmin(
        waypointsCoordinatesDistancesOfCurrentFloor)
    lowestWaypointIndexOfCurrentFloor = waypointsIndexesOfCurrentFloor[lowestWaypointIndex]
    return lowestWaypointIndexOfCurrentFloor


# TODO: add unit tests
def getBreakpointTileMovementSpeed(charSpeed, tileFriction):
    breakpointTileMovementSpeed = {
        1: 850,
        2: 800,
        3: 750,
        4: 700,
        5: 650,
        6: 600,
        7: 550,
        8: 500,
        9: 450,
        10: 400,
        11: 350,
        12: 300,
        13: 250,
        14: 200,
        15: 150,
        16: 100,
        17: 50,
    }
    tilesFrictionsBreakpoints = {
        70:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 142, 200, 342, 1070]),
        90:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 147, 192, 278, 499, 1842]),
        95:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 157, 205, 299, 543, 2096]),
        100: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 113, 135, 167, 219, 321, 592, 2382]),
        110: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 150, 187, 248, 367, 696, 3060]),
        120: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
        125: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
        130: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
        135: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
        136: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
        140: np.array([0, 0, 0, 0, 0, 0, 0, 111, 125, 143, 167, 201, 254, 344, 531, 1092, 6341]),
        150: np.array([0, 0, 0, 0, 0, 0, 0, 120, 135, 155, 181, 219, 278, 380, 595, 1258, 8036]),
        160: np.array([0, 0, 0, 0, 0, 0, 116, 129, 145, 167, 196, 238, 304, 419, 663, 1443, 10167]),
        170: np.array([0, 0, 0, 0, 0, 0, 116, 129, 145, 167, 196, 238, 304, 419, 663, 1443, 10167]),
        200: np.array([0, 0, 0, 114, 124, 135, 149, 167, 190, 219, 261, 322, 419, 597, 998, 2444, 25761]),
        250: np.array([117, 126, 135, 146, 160, 175, 195, 220, 252, 295, 356, 446, 598, 884, 1591, 4557, 81351]),
        255: np.array([117, 126, 135, 146, 160, 175, 195, 220, 252, 295, 356, 446, 598, 884, 1591, 4557, 81351]),
    }
    # TODO: sometimes friction is not found
    if tileFriction in tilesFrictionsBreakpoints:
        breakpoints = tilesFrictionsBreakpoints[tileFriction]
    else:
        breakpoints = tilesFrictionsBreakpoints[140]
    currentSpeedBreakpoint = np.nonzero(breakpoints >= charSpeed)[0][0]
    speed = breakpointTileMovementSpeed[currentSpeedBreakpoint]
    return speed


# TODO: add unit tests
def getTileFrictionByCoordinate(coordinate):
    xOfPixelCoordinate, yOfPixelCoordinate = utils.core.getPixelFromCoordinate(
        coordinate)
    floorLevel = coordinate[2]
    tileFriction = config.floorsPathsSqms[floorLevel,
                                          yOfPixelCoordinate, xOfPixelCoordinate]
    return tileFriction


# TODO: add unit tests
def goToCoordinate(screenshot, currentCoordinate, nextCoordinate):
    (radarToolsPosX, radarToolsPosY, _, _) = locators.getRadarToolsPos(screenshot)
    x0 = radarToolsPosX - config.dimensions['width'] - 11
    y0 = radarToolsPosY - 50
    radarCenterX = x0 + config.dimensions['halfWidth']
    radarCenterY = y0 + config.dimensions['halfHeight']
    xdiff = nextCoordinate[0] - currentCoordinate[0]
    ydiff = nextCoordinate[1] - currentCoordinate[1]
    x = xdiff + radarCenterX
    y = ydiff + radarCenterY
    pyautogui.click(x, y)
    sleep(0.25)


def isCloseToCoordinate(currentCoordinate, possibleCloseCoordinate, distanceTolerance=10):
    (xOfCurrentCoordinate, yOfCurrentCoordinate, _) = currentCoordinate
    XYOfCurrentCoordinate = (xOfCurrentCoordinate, yOfCurrentCoordinate)
    (xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate, _) = possibleCloseCoordinate
    XYOfPossibleCloseCoordinate = (
        xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate)
    euclideanDistance = distance.cdist(
        [XYOfCurrentCoordinate], [XYOfPossibleCloseCoordinate])
    isClose = euclideanDistance <= distanceTolerance
    return isClose


# TODO: 2 coordinates was tested. Is very hard too test all coordinates(16 floors * 2560 mapWidth * 2048 mapHeight = 83.886.080 pixels)
def isCoordinateWalkable(coordinate):
    (_, _, floorLevel) = coordinate
    (xOfPixel, yOfPixel) = utils.core.getPixelFromCoordinate(coordinate)
    pixelValue = config.walkableFloorsSqms[floorLevel, yOfPixel, xOfPixel]
    isWalkable = pixelValue == 1
    return isWalkable


def isNonWalkablePixelColor(pixelColor):
    isNonWalkable = np.isin(pixelColor, config.nonWalkablePixelsColors)
    return isNonWalkable
