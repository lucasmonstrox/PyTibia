import pyautogui
from time import time


class AttackClosestCreatureTask:
    def __init__(self, closestCreature):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = 2
        self.name = 'attackClosestCreature'
        self.status = 'notStarted'
        self.value = closestCreature

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        closestCreature = self.value
        x, y = closestCreature['windowCoordinate']
        pyautogui.rightClick(x, y)
        return context

    def did(self, context):
        hasTargetCreature = context['targetCreature'] is not None
        return hasTargetCreature

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
