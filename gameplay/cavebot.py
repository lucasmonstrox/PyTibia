import battleList.core
from gameplay.groupTasks.groupOfAttackClosestCreatureTasks import GroupOfAttackClosestCreatureTasks
from gameplay.groupTasks.groupOfFollowTargetCreatureTasks import GroupOfFollowTargetCreatureTasks
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
        return targetCreature, GroupOfFollowTargetCreatureTasks(context, targetCreature)
    targetCreature = hud.creatures.getClosestCreature(
        context['monsters'], context['coordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        return targetCreature, None
    return targetCreature, GroupOfAttackClosestCreatureTasks(context, targetCreature)
