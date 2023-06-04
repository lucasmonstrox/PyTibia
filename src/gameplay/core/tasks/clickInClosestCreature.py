import pyautogui
from src.utils.mouse import leftClick
from ...typings import Context
from .common.base import BaseTask


# TODO: make task retriable
class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'
        self.delayAfterComplete = 0.1
        self.delayOfTimeout = 2

    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnore = context['cavebot']['targetCreature'] is not None
        return shouldIgnore

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        ignoreHotkeyAttack = len(context['gameWindow']['players']) > 0 or context['targeting']['hasIgnorableCreatures']
        if ignoreHotkeyAttack:
            pyautogui.keyDown('alt')
            leftClick(context['cavebot']['closestCreature']['windowCoordinate'])
            pyautogui.keyUp('alt')
            return context
        # TODO: bind automatically
        pyautogui.press('space')
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = context['cavebot']['isAttackingSomeCreature']
        return didTask

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        context['taskOrchestrator'].reset()
        return context
