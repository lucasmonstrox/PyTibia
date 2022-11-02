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


def generateFloorWalkpoints(coordinate, goalCoordinate):
    pixelCoordinate = utils.core.getPixelFromCoordinate(coordinate)
    xFromTheStartOfRadar = pixelCoordinate[0] - 53
    xFromTheEndOfRadar = pixelCoordinate[0] + 53
    yFromTheStartOfRadar = pixelCoordinate[1] - 54
    yFromTheEndOfRadar = pixelCoordinate[1] + 55
    xOfRadarCoordinate, yOfRadarCoordinate, level = coordinate
    walkableFloorsSqms = radar.config.walkableFloorsSqms[level].copy()
    walkableFloorsSqms = walkableFloorsSqms[
        yFromTheStartOfRadar:yFromTheEndOfRadar, xFromTheStartOfRadar:xFromTheEndOfRadar]
    # TODO: colocar os players, monstros e buracos/escadas
    pf = tcod.path.AStar(walkableFloorsSqms, 0)
    xOfGoalCoordinate, yOfGoalCoordinate, _ = goalCoordinate
    x = xOfGoalCoordinate - xOfRadarCoordinate + 53
    y = yOfGoalCoordinate - yOfRadarCoordinate + 54
    paths = pf.get_path(54, 53, y, x)
    walkpoints = [[xOfRadarCoordinate + x - 53,
                   yOfRadarCoordinate + y - 54, level] for y, x in paths]
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


def resolveUseShovelWaypointCoordinate(radarCoordinate, nextCoordinate):
    floorLevel = nextCoordinate[2]
    walkableFloorSqms = radar.config.walkableFloorsSqms[floorLevel].copy()
    availableAroundCoordinates = utils.coordinate.getAvailableAroundCoordinates(
        nextCoordinate, walkableFloorSqms)
    closestCoordinate = utils.coordinate.getClosestCoordinate(
        radarCoordinate, availableAroundCoordinates)
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


def resolveGoalCoordinate(radarCoordinate, waypoint):
    goalCoordinate = None
    if waypoint['type'] == 'useRope':
        goalCoordinate = resolveUseRopeWaypointCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useShovel':
        goalCoordinate = resolveUseShovelWaypointCoordinate(
            radarCoordinate, waypoint['coordinate'])
    # elif waypoint['type'] == 'moveDownEast':
    #     goalCoordinate = resolveMoveDownEastCoordinate(
    #         radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownNorth':
        goalCoordinate = resolveMoveDownNorthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownSouth':
        goalCoordinate = resolveMoveDownSouthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownWest':
        goalCoordinate = resolveMoveDownWestCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpNorth':
        goalCoordinate = resolveMoveUpNorthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpSouth':
        goalCoordinate = resolveMoveUpSouthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'useHole':
        goalCoordinate = resolveUseHoleCoordinate(
            radarCoordinate, waypoint['coordinate'])
    else:
        goalCoordinate = resolveFloorCoordinate(
            radarCoordinate, waypoint['coordinate'])
    return goalCoordinate
