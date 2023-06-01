from typing import Union
from src.repositories.gameWindow.creatures import getClosestCreature, hasTargetToCreature
from .core.tasks.attackClosestCreature import AttackClosestCreatureTask
from .typings import Context


# TODO: add unit tests
def resolveCavebotTasks(context: Context) -> Union[AttackClosestCreatureTask, None]:
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
            return AttackClosestCreatureTask(context)
        # TODO: recalculate route if something cross walkpoints
        return FollowTargetCreatureTasks(context)
    context['cavebot']['closestCreature'] = getClosestCreature(context['gameWindow']['monsters'], context['radar']['coordinate'])
    hasNoClosestCreature = context['cavebot']['closestCreature'] == None
    if hasNoClosestCreature:
        return None
    return AttackClosestCreatureTask(context)


# TODO: add unit tests
def shouldAskForCavebotTasks(context: Context) -> bool:
    if context['way'] != 'cavebot':
        return False
    currentTask = context['taskOrchestrator'].getCurrentTask(context)
    if currentTask is None:
        return True
    return (currentTask.name not in ['dropFlasks', 'lootCorpse', 'refillChecker', 'singleWalk', 'moveDownEast', 'moveDownNorth', 'moveDownSouth', 'moveDownWest', 'moveUpEast', 'moveUpNorth', 'moveUpSouth', 'moveUpWest', 'refillChecker', 'useRopeWaypoint', 'useShovelWaypoint'])
