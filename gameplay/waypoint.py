import numpy as np
import tcod
import radar.config
import radar.core
import radar.extractors
import utils.array
import utils.coordinate
import utils.core
import utils.image
import utils.matrix
import utils.mouse


def generateFloorWalkpoints(coordinate, goalCoordinate, nonWalkableCoordinates=None):
    pixelCoordinate = utils.core.getPixelFromCoordinate(coordinate)
    xFromTheStartOfRadar = pixelCoordinate[0] - 53
    xFromTheEndOfRadar = pixelCoordinate[0] + 53
    yFromTheStartOfRadar = pixelCoordinate[1] - 54
    yFromTheEndOfRadar = pixelCoordinate[1] + 55
    xOfCoordinate, yOfCoordinate, level = coordinate
    walkableFloorSqms = radar.config.walkableFloorsSqms[level].copy()
    hasNonWalkableCoordinates = nonWalkableCoordinates is not None
    if hasNonWalkableCoordinates:
        floorLevel = coordinate[2]
        nonWalkableCoordinatesIndexes = nonWalkableCoordinates['z'] == floorLevel
        nonWalkableCoordinatesByCurrentFloorLevel = nonWalkableCoordinates[nonWalkableCoordinatesIndexes]
        for coordinate in nonWalkableCoordinatesByCurrentFloorLevel:
            nonWalkableCoordinateInPixel = utils.core.getPixelFromCoordinate(coordinate)
            x = nonWalkableCoordinateInPixel[1]
            y = nonWalkableCoordinateInPixel[0]
            walkableFloorSqms[x, y] = 0
    walkableFloorSqms = walkableFloorSqms[
        yFromTheStartOfRadar:yFromTheEndOfRadar, xFromTheStartOfRadar:xFromTheEndOfRadar]
    pf = tcod.path.AStar(walkableFloorSqms, 0)
    xOfGoalCoordinate, yOfGoalCoordinate, _ = goalCoordinate
    x = xOfGoalCoordinate - xOfCoordinate + 53
    y = yOfGoalCoordinate - yOfCoordinate + 54
    paths = pf.get_path(54, 53, y, x)
    walkpoints = [[xOfCoordinate + x - 53,
                   yOfCoordinate + y - 54, level] for y, x in paths]
    return walkpoints


def resolveFloorCoordinate(_, nextCoordinate):
    return {
        'goalCoordinate': nextCoordinate,
        'checkInCoordinate': nextCoordinate,
    }


def resolveMoveDownWestCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x + 2, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


def resolveMoveDownNorthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x, y - 2, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


def resolveMoveDownSouthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x, y + 2, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


def resolveMoveDownWestCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    checkInCoordinate = [x - 2, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


def resolveMoveUpNorthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y - 2, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


def resolveMoveUpSouthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y + 2, floorLevel - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


def resolveUseShovelWaypointCoordinate(coordinate, nextCoordinate):
    floorLevel = nextCoordinate[2]
    walkableFloorSqms = radar.config.walkableFloorsSqms[floorLevel].copy()
    availableAroundCoordinates = utils.coordinate.getAvailableAroundCoordinates(
        nextCoordinate, walkableFloorSqms)
    closestCoordinate = utils.coordinate.getClosestCoordinate(
        coordinate, availableAroundCoordinates)
    checkInCoordinate = [nextCoordinate[0],
                         nextCoordinate[1], nextCoordinate[2] + 1]
    return {
        'goalCoordinate': closestCoordinate,
        'checkInCoordinate': checkInCoordinate,
    }


def resolveUseRopeWaypointCoordinate(_, nextCoordinate):
    checkInCoordinate = [nextCoordinate[0],
                         nextCoordinate[1] + 1, nextCoordinate[2] - 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': checkInCoordinate,
    }


def resolveUseHoleCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y, floorLevel + 1]
    return {
        'goalCoordinate': [nextCoordinate[0], nextCoordinate[1], nextCoordinate[2]],
        'checkInCoordinate': goalCoordinate,
    }


def resolveGoalCoordinate(coordinate, waypoint):
    goalCoordinate = None
    if waypoint['type'] == 'useRope':
        goalCoordinate = resolveUseRopeWaypointCoordinate(
            coordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useShovel':
        goalCoordinate = resolveUseShovelWaypointCoordinate(
            coordinate, waypoint['coordinate'])
    # elif waypoint['type'] == 'moveDownEast':
    #     goalCoordinate = resolveMoveDownEastCoordinate(
    #         coordinate, waypoint['coordinate'])
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
