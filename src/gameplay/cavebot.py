from typing import Union
from src.repositories.gameWindow.creatures import getClosestCreature, hasTargetToCreature
from .core.tasks.groupOfAttackClosestCreature import GroupOfAttackClosestCreatureTasks
from .core.tasks.groupOfFollowTargetCreature import GroupOfFollowTargetCreatureTasks
from .typings import Context


# TODO: add unit tests
def resolveCavebotTasks(context: Context) -> Union[Union[GroupOfAttackClosestCreatureTasks, GroupOfFollowTargetCreatureTasks], None]:
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
def shouldAskForCavebotTasks(context: Context) -> bool:
    if context['way'] != 'cavebot':
        return False
    if context['currentTask'] is None:
        return True
    return (context['currentTask'].name not in ['dropFlasks', 'groupOfLootCorpse', 'groupOfRefillChecker', 'groupOfSingleWalk', 'moveDownEast', 'moveDownNorth', 'moveDownSouth', 'moveDownWest', 'moveUpEast', 'moveUpNorth', 'moveUpSouth', 'moveUpWest', 'refillChecker', 'useRopeWaypoint', 'useShovelWaypoint'])
