import battleList.core
from .groupTasks.groupOfAttackClosestCreatureTasks import GroupOfAttackClosestCreatureTasks
from .groupTasks.groupOfFollowTargetCreatureTasks import GroupOfFollowTargetCreatureTasks
import hud.creatures


def resolveCavebotTasks(context):
    isAttackingSomeCreature = battleList.core.isAttackingSomeCreature(
        context['battleListCreatures'])
    if isAttackingSomeCreature:
        targetCreature = hud.creatures.getTargetCreature(
            context['monsters'])
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            return targetCreature, None
        hasNoTargetToTargetCreature = hud.creatures.hasTargetToCreature(
            context['monsters'], targetCreature, context['coordinate']) == False
        if hasNoTargetToTargetCreature:
            targetCreature = hud.creatures.getClosestCreature(
                context['monsters'], context['coordinate'])
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                return targetCreature, None
            return targetCreature, GroupOfAttackClosestCreatureTasks(context, targetCreature)
        # TODO: check if follow target is really necessary to recalculate
        return targetCreature, GroupOfFollowTargetCreatureTasks(context, targetCreature)
    targetCreature = hud.creatures.getClosestCreature(
        context['monsters'], context['coordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        return targetCreature, None
    return targetCreature, GroupOfAttackClosestCreatureTasks(context, targetCreature)
