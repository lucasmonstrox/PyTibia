import numpy as np
import pyautogui
import time
import hud.core
import hud.slot
import utils.coordinate
from . import waypoint as wp


taskType = np.dtype([
    ('type', np.str_, 64),
    ('data', np.object_),
])


def openHole(context, roleRadarCoordinate):
    slot = hud.core.getSlotFromCoordinate(
        context['radarCoordinate'], roleRadarCoordinate)
    pyautogui.press('f9')
    hud.slot.clickSlot(slot, context['hudCoordinate'])
    return context


def makeOpenHoleTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 1,
        'shouldExec': lambda context: hud.core.isHoleOpen(context['hudImg'], context['radarCoordinate'], waypoint['coordinate']) == False,
        'do': lambda context: openHole(context, waypoint['coordinate']),
        'did': lambda _: True,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('openHole', task)


def doClickHoleTask(context, waypoint):
    slot = hud.core.getSlotFromCoordinate(
        context['radarCoordinate'], waypoint['coordinate'])
    hud.slot.clickSlot(slot, context['hudCoordinate'])
    return context


def makeClickHoleTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 2,
        'shouldExec': lambda context: True,
        'do': lambda context: doClickHoleTask(context, waypoint),
        'did': lambda _: True,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('goDownHole', task)


def makeUseShovelTasks(context, goalCoordinate, waypoint):
    tasks = np.array([], dtype=taskType)
    floorTasks = makeFloorTasks(context, goalCoordinate)
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=taskType)
        tasks = np.append(tasks, [taskToAppend])
    tasksToAppend = np.array([
        makeOpenHoleTask(waypoint),
        makeClickHoleTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks


def makeFloorTasks(context, waypointRadarCoordinate):
    walkpoints = wp.generateFloorWalkpoints(
        context['radarCoordinate'], waypointRadarCoordinate)
    tasks = np.array([], dtype=taskType)
    for walkpoint in walkpoints:
        walkpointTask = makeWalkpointTask(walkpoint)
        taskToAppend = np.array([walkpointTask], dtype=taskType)
        tasks = np.append(tasks, [taskToAppend])
    return tasks


def makeMoveDownNorthTasks(context, goalCoordinate, waypointRadarCoordinate):
    tasks = makeFloorTasks(context, waypointRadarCoordinate)
    walkpointTask = makeWalkpointTask(goalCoordinate)
    taskToAppend = np.array([walkpointTask], dtype=taskType)
    tasks = np.append(tasks, [taskToAppend])
    return tasks


def makeMoveUpNorthTasks(context, goalCoordinate, waypointRadarCoordinate):
    tasks = makeFloorTasks(context, waypointRadarCoordinate)
    walkpointTask = makeWalkpointTask(goalCoordinate)
    taskToAppend = np.array([walkpointTask], dtype=taskType)
    tasks = np.append(tasks, [taskToAppend])
    return tasks


def shouldExecWalkpoint(context):
    isStartingFromLastCoordinate = context['lastCoordinateVisited'] is None or np.any(
        context['radarCoordinate'] == context['lastCoordinateVisited']) == True
    return isStartingFromLastCoordinate


def doWalkpointTask(context, walkpoint):
    copyOfContext = context.copy()
    hasMoreWalkpointTasks = len(
        copyOfContext['tasks']) > 1 and copyOfContext['tasks'][1]['type'] == 'walk'
    direction = utils.coordinate.getDirectionBetweenRadarCoordinates(
        copyOfContext['radarCoordinate'], walkpoint)
    hasNoNewDirection = direction is None
    if hasNoNewDirection:
        return copyOfContext
    futureDirection = None
    if hasMoreWalkpointTasks:
        futureDirection = utils.coordinate.getDirectionBetweenRadarCoordinates(
            walkpoint, copyOfContext['tasks'][1]['data']['value'])
    if direction != futureDirection:
        if copyOfContext['lastPressedKey'] is not None:
            pyautogui.keyUp(copyOfContext['lastPressedKey'])
            copyOfContext['lastPressedKey'] = None
        else:
            pyautogui.press(direction)
        return copyOfContext
    else:
        filterByWalkTasks = copyOfContext['tasks']['type'] == 'walk'
        walkTasks = copyOfContext['tasks'][filterByWalkTasks]
        walkTasksLength = len(walkTasks)
        if direction != copyOfContext['lastPressedKey']:
            if walkTasksLength > 2:
                pyautogui.keyDown(direction)
                copyOfContext['lastPressedKey'] = direction
            else:
                pyautogui.press(direction)
        elif walkTasksLength == 1:
            if copyOfContext['lastPressedKey'] is not None:
                pyautogui.keyUp(copyOfContext['lastPressedKey'])
                copyOfContext['lastPressedKey'] = None
    return copyOfContext


def didWalkpointTask(radarCoordinate, nextwalkpoint):
    response = np.any(radarCoordinate == nextwalkpoint)
    didTask = response == True
    return didTask


def shouldRestartWalkpointTask(context):
    return False


def makeWalkpointTask(walkpoint):
    data = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 0,
        'shouldExec': lambda context: shouldExecWalkpoint(context),
        'do': lambda context: doWalkpointTask(context, walkpoint),
        'did': lambda context: didWalkpointTask(context['radarCoordinate'], walkpoint),
        'shouldRestart': lambda context: shouldRestartWalkpointTask(context),
        'status': 'notStarted',
        'value': walkpoint
    }
    return ('walk', data)


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'floor':
        floorTasks = makeFloorTasks(
            context, waypoint['coordinate'])
        return floorTasks
    elif waypoint['type'] == 'moveDownNorth':
        moveDownTasks = makeMoveDownNorthTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint['coordinate'])
        return moveDownTasks
    elif waypoint['type'] == 'moveUpNorth':
        moveUpNorthTasks = makeMoveUpNorthTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint['coordinate'])
        return moveUpNorthTasks
    elif waypoint['type'] == 'useShovel':
        useShovelTasks = makeUseShovelTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint)
        for useShovelTask in useShovelTasks:
            context['tasks'] = np.append(context['tasks'], [useShovelTask])
        return useShovelTasks
