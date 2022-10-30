import pyautogui
from time import time
from refill import core


class AttackClosestCreatureTask:
    def __init__(self, closestCreature):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'attackClosestCreature'
        self.status = 'notStarted'
        self.value = closestCreature

    def shouldIgnore(self, context):
        return True

    def do(self, context):
        closestCreature = self.value
        x, y = closestCreature['windowCoordinate']
        pyautogui.rightClick(x, y)
        return context

    def did(self, _):
        # TODO: check if closest creature is being attacked
        return True
    
    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
