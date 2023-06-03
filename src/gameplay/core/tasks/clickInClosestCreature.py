import pyautogui
from src.utils.mouse import leftClick
from ...typings import Context
from .common.base import BaseTask


class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        ignoreHotkeyAttack = len(context['gameWindow']['players']) > 0 or context['targeting']['hasIgnorableCreatures']
        if ignoreHotkeyAttack:
            x, y = context['cavebot']['closestCreature']['windowCoordinate']
            pyautogui.keyDown('alt')
            leftClick(x, y)
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
