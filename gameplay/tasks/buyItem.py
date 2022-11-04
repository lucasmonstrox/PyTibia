from time import time
from refill import core


class BuyItemTask:
    def __init__(self, itemNameWithQuantity):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'buyItem'
        self.status = 'notStarted'
        self.value = itemNameWithQuantity

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        core.buyItem(context['screenshot'], self.value)
        return context

    def shouldRestart(self, _):
        return False

    def did(self, _):
        return True

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
