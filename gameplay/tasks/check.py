import numpy as np
import time
import actionBar.core
import gameplay.baseTasks
import skills.core


def doCheck(context):
    print('eu vou fazerrrrrrrrrrrrrrrrr')
    context['waypoints']['currentIndex'] = 10
    context['waypoints']['state'] = None
    return context


def didNotComplete(context):
    print('eu nao completeiiiiiiiiii')
    context['waypoints']['currentIndex'] += 1
    context['waypoints']['state'] = None
    return context


def makeCheckTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: shouldExecCheckTask(context, waypoint),
        'do': lambda context: doCheck(context),
        'did': lambda _: True,
        'didNotComplete': lambda context: didNotComplete(context),
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('check', task)


def makeCheckTasks(waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    tasksToAppend = np.array([
        makeCheckTask(waypoint),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks


def shouldExecCheckTask(context, waypoint):
    quantityOfHealthPotions = actionBar.core.getSlotCount(
        context['screenshot'], '1')
    quantityOfCapacity = skills.core.getCapacity(context['screenshot'])
    shouldExec = quantityOfHealthPotions > waypoint['options'][
        'minimumOfHealthPotions'] or quantityOfCapacity > waypoint['options']['minimumOfCapacity']
    return shouldExec
