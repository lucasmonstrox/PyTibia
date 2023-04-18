import pyautogui
from src.utils.mouse import leftClick
from .baseTask import BaseTask


class AttackClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayOfTimeout = 1
        self.name = 'attackClosestCreature'

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
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
    # TODO: add perf
    # TODO: add typings
    def did(self, context):
        return context['cavebot']['isAttackingSomeCreature']

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def onDidTimeout(self, context):
        context['currentTask'] = None
        return context
