from typing import Union
from src.repositories.gameWindow.creatures import hasTargetToCreature
from .core.tasks.attackClosestCreature import AttackClosestCreatureTask
from .typings import Context


# TODO: add unit tests
def resolveCavebotTasks(context: Context) -> Union[AttackClosestCreatureTask, None]:
    currentTask = context['taskOrchestrator'].getCurrentTask(context)
    if context['cavebot']['isAttackingSomeCreature']:
        if context['cavebot']['targetCreature'] == None:
            return context
        if hasTargetToCreature(
            context['gameWindow']['monsters'], context['cavebot']['targetCreature'], context['radar']['coordinate']) == False:
            if context['cavebot']['closestCreature'] == None:
                return context
            context['taskOrchestrator'].setRootTask(AttackClosestCreatureTask())
            return context
        if currentTask is None or context['taskOrchestrator'].rootTask.name != 'attackClosestCreature':
            context['taskOrchestrator'].setRootTask(AttackClosestCreatureTask())
        return context
    if context['cavebot']['closestCreature'] == None:
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
