import numpy as np
import battleList.core
from gameplay.groupTasks.makeGroupOfAttackClosestCreatureTasks import makeAttackClosestCreatureTasks
# from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks
import hud.creatures
from gameplay.typings import taskType


def makeFollowCreatureTasks(context, closestCreature):
    tasksArray = np.array([], dtype=taskType)
    # floorTasks = makeGroupOfWalkpointTasks(
    #     context, closestCreature['coordinate'])
    # for floorTask in floorTasks:
    #     taskToAppend = np.array([floorTask], dtype=taskType)
    #     tasksArray = np.append(tasksArray, [taskToAppend])
    return tasksArray


def resolveCavebotTasks(context):
    isAttackingSomeCreature = battleList.core.isAttackingSomeCreature(
        context['battleListCreatures'])
    if isAttackingSomeCreature:
        targetCreature = hud.creatures.getTargetCreature(
            context['monsters'])
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            print('hasNoTargetCreature 1')
            return None
        hasNoTargetToTargetCreature = hud.creatures.hasTargetToCreature(
            context['monsters'], targetCreature, context['coordinate']) == False
        if hasNoTargetToTargetCreature:
            targetCreature = hud.creatures.getClosestCreature(
                context['monsters'], context['coordinate'])
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                print('hasNoTargetCreature 2')
                return None
        # - regenerar tasks se for preciso para seguir a criatura
        tasks = makeFollowCreatureTasks(context, targetCreature)
        return tasks
    targetCreature = hud.creatures.getClosestCreature(
        context['monsters'], context['coordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        print('hasNoTargetCreature 3')
        return None
    tasks = makeAttackClosestCreatureTasks(context, targetCreature)
    return tasks
