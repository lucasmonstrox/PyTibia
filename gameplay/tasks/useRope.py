import numpy as np
import pyautogui
import time
import hud.core
import hud.slot
import gameplay.baseTasks


def doUseRope(context, roleRadarCoordinate):
    slot = hud.core.getSlotFromCoordinate(
        context['radarCoordinate'], roleRadarCoordinate)
    pyautogui.press('f8')
    hud.slot.clickSlot(slot, context['hudCoordinate'])
    return context


def makeUseRopeTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: True,
        'do': lambda context: doUseRope(context, waypoint['coordinate']),
        'did': lambda _: True,
        'didComplete': lambda context: context,
        'didNotComplete': lambda context: context,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('useRope', task)


def makeUseRopeTasks(context, goalCoordinate, waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    floorTasks = gameplay.baseTasks.makeWalkpointTasks(context, goalCoordinate)
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=gameplay.baseTasks.taskType)
        tasks = np.append(tasks, [taskToAppend])
    tasksToAppend = np.array([
        makeUseRopeTask(waypoint),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
