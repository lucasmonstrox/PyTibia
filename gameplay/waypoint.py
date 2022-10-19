import tcod
import radar.config
import radar.core
import radar.extractors
import utils.array
import utils.coordinate
import utils.core
import utils.image
import utils.mouse
import utils.matrix


# TODO: add unit tests
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


# TODO: add unit tests
def resolveFloorCoordinate(_, nextCoordinate):
    return nextCoordinate


# TODO: add unit tests
def resolveMoveDownNorthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y - 2, floorLevel + 1]
    return goalCoordinate


# TODO: add unit tests
def resolveMoveUpNorthCoordinate(_, nextCoordinate):
    (x, y, floorLevel) = nextCoordinate
    goalCoordinate = [x, y - 2, floorLevel - 1]
    return goalCoordinate


# TODO: add unit tests
def resolveUseShovelWaypointCoordinate(radarCoordinate, nextCoordinate):
    floorLevel = nextCoordinate[2]
    walkableFloorSqms = radar.config.walkableFloorsSqms[floorLevel].copy()
    availableAroundCoordinates = utils.coordinate.getAvailableAroundCoordinates(
        nextCoordinate, walkableFloorSqms)
    closestCoordinate = utils.coordinate.getClosestCoordinate(
        radarCoordinate, availableAroundCoordinates)
    return closestCoordinate


# TODO: add unit tests
def resolveGoalCoordinate(radarCoordinate, waypoint):
    goalCoordinate = None
    if waypoint['type'] == 'useShovel':
        goalCoordinate = resolveUseShovelWaypointCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveDownNorth':
        goalCoordinate = resolveMoveDownNorthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUpNorth':
        goalCoordinate = resolveMoveUpNorthCoordinate(
            radarCoordinate, waypoint['coordinate'])
    else:
        goalCoordinate = resolveFloorCoordinate(
            radarCoordinate, waypoint['coordinate'])
    return goalCoordinate
