from time import time
from refill import core


class BuyItemTask:
    def __init__(self, itemNameWithQuantity):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'buyItem'
        self.status = 'notStarted'
        self.value = itemNameWithQuantity

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        core.buyItem(context['screenshot'],
                     (self.value.itemName, self.value.quantity))
        return context

    def shouldRestart(self, _):
        return False

    def did(self, _):
        return True

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        # TODO: fix this
        context['waypoints']['currentIndex'] += 1
        context['waypoints']['state'] = None
        return context
