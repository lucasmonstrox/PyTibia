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
        return GroupOfFollowTargetCreatureTasks(context, targetCreature)
    targetCreature = hud.creatures.getClosestCreature(
        context['monsters'], context['coordinate'])
    hasNoTargetCreature = targetCreature == None
    if hasNoTargetCreature:
        print('hasNoTargetCreature 3')
        return None
    return GroupOfAttackClosestCreatureTasks(context, targetCreature)
