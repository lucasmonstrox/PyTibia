import tcod
from src.repositories.radar.config import walkableFloorsSqms
from src.shared.typings import Coordinate, CoordinateList
from src.utils.coordinate import getAvailableAroundCoordinates, getClosestCoordinate
from src.utils.core import getPixelFromCoordinate
from .typings import Checkpoint


# TODO: add unit tests
def generateFloorWalkpoints(coordinate: Coordinate, goalCoordinate: Coordinate, nonWalkableCoordinates=[]) -> CoordinateList:
    pixelCoordinate = getPixelFromCoordinate(coordinate)
    xFromTheStartOfRadar = pixelCoordinate[0] - 53
    xFromTheEndOfRadar = pixelCoordinate[0] + 53
    yFromTheStartOfRadar = pixelCoordinate[1] - 54
    yFromTheEndOfRadar = pixelCoordinate[1] + 55
    copiedWalkableFloorSqms = walkableFloorsSqms[coordinate[2]][
        yFromTheStartOfRadar:yFromTheEndOfRadar, xFromTheStartOfRadar:xFromTheEndOfRadar].copy()
    for nonWalkableCoordinate in nonWalkableCoordinates:
        if nonWalkableCoordinate[2] == coordinate[2]:
            nonWalkableCoordinateInPixelX, nonWalkableCoordinateInPixelY = getPixelFromCoordinate(nonWalkableCoordinate)
            leX = nonWalkableCoordinateInPixelX - xFromTheStartOfRadar
            leY = nonWalkableCoordinateInPixelY - yFromTheStartOfRadar
            if leX >= 0 and leX <= 106 and leY >= 0 and leY <= 109:
                copiedWalkableFloorSqms[leY, leX] = 0
    x = goalCoordinate[0] - coordinate[0] + 53
    y = goalCoordinate[1] - coordinate[1] + 54
    return [[coordinate[0] + x - 53,
                   coordinate[1] + y - 54, coordinate[2]] for y, x in tcod.path.AStar(copiedWalkableFloorSqms, 0).get_path(54, 53, y, x)]


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
    elif waypoint['type'] == 'moveDown':
        goalCoordinate = resolveMoveDownEastCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDown':
        goalCoordinate = resolveMoveDownNorthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDown':
        goalCoordinate = resolveMoveDownSouthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDown':
        goalCoordinate = resolveMoveDownWestCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUp':
        goalCoordinate = resolveMoveUpNorthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUp':
        goalCoordinate = resolveMoveUpWestCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDown':
        goalCoordinate = resolveMoveUpEastCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUp':
        goalCoordinate = resolveMoveUpSouthCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useHole':
        goalCoordinate = resolveUseHoleCoordinate(
            coordinate, waypoint['coordinate'])
    else:
        goalCoordinate = resolveFloorCoordinate(
            coordinate, waypoint['coordinate'])
    return goalCoordinate
