from time import time
from refill import core


class BuyItemTask:
    def __init__(self, itemNameWithQuantity):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'buyItem'
        self.status = 'notStarted'
        self.value = itemNameWithQuantity

    def shouldIgnore(self, context):
        return True

    def do(self, context):
        core.buyItem(context['screenshot'],
                     (self.value.itemName, self.value.quantity))
        return context

    def shouldRestart(self, _):
        return False

    def did(self, context):
        return True

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        context['waypoints']['currentIndex'] += 1
        context['waypoints']['state'] = None
        return context
