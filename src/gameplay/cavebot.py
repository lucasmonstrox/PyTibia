from src.features.gameWindow.creatures import getClosestCreature, hasTargetToCreature
from .core.tasks.groupOfAttackClosestCreature import GroupOfAttackClosestCreatureTasks
from .core.tasks.groupOfFollowTargetCreature import GroupOfFollowTargetCreatureTasks


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def resolveCavebotTasks(context):
    if context['cavebot']['isAttackingSomeCreature']:
        hasNoTargetCreature = context['cavebot']['targetCreature'] == None
        if hasNoTargetCreature:
            return None
        hasNoTargetToTargetCreature = hasTargetToCreature(
            context['gameWindow']['monsters'], context['cavebot']['targetCreature'], context['radar']['coordinate']) == False
        if hasNoTargetToTargetCreature:
            context['cavebot']['closestCreature'] = getClosestCreature(context['gameWindow']['monsters'], context['radar']['coordinate'])
            hasNoClosestCreature = context['cavebot']['closestCreature'] == None
            if hasNoClosestCreature:
                return None
            return GroupOfAttackClosestCreatureTasks(context)
        # TODO: recalculate route if something cross walkpoints
        return GroupOfFollowTargetCreatureTasks(context)
    context['cavebot']['closestCreature'] = getClosestCreature(context['gameWindow']['monsters'], context['radar']['coordinate'])
    hasNoClosestCreature = context['cavebot']['closestCreature'] == None
    if hasNoClosestCreature:
        return None
    return GroupOfAttackClosestCreatureTasks(context)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def shouldAskForCavebotTasks(context):
    if context['way'] != 'cavebot':
        return False
    if context['currentTask'] is None:
        return True
    return (context['currentTask'].name not in ['groupOfLootCorpse', 'groupOfRefillChecker', 'groupOfSingleWalk', 'useRopeWaypoint', 'useShovelWaypoint'])
