import pyautogui
from utils.mouse import leftClick
from .baseTask import BaseTask


class AttackClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayOfTimeout = 1
        self.name = 'attackClosestCreature'

    def do(self, context):
        x, y = context['cavebot']['closestCreature']['windowCoordinate']
        pyautogui.keyDown('alt')
        leftClick(x, y)
        pyautogui.keyUp('alt')
        return context

    def did(self, context):
        return context['cavebot']['isAttackingSomeCreature']
    
    def onDidTimeout(self, context):
        context['currentTask'] = None
        return context
