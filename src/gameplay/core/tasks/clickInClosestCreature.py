from src.utils.keyboard import keyDown, keyUp, press
from src.utils.mouse import leftClick
from ...typings import Context
from .common.base import BaseTask


# TODO: make task retriable
class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'
        self.delayOfTimeout = 1

    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = context['cavebot']['targetCreature'] is not None
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        ignoreHotkeyAttack = len(context['gameWindow']['players']) > 0 or context['targeting']['hasIgnorableCreatures']
        if ignoreHotkeyAttack:
            keyDown('alt')
            leftClick(context['cavebot']['closestCreature']['windowCoordinate'])
            keyUp('alt')
            return context
        # TODO: bind automatically
        press('space')
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = context['cavebot']['isAttackingSomeCreature']
        return didTask

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        context['tasksOrchestrator'].reset()
        return context
