from battleList.core import isAttackingSomeCreature
from hud.creatures import getClosestCreature, getTargetCreature, hasTargetToCreature
from .groupTasks.groupOfAttackClosestCreatureTasks import GroupOfAttackClosestCreatureTasks
from .groupTasks.groupOfFollowTargetCreatureTasks import GroupOfFollowTargetCreatureTasks


def resolveCavebotTasks(context):
    if isAttackingSomeCreature(context['battleListCreatures']):
        targetCreature = getTargetCreature(context['monsters'])
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            return targetCreature, None
        hasNoTargetToTargetCreature = hasTargetToCreature(
            context['monsters'], targetCreature, context['coordinate']) == False
        if hasNoTargetToTargetCreature:
            targetCreature = getClosestCreature(context['monsters'], context['coordinate'])
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                return targetCreature, None
            return targetCreature, GroupOfAttackClosestCreatureTasks(context, targetCreature)
        # TODO: recalculate route if something cross walkpoints
        return targetCreature, GroupOfFollowTargetCreatureTasks(context, targetCreature)
    targetCreature = getClosestCreature(context['monsters'], context['coordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        return targetCreature, None
    return targetCreature, GroupOfAttackClosestCreatureTasks(context, targetCreature)
