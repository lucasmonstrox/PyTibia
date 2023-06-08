import src.utils.keyboard as keyboard
import src.utils.mouse as mouse
from ...typings import Context
from .common.base import BaseTask


class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'
        self.delayOfTimeout = 1

    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = context['cavebot']['targetCreature'] is not None
        return shouldIgnoreTask

    def do(self, context: Context) -> Context:
        ignoreHotkeyAttack = len(context['gameWindow']['players']) > 0 or context['targeting']['hasIgnorableCreatures']
        if ignoreHotkeyAttack:
            keyboard.keyDown('alt')
            mouse.leftClick(context['cavebot']['closestCreature']['windowCoordinate'])
            keyboard.keyUp('alt')
            return context
        # TODO: bind automatically
        keyboard.press('space')
        return context

    def did(self, context: Context) -> bool:
        didTask = context['cavebot']['isAttackingSomeCreature']
        return didTask

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        # TODO: avoid this, tree should not be reseted manually
        context['tasksOrchestrator'].reset()
        return context
