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
def resolveMoveUpCoordinate(_, nextCoordinate):
    return nextCoordinate


# TODO: add unit tests
def resolveShovelWaypointCoordinate(radarCoordinate, nextCoordinate):
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
    # if copiedWaypointsManager['state'] == None:
    # copiedWaypointsManager['state'] = {
    #     'goalCoordinate': resolveGoalCoordinate(radarCoordinate, nextWaypoint),
    #     'goalWaypoint': nextWaypoint,
    # }
    # copiedWaypointsManager = resolveWaypointByType(
    #     screenshot, radarCoordinate, copiedWaypointsManager)
    # hasWaypointResolved = copiedWaypointsManager['state']['status'] == 'done'
    # if hasWaypointResolved:
    #     copiedWaypointsManager['currentIndex'] = nextWaypointIndex
    #     nextOfNextWaypointIndex = utils.array.getNextArrayIndex(
    #         copiedWaypointsManager['points'], copiedWaypointsManager['currentIndex'])
    #     nextWaypoint = copiedWaypointsManager['points'][nextOfNextWaypointIndex]
    #     copiedWaypointsManager['state'] = {
    #         'goalCoordinate': resolveGoalCoordinate(radarCoordinate, nextWaypoint),
    #         'goalWaypoint': nextWaypoint,
    #         'status': 'awaiting'
    #     }
    return copiedWaypointsManager


# TODO: add unit tests
# TODO: if path is blocked by player, npc, or another block object, maybe reset the path
# TODO: if char doesnt move for some time, maybe reset the path
# TODO: reset path when paralyzed
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
            copiedWalkpointsManager['points'] = generateFloorWalkpoints(
                radarCoordinate, waypointsManager['state']['goalCoordinate'])
    return copiedWalkpointsManager


# TODO: add unit tests
# TODO: if character is walking in a non path, maybe reset the path
def walk(radarCoordinate, walkpointsManager):
    copiedWalkpointsManager = walkpointsManager.copy()
    shouldntWalk = len(copiedWalkpointsManager['points']) == 0
    if shouldntWalk:
        if copiedWalkpointsManager['lastPressedKey'] is not None:
            pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
            copiedWalkpointsManager['lastPressedKey'] = None
        copiedWalkpointsManager['lastCoordinateVisited'] = None
        copiedWalkpointsManager['lastCoordinateVisitedAt'] = None
        return copiedWalkpointsManager
    nextWalkpointIndex = 0
    coordinateDidntChange = np.all(
        radarCoordinate == copiedWalkpointsManager['lastCoordinateVisited'])
    if coordinateDidntChange:
        if copiedWalkpointsManager['lastCoordinateVisitedAt'] is None:
            return copiedWalkpointsManager
        charSpeed = 2250
        tileFriction = radar.core.getTileFrictionByRadarCoordinate(
            copiedWalkpointsManager['points'][nextWalkpointIndex])
        movementSpeed = radar.core.getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        currentTime = time.time()
        timeSinceLastCoordinateVisitedAt = (currentTime -
                                            copiedWalkpointsManager['lastCoordinateVisitedAt']) * 1000
        movementSpeedDot3 = movementSpeed * 3
        shouldResetPath = timeSinceLastCoordinateVisitedAt > movementSpeedDot3
        if shouldResetPath:
            copiedWalkpointsManager['lastCoordinateVisited'] = None
            copiedWalkpointsManager['lastCoordinateVisitedAt'] = None
            copiedWalkpointsManager['points'] = np.array([])
            if copiedWalkpointsManager['lastPressedKey'] is not None:
                pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
                copiedWalkpointsManager['lastPressedKey'] = None
        return copiedWalkpointsManager
    copiedWalkpointsManager['lastCoordinateVisited'] = radarCoordinate
    copiedWalkpointsManager['lastCoordinateVisitedAt'] = time.time()
    nextWalkpointRadarCoordinate = copiedWalkpointsManager['points'][nextWalkpointIndex]
    direction = utils.coordinate.getDirectionBetweenRadarCoordinates(
        radarCoordinate, nextWalkpointRadarCoordinate)
    beingDeletedWalkpoint = copiedWalkpointsManager['points'][0].copy()
    copiedWalkpointsManager['points'] = np.delete(
        copiedWalkpointsManager['points'], 0, axis=0)
    hasNoNewDirection = direction is None
    if hasNoNewDirection:
        return copiedWalkpointsManager
    if len(copiedWalkpointsManager['points']) > 0:
        futureDirection = utils.coordinate.getDirectionBetweenRadarCoordinates(
            beingDeletedWalkpoint, copiedWalkpointsManager['points'][0])
    else:
        futureDirection = None
    if direction != futureDirection:
        if copiedWalkpointsManager['lastPressedKey'] is not None:
            pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
            copiedWalkpointsManager['lastPressedKey'] = None
        else:
            pyautogui.press(direction)
        return copiedWalkpointsManager
    else:
        pointsLength = len(copiedWalkpointsManager['points'])
        if direction != copiedWalkpointsManager['lastPressedKey']:
            if pointsLength > 2:
                pyautogui.keyDown(direction)
                copiedWalkpointsManager['lastPressedKey'] = direction
            else:
                pyautogui.press(direction)
        elif pointsLength == 1:
            if copiedWalkpointsManager['lastPressedKey'] is not None:
                pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
                copiedWalkpointsManager['lastPressedKey'] = None
    return copiedWalkpointsManager
