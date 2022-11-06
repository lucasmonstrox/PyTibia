import numpy as np
from scipy.spatial import distance
from . import core


def getAroundPixelsCoordinates(pixelCoordinate):
    aroundPixelsCoordinatesIndexes = np.array(
        [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]])
    pixelCoordinates = np.broadcast_to(
        pixelCoordinate, aroundPixelsCoordinatesIndexes.shape)
    aroundPixelsCoordinates = np.add(
        aroundPixelsCoordinatesIndexes, pixelCoordinates)
    return aroundPixelsCoordinates


def getAvailableAroundPixelsCoordinates(aroundPixelsCoordinates, walkableFloorSqms):
    yPixelsCoordinates = aroundPixelsCoordinates[:, 1]
    xPixelsCoordinates = aroundPixelsCoordinates[:, 0]
    walkableFloorSqmsByPixelsCoordinates = walkableFloorSqms[yPixelsCoordinates,
                                                             xPixelsCoordinates]
    nonzero = np.nonzero(walkableFloorSqmsByPixelsCoordinates)[0]
    availableAroundPixelsCoordinates = np.take(
        aroundPixelsCoordinates, nonzero, axis=0)
    return availableAroundPixelsCoordinates


def getAvailableAroundCoordinates(coordinate, walkableFloorSqms):
    floor = coordinate[2]
    pixelCoordinate = core.getPixelFromCoordinate(coordinate)
    aroundPixelsCoordinates = getAroundPixelsCoordinates(pixelCoordinate)
    availableAroundPixelsCoordinates = getAvailableAroundPixelsCoordinates(
        aroundPixelsCoordinates, walkableFloorSqms)
    xCoordinates = availableAroundPixelsCoordinates[:, 0] + 31744
    yCoordinates = availableAroundPixelsCoordinates[:, 1] + 30976
    floors = np.broadcast_to(
        floor, (availableAroundPixelsCoordinates.shape[0]))
    availableAroundCoordinates = np.column_stack(
        (xCoordinates, yCoordinates, floors))
    return availableAroundCoordinates


def getClosestCoordinate(coordinate, coordinates):
    xOfCoordinate, yOfCoordinate, _ = coordinate
    coordinateWithoutFloor = [xOfCoordinate, yOfCoordinate]
    coordinatesWithoutFloor = coordinates[:, [0, 1]]
    distancesOfCoordinates = distance.cdist(
        [coordinateWithoutFloor], coordinatesWithoutFloor)[0]
    sortedDistancesOfCoordinates = np.argsort(distancesOfCoordinates)
    closestCoordinateIndex = sortedDistancesOfCoordinates[0]
    closestCoordinate = coordinates[closestCoordinateIndex]
    return closestCoordinate


def getDirectionBetweenCoordinates(coordinate, nextCoordinate):
    (xOfCurrentCoordinate, yOfCurrentCoordinate, _) = coordinate
    (xOfNextWaypointCoordinate, yOfNextWaypointCoordinate, _) = nextCoordinate
    if xOfCurrentCoordinate < xOfNextWaypointCoordinate:
        return 'right'
    if xOfNextWaypointCoordinate < xOfCurrentCoordinate:
        return 'left'
    if yOfCurrentCoordinate < yOfNextWaypointCoordinate:
        return 'down'
    if yOfNextWaypointCoordinate < yOfCurrentCoordinate:
        return 'up'
    return None
