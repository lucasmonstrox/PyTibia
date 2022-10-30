import numpy as np
import battleList.core
from gameplay.groupTasks.makeGroupOfAttackClosestCreatureTasks import makeAttackClosestCreatureTasks
from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks
import hud.creatures
from gameplay.factories.makeAttackClosestCreature import makeAttackClosestCreatureTask
from gameplay.typings import taskType


def makeFollowCreatureTasks(context, closestCreature):
    tasksArray = np.array([], dtype=taskType)
    floorTasks = makeGroupOfWalkpointTasks(
        context, closestCreature['radarCoordinate'])
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=taskType)
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
