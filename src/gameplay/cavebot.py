from typing import Union
from src.repositories.gameWindow.creatures import getClosestCreature, hasTargetToCreature
from .core.tasks.attackClosestCreature import AttackClosestCreatureTask
from .typings import Context


# TODO: add unit tests
def resolveCavebotTasks(context: Context) -> Union[AttackClosestCreatureTask, None]:
    currentTask = context['taskOrchestrator'].getCurrentTask(context)
    context['cavebot']['closestCreature'] = getClosestCreature(context['gameWindow']['monsters'], context['radar']['coordinate'])
    if context['cavebot']['isAttackingSomeCreature']:
        hasNoTargetCreature = context['cavebot']['targetCreature'] == None
        if hasNoTargetCreature:
            return context
        hasNoTargetToTargetCreature = hasTargetToCreature(
            context['gameWindow']['monsters'], context['cavebot']['targetCreature'], context['radar']['coordinate']) == False
        if hasNoTargetToTargetCreature:
            hasNoClosestCreature = context['cavebot']['closestCreature'] == None
            if hasNoClosestCreature:
                return context
            context['taskOrchestrator'].setRootTask(AttackClosestCreatureTask())
            return context
        if currentTask is None or context['taskOrchestrator'].rootTask.name != 'attackClosestCreature':
            context['taskOrchestrator'].setRootTask(AttackClosestCreatureTask())
        return context
    hasNoClosestCreature = context['cavebot']['closestCreature'] == None
    if hasNoClosestCreature:
        return context
    context['taskOrchestrator'].setRootTask(AttackClosestCreatureTask())
    return context


# TODO: add unit tests
def shouldAskForCavebotTasks(context: Context) -> bool:
    if context['way'] != 'cavebot':
        return False
    currentTask = context['taskOrchestrator'].getCurrentTask(context)
    if currentTask is None:
        return True
    return (currentTask.name not in ['dropFlasks', 'lootCorpse', 'moveDown', 'moveUp', 'refillChecker', 'singleWalk', 'refillChecker', 'useRopeWaypoint', 'useShovelWaypoint'])
