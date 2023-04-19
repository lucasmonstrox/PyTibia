import tcod
from src.repositories.radar.config import walkableFloorsSqms
from src.shared.typings import Coordinate, CoordinateList
from src.utils.coordinate import getAvailableAroundCoordinates, getClosestCoordinate
from src.utils.core import getPixelFromCoordinate
from .typings import Checkpoint


# TODO: add unit tests
def generateFloorWalkpoints(coordinate: Coordinate, goalCoordinate: Coordinate, nonWalkableCoordinates=None) -> CoordinateList:
    pixelCoordinate = getPixelFromCoordinate(coordinate)
    xFromTheStartOfRadar = pixelCoordinate[0] - 53
    xFromTheEndOfRadar = pixelCoordinate[0] + 53
    yFromTheStartOfRadar = pixelCoordinate[1] - 54
    yFromTheEndOfRadar = pixelCoordinate[1] + 55
    xOfCoordinate = coordinate[0]
    yOfCoordinate = coordinate[1]
    level = coordinate[2]
    walkableFloorSqms = walkableFloorsSqms[level]
    hasNonWalkableCoordinates = nonWalkableCoordinates is not None
    if hasNonWalkableCoordinates:
        floorLevel = coordinate[2]
        nonWalkableCoordinatesIndexes = nonWalkableCoordinates['z'] == floorLevel
        nonWalkableCoordinatesByCurrentFloorLevel = nonWalkableCoordinates[nonWalkableCoordinatesIndexes]
        for coordinate in nonWalkableCoordinatesByCurrentFloorLevel:
            nonWalkableCoordinateInPixel = getPixelFromCoordinate(coordinate)
            x = nonWalkableCoordinateInPixel[1]
            y = nonWalkableCoordinateInPixel[0]
            # TODO: avoid this, should be copied first
            walkableFloorSqms[x, y] = 0
    pf = tcod.path.AStar(walkableFloorSqms[
        yFromTheStartOfRadar:yFromTheEndOfRadar, xFromTheStartOfRadar:xFromTheEndOfRadar], 0)
    x = goalCoordinate[0] - xOfCoordinate + 53
    y = goalCoordinate[1] - yOfCoordinate + 54
    paths = pf.get_path(54, 53, y, x)
    walkpoints = [[xOfCoordinate + x - 53,
                   yOfCoordinate + y - 54, level] for y, x in paths]
    return walkpoints


# TODO: add unit tests
def resolveFloorCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    return {
        'goalCoordinate': nextCoordinate,
        'checkInCoordinate': nextCoordinate,
    }


# TODO: add unit tests
def resolveMoveDownEastCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x + 2, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveMoveDownNorthCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x, y - 2, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveMoveDownSouthCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x, y + 2, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveMoveDownWestCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x - 2, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveMoveUpNorthCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y - 2, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


# TODO: add unit tests
def resolveMoveUpWestCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x - 2, y, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


# TODO: add unit tests
def resolveMoveUpEastCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x + 2, y, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


# TODO: add unit tests
def resolveMoveUpSouthCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y + 2, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


# TODO: add unit tests
def resolveUseShovelWaypointCoordinate(coordinate, nextCoordinate: Coordinate) -> Checkpoint:
    floorLevel = nextCoordinate[2]
    # TODO: avoid copying whole level
    walkableFloorSqms = walkableFloorsSqms[floorLevel].copy()
    availableAroundCoordinates = getAvailableAroundCoordinates(
        nextCoordinate, walkableFloorSqms)
    closestCoordinate = getClosestCoordinate(
        coordinate, availableAroundCoordinates)
    checkInCoordinate = [nextCoordinate[0],
                         nextCoordinate[1], nextCoordinate[2] + 1]
    return {
        'goalCoordinate': closestCoordinate,
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveUseRopeWaypointCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    checkInCoordinate = [nextCoordinate[0],
                         nextCoordinate[1] + 1, nextCoordinate[2] - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


# TODO: add unit tests
def resolveUseHoleCoordinate(_, nextCoordinate: Coordinate) -> Checkpoint:
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


# TODO: add unit tests
def resolveGoalCoordinate(coordinate: Coordinate, waypoint):
    goalCoordinate = None
    if waypoint['type'] == 'useRope':
        goalCoordinate = resolveUseRopeWaypointCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useShovel':
        goalCoordinate = resolveUseShovelWaypointCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownEast':
        goalCoordinate = resolveMoveDownEastCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownNorth':
        goalCoordinate = resolveMoveDownNorthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownSouth':
        goalCoordinate = resolveMoveDownSouthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownWest':
        goalCoordinate = resolveMoveDownWestCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpNorth':
        goalCoordinate = resolveMoveUpNorthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpWest':
        goalCoordinate = resolveMoveUpWestCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownEast':
        goalCoordinate = resolveMoveUpEastCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpSouth':
        goalCoordinate = resolveMoveUpSouthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useHole':
        goalCoordinate = resolveUseHoleCoordinate(
            coordinate, waypoint['coordinate'])
    else:
        goalCoordinate = resolveFloorCoordinate(
            coordinate, waypoint['coordinate'])
    return goalCoordinate
