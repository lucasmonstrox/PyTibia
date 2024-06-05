from numba import njit
import numpy as np
from scipy.spatial import distance
from typing import Union
from src.shared.typings import Coordinate, GrayImage, GrayPixel, WaypointList
from src.utils.core import hashit, locate
from src.utils.coordinate import getCoordinateFromPixel, getPixelFromCoordinate
from .config import availableTilesFrictions, breakpointTileMovementSpeed, coordinates, dimensions, floorsImgs, floorsLevelsImgsHashes, floorsPathsSqms, nonWalkablePixelsColors, tilesFrictionsWithBreakpoints, walkableFloorsSqms
from .extractors import getRadarImage
from .locators import getRadarToolsPosition
from .typings import FloorLevel, TileFriction


# TODO: add unit tests
# TODO: add perf
# TODO: get by cached images coordinates hashes
def getCoordinate(screenshot: GrayImage, previousCoordinate: Coordinate = None) -> Coordinate | None:
    radarToolsPosition = getRadarToolsPosition(screenshot)
    if radarToolsPosition is None:
        return None
    radarImage = getRadarImage(screenshot, radarToolsPosition)
    radarHashedImg = hashit(radarImage)
    hashedCoordinate = coordinates.get(radarHashedImg, None)
    if hashedCoordinate is not None:
        return hashedCoordinate
    floorLevel = getFloorLevel(screenshot)
    if floorLevel is None:
        return None
    radarImage[52, 53] = 128
    radarImage[52, 54] = 128
    radarImage[53, 53] = 128
    radarImage[53, 54] = 128
    radarImage[54, 51] = 128
    radarImage[54, 52] = 128
    radarImage[55, 51] = 128
    radarImage[55, 52] = 128
    radarImage[54, 53] = 128
    radarImage[54, 54] = 128
    radarImage[55, 53] = 128
    radarImage[55, 54] = 128
    radarImage[54, 55] = 128
    radarImage[54, 56] = 128
    radarImage[55, 55] = 128
    radarImage[55, 56] = 128
    radarImage[56, 53] = 128
    radarImage[56, 54] = 128
    radarImage[57, 53] = 128
    radarImage[57, 54] = 128
    if previousCoordinate is not None:
        (previousCoordinateXPixel, previousCoordinateYPixel) = getPixelFromCoordinate(
            previousCoordinate)
        paddingSize = 5
        yStart = previousCoordinateYPixel - \
            (dimensions['halfHeight'] + paddingSize)
        yEnd = previousCoordinateYPixel + \
            (dimensions['halfHeight'] + 1 + paddingSize)
        xStart = previousCoordinateXPixel - \
            (dimensions['halfWidth'] + paddingSize)
        xEnd = previousCoordinateXPixel + \
            (dimensions['halfWidth'] + paddingSize)
        areaImgToCompare = floorsImgs[floorLevel][yStart:yEnd, xStart:xEnd]
        areaFoundImg = locate(areaImgToCompare, radarImage, confidence=0.9)
        if areaFoundImg:
            currentCoordinateXPixel = previousCoordinateXPixel - \
                paddingSize + areaFoundImg[0]
            currentCoordinateYPixel = previousCoordinateYPixel - \
                paddingSize + areaFoundImg[1]
            (currentCoordinateX, currentCoordinateY) = getCoordinateFromPixel(
                (currentCoordinateXPixel, currentCoordinateYPixel))
            return (currentCoordinateX, currentCoordinateY, floorLevel)
    imgCoordinate = locate(floorsImgs[floorLevel], radarImage, confidence=0.75)
    if imgCoordinate is None:
        return None
    xImgCoordinate = imgCoordinate[0] + dimensions['halfWidth']
    yImgCoordinate = imgCoordinate[1] + dimensions['halfHeight']
    xCoordinate, yCoordinate = getCoordinateFromPixel(
        (xImgCoordinate, yImgCoordinate))
    return (xCoordinate, yCoordinate, floorLevel)


# TODO: add unit tests
# TODO: add perf
def getFloorLevel(screenshot: GrayImage) -> FloorLevel | None:
    radarToolsPosition = getRadarToolsPosition(screenshot)
    if radarToolsPosition is None:
        return None
    left, top, width, height = radarToolsPosition
    left = left + width + 8
    top = top - 7
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = hashit(floorLevelImg)
    if floorImgHash not in floorsLevelsImgsHashes:
        return None
    return floorsLevelsImgsHashes[floorImgHash]


# TODO: add unit tests
# TODO: add perf
def getClosestWaypointIndexFromCoordinate(coordinate: Coordinate, waypoints: WaypointList) -> Union[int, None]:
    closestWaypointIndex = None
    closestWaypointDistance = 9999
    for waypointIndex, waypoint in enumerate(waypoints):
        if waypoint['coordinate'][2] != coordinate[2]:
            continue
        waypointDistance = distance.cdist(
            [(waypoint['coordinate'][0], waypoint['coordinate'][1])], [(coordinate[0], coordinate[1])]).flatten()[0]
        if waypointDistance < closestWaypointDistance:
            closestWaypointIndex = waypointIndex
            closestWaypointDistance = waypointDistance
    return closestWaypointIndex


# TODO: add perf
def getBreakpointTileMovementSpeed(charSpeed: int, tileFriction: TileFriction) -> int:
    tileFrictionNotFound = tileFriction not in tilesFrictionsWithBreakpoints
    if tileFrictionNotFound:
        closestTilesFrictions = np.flatnonzero(
            availableTilesFrictions > tileFriction)
        tileFriction = availableTilesFrictions[closestTilesFrictions[0]] if len(
            closestTilesFrictions) > 0 else 250
    availableBreakpointsIndexes = np.flatnonzero(
        charSpeed >= tilesFrictionsWithBreakpoints[tileFriction])
    if len(availableBreakpointsIndexes) == 0:
        return breakpointTileMovementSpeed[1]
    return breakpointTileMovementSpeed.get(availableBreakpointsIndexes[-1] + 1)


# TODO: add unit tests
# TODO: add perf
def getTileFrictionByCoordinate(coordinate: Coordinate) -> TileFriction:
    xOfPixelCoordinate, yOfPixelCoordinate = getPixelFromCoordinate(
        coordinate)
    floorLevel = coordinate[2]
    tileFriction = floorsPathsSqms[floorLevel,
                                   yOfPixelCoordinate, xOfPixelCoordinate]
    return tileFriction


# TODO: add unit tests
# TODO: add perf
def isCloseToCoordinate(currentCoordinate: Coordinate, possibleCloseCoordinate: Coordinate, distanceTolerance: int = 10) -> bool:
    (xOfCurrentCoordinate, yOfCurrentCoordinate, _) = currentCoordinate
    XYOfCurrentCoordinate = (xOfCurrentCoordinate, yOfCurrentCoordinate)
    (xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate, _) = possibleCloseCoordinate
    XYOfPossibleCloseCoordinate = (
        xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate)
    euclideanDistance = distance.cdist(
        [XYOfCurrentCoordinate], [XYOfPossibleCloseCoordinate])
    return euclideanDistance <= distanceTolerance


# TODO: add unit tests
# TODO: add perf
# TODO: 2 coordinates was tested. Is very hard too test all coordinates(16 floors * 2560 mapWidth * 2048 mapHeight = 83.886.080 pixels)
def isCoordinateWalkable(coordinate: Coordinate) -> bool:
    (xOfPixel, yOfPixel) = getPixelFromCoordinate(coordinate)
    return (walkableFloorsSqms[coordinate[2], yOfPixel, xOfPixel]) == 1


# TODO: add unit tests
# TODO: add perf
def isNonWalkablePixelColor(pixelColor: GrayPixel) -> bool:
    return np.isin(pixelColor, nonWalkablePixelsColors)
