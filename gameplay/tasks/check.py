import numpy as np
import time
import actionBar.core
import gameplay.baseTasks
import skills.core


def doCheck(context):
    context['waypoints']['currentIndex'] = 10  # TODO: replace by variable
    context['waypoints']['state'] = None
    return context


def didNotComplete(context):
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
        'didComplete': lambda context: context,
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
    quantityOfCapacity = skills.core.getCapacity(context['screenshot'])
    quantityOfHealthPotions = actionBar.core.getSlotCount(
        context['screenshot'], '1')
    quantityOfManaPotions = actionBar.core.getSlotCount(
        context['screenshot'], '2')
    hasEnoughCapacity = quantityOfCapacity > waypoint['options']['minimumOfCapacity']
    hasEnoughHealthPotions = quantityOfHealthPotions > waypoint['options'][
        'minimumOfHealthPotions']
    hasEnoughManaPotions = quantityOfManaPotions > waypoint['options'][
        'minimumOfManaPotions']
    shouldExec = hasEnoughCapacity and hasEnoughHealthPotions and hasEnoughManaPotions
    return shouldExec
