import numpy as np
import pyautogui
import time
import battleList.core
import hud.creatures
from . import baseTasks


def doAttackClosestCreature(context, closestCreature):
    x, y = closestCreature['windowCoordinate']
    pyautogui.rightClick(x, y)
    return context


def makeAttackClosestCreatureTask(closestCreature):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 0,
        'delayAfterComplete': 0.1,
        'shouldExec': lambda context: True,
        'do': lambda context: doAttackClosestCreature(context, closestCreature),
        'did': lambda _: True,  # Verificar se a criatura tem target
        'didNotComplete': lambda context: context,
        'shouldRestart': lambda context: False,  # Verificar se ficou sem target
        'status': 'notStarted',
        'value': closestCreature,
    }
    return ('attackClosestCreature', task)


def makeAttackClosestCreatureTasks(context, closestCreature):
    tasksArray = np.array([], dtype=baseTasks.taskType)
    tasksToAppend = np.array([
        makeAttackClosestCreatureTask(closestCreature),
    ], dtype=baseTasks.taskType)
    tasksArray = np.append(tasksArray, [tasksToAppend])
    floorTasks = baseTasks.makeWalkpointTasks(
        context, closestCreature['radarCoordinate'])
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=baseTasks.taskType)
        tasksArray = np.append(tasksArray, [taskToAppend])
    return tasksArray


def makeFollowCreatureTasks(context, closestCreature):
    tasksArray = np.array([], dtype=baseTasks.taskType)
    floorTasks = baseTasks.makeWalkpointTasks(
        context, closestCreature['radarCoordinate'])
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=baseTasks.taskType)
        tasksArray = np.append(tasksArray, [taskToAppend])
    return tasksArray


def resolveCavebotTasks(context):
    isAttackingSomeCreature = battleList.core.isAttackingSomeCreature(
        context['battleListCreatures'])
    if isAttackingSomeCreature:
        targetCreature = hud.creatures.getTargetCreature(
            context['hudCreatures'])
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            print('hasNoTargetCreature 1')
            return None
        hasNoTargetToTargetCreature = hud.creatures.hasTargetToCreature(
            context['hudCreatures'], targetCreature, context['radarCoordinate']) == False
        if hasNoTargetToTargetCreature:
            targetCreature = hud.creatures.getClosestCreature(
                context['hudCreatures'], context['radarCoordinate'])
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                print('hasNoTargetCreature 2')
                return None
        # - regenerar tasks se for preciso para seguir a criatura
        tasks = makeFollowCreatureTasks(context, targetCreature)
        return tasks
    targetCreature = hud.creatures.getClosestCreature(
        context['hudCreatures'], context['radarCoordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        print('hasNoTargetCreature 3')
        return None
    tasks = makeAttackClosestCreatureTasks(context, targetCreature)
    return tasks
