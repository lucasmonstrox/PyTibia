import json
import numpy as np
from numpy import dtype
import hud.core
import radar.core
import utils.core
import utils.AStar
from hud import creatures
import battleList

waypointArray = np.array([], dtype=dtype)
waypointIndex = None
nextWaypoint = None

waypointType = np.dtype([
    ('routeName', np.str_, 64),
    ('routeType', np.str_, 64),
    ('id', np.uint32),
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('combatStyle', np.str_, 64),
    ('hotkey', np.str_, 64),
    ('waitTime', np.uint32),
    ('minCreatures', np.uint32),
    ('speed', np.uint32),
    ('tolerance', np.uint32)
])


def loadWaypointJSON(filename):
    global waypointArray
    waypointList = []
    wptFile = open(filename)
    jsonFile = json.load(wptFile)
    for i in range(len(jsonFile['routes'])):
        for j in range(len(jsonFile['routes'][i]['waypoints'])):
            waypointList.append((
                jsonFile['routes'][i]['name'],
                jsonFile['routes'][i]['type'],
                jsonFile['routes'][i]['waypoints'][j]['id'],
                jsonFile['routes'][i]['waypoints'][j]['type'],
                tuple(jsonFile['routes'][i]['waypoints'][j]['coord']),
                jsonFile['routes'][i]['waypoints'][j]['combatStyle'],
                jsonFile['routes'][i]['waypoints'][j]['hotkey'],
                jsonFile['routes'][i]['waypoints'][j]['waitTime'],
                jsonFile['routes'][i]['waypoints'][j]['minCreatures'],
                jsonFile['routes'][i]['waypoints'][j]['speed'],
                jsonFile['routes'][i]['waypoints'][j]['tolerance']))

    waypointArray = np.array(waypointList, dtype=waypointType)

    return waypointArray


# TODO: Implement the other types of waypoints
# TODO: Implement routes of type loop and travel and make loop be looping until condition is met
def waypointManager(screenshot, currentPlayerCoordinate):

    global waypointIndex

    if waypointIndex is None:
        waypointIndex = radar.core.getWaypointIndexFromClosestCoordinate(currentPlayerCoordinate, waypointArray)

    if len(waypointArray) == waypointIndex:
        waypointIndex = 0
    waypoint = waypointArray[waypointIndex]

    isGroundWaypoint = waypoint['type'] == 'ground'
    if isGroundWaypoint:
        status = goToNextWaypoint(screenshot, currentPlayerCoordinate)
        if status is True:
            print(f"Reached waypoint idx:{str(waypointIndex)} {waypoint['coordinate'][0]} {waypoint['coordinate'][1]} {waypoint['coordinate'][2]}")
            waypointIndex += 1
        return

    isRampWaypoint = waypoint['type'] == 'ramp'
    if isRampWaypoint:
        (currentPlayerCoordinateX, currentPlayerCoordinateY, _) = currentPlayerCoordinate
        (waypointCoordinateX, waypointCoordinateY, _) = waypoint['coordinate']
        xDifference = currentPlayerCoordinateX - waypointCoordinateX
        shouldWalkToLeft = xDifference > 0
        if shouldWalkToLeft:
            utils.core.press('left')
            return
        shouldWalkToRight = xDifference < 0
        if shouldWalkToRight:
            utils.core.press('right')
            return
        yDifference = currentPlayerCoordinateY - waypointCoordinateY
        if yDifference < 0:
            utils.core.press('down')
            return
        if yDifference > 0:
            utils.core.press('up')
            return

    isTradeWaypoint = waypoint['type'] == 'trade'
    if isTradeWaypoint:
        # TODO: Implement chat method to make trade action
        print('chat method here')
        waypointIndex += 1


def goToNextWaypoint(screenshot, currentPlayerCoordinate):
    global waypointIndex, waypointArray, nextWaypoint
    walkStatus = arrowKeysWalk(screenshot, currentPlayerCoordinate, waypointArray[waypointIndex]['coordinate'])
    if walkStatus is None:
        # TODO: Handle waypoint not on this floor
        print('Method to treat incorrect coordinates here')
        return None
    (hasReachedDestination, isMonsterBlocking) = walkStatus
    newPlayerCoordinate = radar.core.getCoordinate(screenshot, currentPlayerCoordinate)
    if newPlayerCoordinate == currentPlayerCoordinate:
        # TODO: Handle being stuck on the same position
        print('Player is stuck')
    if hasReachedDestination:
        return True
    if isMonsterBlocking:
        # TODO: Handle monster blocking the path
        print('A creature is blocking the path, change stance to attack')
    return False


def arrowKeysWalk(screenshot, origin, destination):

    (x1, y1, z1) = origin
    x1, y1 = utils.core.getPixelFromCoordinate(origin)
    (x2, y2, z2) = destination
    x2, y2 = utils.core.getPixelFromCoordinate(destination)
    if z1 != z2:
        return None

    radarImg = radar.config.floorsImgs[z1][y1 - 50:y1 + 50, x1 - 50:x1 + 50]
    radarWalkableFloorSqms = np.where(
        np.isin(radarImg, radar.config.nonWalkablePixelsColors), 1, 0)
    radarWalkableFloorWithMonstersSqms = np.where(
        np.isin(radarImg, radar.config.nonWalkablePixelsColors), 1, 0)
    battleListCreatures = battleList.core.getCreatures(screenshot)
    creaturesHud = hud.creatures.getCreatures(screenshot, battleListCreatures)

    for creature in creaturesHud:
        radarWalkableFloorWithMonstersSqms[creature['slot'][1] + 45, creature['slot'][0] + 43] = 1

    if abs(y2-y1) <= 1 and abs(x2-x1) <= 1:
        return True, False

    path = utils.AStar.search(radarWalkableFloorWithMonstersSqms, 1, (50, 50), (y2 - y1 + 50, x2 - x1 + 50))

    if path is None:
        path = utils.AStar.search(radarWalkableFloorSqms, 1, (50, 50), (y2 - y1 + 50, x2 - x1 + 50))
        if path is not None:
            return False, True

    (calcY, calcX) = path[1]
    print(f"X: {calcX} Y: {calcY}")

    if calcY < 50 and calcX < 50:
        if radarWalkableFloorSqms[50, 49] == 0:
            utils.core.press('left')
            utils.core.press('up')
        elif radarWalkableFloorSqms[49, 50] == 0:
            utils.core.press('up')
            utils.core.press('left')
        else:
            utils.core.press('q')

    if calcY < 50 and calcX > 50:
        if radarWalkableFloorSqms[50, 51] == 0:
            utils.core.press('right')
            utils.core.press('up')
        elif radarWalkableFloorSqms[49, 50] == 0:
            utils.core.press('up')
            utils.core.press('right')
        else:
            utils.core.press('e')

    if calcY > 50 and calcX < 50:
        if radarWalkableFloorSqms[50, 49] == 0:
            utils.core.press('left')
            utils.core.press('down')
        elif radarWalkableFloorSqms[51, 50] == 0:
            utils.core.press('down')
            utils.core.press('left')
        else:
            utils.core.press('z')

    if calcY > 50 and calcX > 50:
        if radarWalkableFloorSqms[51, 50] == 0:
            utils.core.press('down')
            utils.core.press('right')
        elif radarWalkableFloorSqms[50, 51] == 0:
            utils.core.press('right')
            utils.core.press('down')
        else:
            utils.core.press('c')

    if calcY < 50 and calcX == 50:
        utils.core.press('up')
    if calcY > 50 and calcX == 50:
        utils.core.press('down')
    if calcX < 50 and calcY == 50:
        utils.core.press('left')
    if calcX > 50 and calcY == 50:
        utils.core.press('right')

    return False, False
