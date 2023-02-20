from hud.creatures import getClosestCreature, getTargetCreature, hasTargetToCreature
from .tasks.groupOfAttackClosestCreature import GroupOfAttackClosestCreatureTasks
from .tasks.groupOfFollowTargetCreature import GroupOfFollowTargetCreatureTasks


def resolveCavebotTasks(context):
    if context['cavebot']['isAttackingSomeCreature']:
        hasNoTargetCreature = context['cavebot']['targetCreature'] == None
        if hasNoTargetCreature:
            return None
        hasNoTargetToTargetCreature = hasTargetToCreature(
            context['monsters'], context['cavebot']['targetCreature'], context['coordinate']) == False
        if hasNoTargetToTargetCreature:
            context['cavebot']['closestCreature'] = getClosestCreature(context['monsters'], context['coordinate'])
            hasNoClosestCreature = context['cavebot']['closestCreature'] == None
            if hasNoClosestCreature:
                return None
            return GroupOfAttackClosestCreatureTasks(context)
        # TODO: recalculate route if something cross walkpoints
        return GroupOfFollowTargetCreatureTasks(context)
    context['cavebot']['closestCreature'] = getClosestCreature(context['monsters'], context['coordinate'])
    hasNoClosestCreature = context['cavebot']['closestCreature'] == None
    if hasNoClosestCreature:
        return None
    return GroupOfAttackClosestCreatureTasks(context)
