import numpy as np
import pyautogui
import tcod
import time
import hud.core
import hud.slot
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
    walkableFloorsSqms = radar.config.walkableFloorsSqms[level][
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
def resolveMoveUpCoordinate(_, nextCoordinate):
    return nextCoordinate


# TODO: add unit tests
def resolveShovelWaypointCoordinate(radarCoordinate, nextCoordinate):
    floorLevel = nextCoordinate[2]
    walkableFloorSqms = radar.config.walkableFloorsSqms[floorLevel]
    availableAroundCoordinates = utils.coordinate.getAvailableAroundCoordinates(
        nextCoordinate, walkableFloorSqms)
    closestCoordinate = utils.coordinate.getClosestCoordinate(
        radarCoordinate, availableAroundCoordinates)
    return closestCoordinate


# TODO: add unit tests
def resolveGoalCoordinate(radarCoordinate, waypoint):
    goalCoordinate = None
    if waypoint['type'] == 'shovel':
        goalCoordinate = resolveShovelWaypointCoordinate(
            radarCoordinate, waypoint['coordinate'])
    elif waypoint['type'] == 'moveUp':
        goalCoordinate = resolveMoveUpCoordinate(
            radarCoordinate, waypoint['coordinate'])
    else:
        goalCoordinate = resolveFloorCoordinate(
            radarCoordinate, waypoint['coordinate'])
    return goalCoordinate


# TODO: add unit tests
def resolveWaypointByType(screenshot, radarCoordinate, waypointsManager):
    copiedWaypointsManager = waypointsManager.copy()
    hasReachedGoalCoordinate = np.all(
        radarCoordinate == copiedWaypointsManager['state']['goalCoordinate'])
    if copiedWaypointsManager['state']['goalWaypoint']['type'] == 'shovel':
        if copiedWaypointsManager['state']['status'] == 'awaiting':
            if hasReachedGoalCoordinate:
                copiedWaypointsManager['state']['status'] = 'isInCoordinate'
                # TODO: send command to sleep 2secs in next frame
                time.sleep(2)
        elif copiedWaypointsManager['state']['status'] == 'isInCoordinate':
            slot = hud.core.getSlotFromCoordinate(
                radarCoordinate, waypointsManager['state']['goalWaypoint']['coordinate'])
            hudCoordinate = hud.core.getCoordinate(screenshot)
            hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
            slotImg = hud.core.getSlotImg(hudImg, slot)
            if hud.core.isHoleOpen(slotImg):
                copiedWaypointsManager['state']['status'] = 'goingToHole'
                newGoalCoordinate = copiedWaypointsManager['state']['goalWaypoint']['coordinate']
                newGoalCoordinate[2] = newGoalCoordinate[2] - 1
                copiedWaypointsManager['state']['goalCoordinate'] = newGoalCoordinate
            else:
                pyautogui.press('f9')
                hudCoordinate = hud.core.getCoordinate(screenshot)
                slot = hud.core.getSlotFromCoordinate(
                    radarCoordinate, waypointsManager['state']['goalWaypoint']['coordinate'])
                hud.slot.clickSlot(slot, hudCoordinate)
    else:
        if hasReachedGoalCoordinate:
            copiedWaypointsManager['state']['status'] = 'done'
    return copiedWaypointsManager


# TODO: add unit tests
def handleWaypoint(screenshot, radarCoordinate, waypointsManager):
    copiedWaypointsManager = waypointsManager.copy()
    nextWaypointIndex = utils.array.getNextArrayIndex(
        copiedWaypointsManager['points'], copiedWaypointsManager['currentIndex'])
    nextWaypoint = copiedWaypointsManager['points'][nextWaypointIndex]
    if copiedWaypointsManager['state'] == None:
        copiedWaypointsManager['state'] = {
            'goalCoordinate': resolveGoalCoordinate(radarCoordinate, nextWaypoint),
            'goalWaypoint': nextWaypoint,
            'status': 'awaiting'
        }
    copiedWaypointsManager = resolveWaypointByType(
        screenshot, radarCoordinate, copiedWaypointsManager)
    hasWaypointResolved = copiedWaypointsManager['state']['status'] == 'done'
    if hasWaypointResolved:
        copiedWaypointsManager['currentIndex'] = nextWaypointIndex
        nextOfNextWaypointIndex = utils.array.getNextArrayIndex(
            copiedWaypointsManager['points'], copiedWaypointsManager['currentIndex'])
        nextWaypoint = copiedWaypointsManager['points'][nextOfNextWaypointIndex]
        copiedWaypointsManager['state'] = {
            'goalCoordinate': resolveGoalCoordinate(radarCoordinate, nextWaypoint),
            'goalWaypoint': nextWaypoint,
            'status': 'awaiting'
        }
    return copiedWaypointsManager


# TODO: add unit tests
def handleWalkpoints(radarCoordinate, walkpointsManager, waypointsManager):
    copiedWalkpointsManager = walkpointsManager.copy()
    shouldRecalculateWalkpoints = len(
        copiedWalkpointsManager['points']) == 0
    if shouldRecalculateWalkpoints:
        copiedWalkpointsManager['lastCoordinateVisited'] = None
        if waypointsManager['state']['goalWaypoint']['type'] == 'moveUp':
            copiedWalkpointsManager['points'] = np.array(
                [waypointsManager['state']['goalCoordinate']])
        elif waypointsManager['state']['goalWaypoint']['type'] == 'moveDown':
            copiedWalkpointsManager['points'] = np.array(
                [waypointsManager['state']['goalCoordinate']])
        else:
            f = abs(waypointsManager['state']['goalCoordinate'][0] -
                    radarCoordinate[0])
            print('f', f)
            if f > 1:
                copiedWalkpointsManager['points'] = generateFloorWalkpoints(
                    radarCoordinate, waypointsManager['state']['goalCoordinate'])
    return copiedWalkpointsManager


# TODO: add unit tests
# TODO: npcs are blocking char
# TODO: blockable objects are blocking char
def walk(radarCoordinate, walkpointsManager):
    copiedWalkpointsManager = walkpointsManager.copy()
    charSpeed = 755
    shouldntWalk = len(copiedWalkpointsManager['points']) == 0
    if shouldntWalk:
        return copiedWalkpointsManager
    currentTime = time.time() * 1000
    differentTimeBeforeLastMove = currentTime - \
        copiedWalkpointsManager['lastCrossedTime']
    nextWalkpointIndex = 0
    tileFriction = radar.core.getTileFrictionByRadarCoordinate(
        copiedWalkpointsManager['points'][nextWalkpointIndex])
    # print('tileFriction', tileFriction)
    movementSpeed = radar.core.getBreakpointTileMovementSpeed(
        charSpeed, tileFriction)
    didntPassedEnoughTime = differentTimeBeforeLastMove * 1.3 < movementSpeed
    # print('movementSpeed', movementSpeed)
    if didntPassedEnoughTime:
        return copiedWalkpointsManager
    copiedWalkpointsManager['lastCrossedTime'] = currentTime
    coordinateDidntChange = np.all(
        radarCoordinate == copiedWalkpointsManager['lastCoordinateVisited'])
    copiedWalkpointsManager['coordinateDidChange'] = not coordinateDidntChange
    if coordinateDidntChange:
        return copiedWalkpointsManager
    copiedWalkpointsManager['lastCoordinateVisited'] = radarCoordinate
    nextWalkpointRadarCoordinate = copiedWalkpointsManager['points'][nextWalkpointIndex]
    direction = utils.coordinate.getDirectionBetweenRadarCoordinates(
        radarCoordinate, nextWalkpointRadarCoordinate)
    beingDeletedWalkpoint = copiedWalkpointsManager['points'][0].copy()
    print('--------------')
    # print(copiedWalkpointsManager['points'])
    # print(len(copiedWalkpointsManager['points']))
    # print('radarCoordinate', radarCoordinate)
    # print('nextWalkpointRadarCoordinate', nextWalkpointRadarCoordinate)
    copiedWalkpointsManager['points'] = np.delete(
        copiedWalkpointsManager['points'], 0, axis=0)
    hasNoNewDirection = direction is None
    if hasNoNewDirection:
        return copiedWalkpointsManager
    # print('lastPressedKey', copiedWalkpointsManager['lastPressedKey'])
    print('direction', direction)
    if len(copiedWalkpointsManager['points']) > 0:
        futureDirection = utils.coordinate.getDirectionBetweenRadarCoordinates(
            beingDeletedWalkpoint, copiedWalkpointsManager['points'][0])
    else:
        futureDirection = None
    print('futureDirection', futureDirection)
    if direction != futureDirection:
        if copiedWalkpointsManager['lastPressedKey'] is not None:
            print('diferente soltei')
            pyautogui.keyUp(direction)
            copiedWalkpointsManager['lastPressedKey'] = None
        else:
            print('diferente pressionei')
            pyautogui.press(direction)
        return copiedWalkpointsManager
    if direction != copiedWalkpointsManager['lastPressedKey']:
        if len(copiedWalkpointsManager['points']) > 1:
            print('igual apertei')
            pyautogui.keyDown(direction)
            copiedWalkpointsManager['lastPressedKey'] = direction
        else:
            print('igual pressionei')
            pyautogui.press(direction)
    return copiedWalkpointsManager
