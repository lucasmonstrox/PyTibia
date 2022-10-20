import numpy as np
import pyautogui
import time
import hud.core
import hud.slot
import gameplay.baseTasks


def doClickHoleTask(context, waypoint):
    slot = hud.core.getSlotFromCoordinate(
        context['radarCoordinate'], waypoint['coordinate'])
    hud.slot.clickSlot(slot, context['hudCoordinate'])
    return context


def doOpenHole(context, roleRadarCoordinate):
    slot = hud.core.getSlotFromCoordinate(
        context['radarCoordinate'], roleRadarCoordinate)
    pyautogui.press('f9')
    hud.slot.clickSlot(slot, context['hudCoordinate'])
    return context


def didClickHoleTask(context, waypoint):
    didTask = np.all(context['waypoints']['state']
                     ['checkInCoordinate'] == context['radarCoordinate']) == True
    return didTask


def makeClickHoleTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: True,  # TODO: check if is near to hole
        'do': lambda context: doClickHoleTask(context, waypoint),
        'did': lambda _: True,
        'didNotComplete': lambda context: context,
        'shouldRestart': lambda context: didClickHoleTask(context, waypoint),
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('goDownHole', task)


def makeOpenHoleTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 1,
        'delayAfterComplete': 0.5,
        'shouldExec': lambda context: shouldExecOpenHole(context, waypoint['coordinate']),
        'do': lambda context: doOpenHole(context, waypoint['coordinate']),
        'did': lambda _: True,
        'didNotComplete': lambda context: context,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('openHole', task)


def makeUseShovelTasks(context, goalCoordinate, waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    floorTasks = gameplay.baseTasks.makeWalkpointTasks(context, goalCoordinate)
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=gameplay.baseTasks.taskType)
        tasks = np.append(tasks, [taskToAppend])
    tasksToAppend = np.array([
        makeOpenHoleTask(waypoint),
        makeClickHoleTask(waypoint),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks


def shouldExecOpenHole(context, waypointCoordinate):
    holeIsClosed = hud.core.isHoleOpen(
        context['hudImg'], context['radarCoordinate'], waypointCoordinate) == False
    return holeIsClosed
