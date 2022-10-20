import numpy as np
import pyautogui
import time
import utils.coordinate
from . import waypoint as wp


taskType = np.dtype([
    ('type', np.str_, 64),
    ('data', np.object_),
])


def didWalkpointTask(radarCoordinate, nextwalkpoint):
    response = np.all(radarCoordinate == nextwalkpoint)
    didTask = response == True
    return didTask


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


def makeWalkpointTask(walkpoint):
    data = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 0,
        'delayAfterComplete': 0,
        'shouldExec': lambda context: shouldExecWalkpointTask(context),
        'do': lambda context: doWalkpointTask(context, walkpoint),
        'did': lambda context: didWalkpointTask(context['radarCoordinate'], walkpoint),
        'didNotComplete': lambda context: context,
        'shouldRestart': lambda context: shouldRestartWalkpointTask(context),
        'status': 'notStarted',
        'value': walkpoint
    }
    return ('walk', data)


def makeWalkpointTasks(context, waypointRadarCoordinate):
    walkpoints = wp.generateFloorWalkpoints(
        context['radarCoordinate'], waypointRadarCoordinate)
    tasks = np.array([], dtype=taskType)
    for walkpoint in walkpoints:
        walkpointTask = makeWalkpointTask(walkpoint)
        taskToAppend = np.array([walkpointTask], dtype=taskType)
        tasks = np.append(tasks, [taskToAppend])
    return tasks


def shouldExecWalkpointTask(context):
    isStartingFromLastCoordinate = context['lastCoordinateVisited'] is None or np.any(
        context['radarCoordinate'] == context['lastCoordinateVisited']) == True
    return isStartingFromLastCoordinate


def shouldRestartWalkpointTask(context):
    return False
