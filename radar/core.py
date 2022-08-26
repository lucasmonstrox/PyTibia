import numpy as np
import pyautogui
from scipy.spatial import distance
from time import sleep
from radar import config, extractors, locators
import utils.core
import utils.image
import utils.mouse


# TODO: add unit tests
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
            return (currentCoordinateX, currentCoordinateY, floorLevel)
    # config.floorsConfidence[floorLevel]
    imgCoordinate = utils.core.locate(
        config.floorsImgs[floorLevel], radarImg, confidence=0.75)
    cannotGetImgCoordinate = imgCoordinate is None
    if cannotGetImgCoordinate:
        return None
    xImgCoordinate = imgCoordinate[0] + config.dimensions["halfWidth"]
    yImgCoordinate = imgCoordinate[1] + config.dimensions["halfHeight"]
    xCoordinate, yCoordinate = utils.core.getCoordinateFromPixel(
        (xImgCoordinate, yImgCoordinate))
    return (xCoordinate, yCoordinate, floorLevel)


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
def goToCoordinate(screenshot, currentRadarCoordinate, nextRadarCoordinate):
    (radarToolsPosX, radarToolsPosY, _, _) = locators.getRadarToolsPos(screenshot)
    x0 = radarToolsPosX - config.dimensions['width'] - 11
    y0 = radarToolsPosY - 50
    radarCenterX = x0 + config.dimensions['halfWidth']
    radarCenterY = y0 + config.dimensions['halfHeight']
    xdiff = nextRadarCoordinate[0] - currentRadarCoordinate[0]
    ydiff = nextRadarCoordinate[1] - currentRadarCoordinate[1]
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
