import pyautogui
from time import time
from battleList.core import isAttackingSomeCreature


class AttackClosestCreatureTask:
    def __init__(self, closestCreature):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = 1
        self.name = 'attackClosestCreature'
        self.status = 'notStarted'
        self.value = closestCreature

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        closestCreature = self.value
        x, y = closestCreature['windowCoordinate']
        pyautogui.keyDown('alt')
        pyautogui.click(x, y)
        pyautogui.keyUp('alt')
        return context

    def ping(self, context):
        return context

    def did(self, context):
        # TODO: check if creature from specific coordinate/slot is being attacked. Avoid checking on battle list
        return isAttackingSomeCreature(context['battleListCreatures'])

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
