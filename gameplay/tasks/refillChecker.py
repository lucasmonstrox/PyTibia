from time import time
from actionBar.core import getSlotCount
from skills.core import getCapacity
from utils.array import getNextArrayIndex


class RefillCheckerTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 1
        self.name = 'refillChecker'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: get correct binds for health potion
        quantityOfHealthPotions = getSlotCount(context['screenshot'], '1')
        # TODO: get correct binds for mana potion
        quantityOfManaPotions = getSlotCount(context['screenshot'], '2')
        hasEnoughHealthPotions = quantityOfHealthPotions > self.value['options']['minimumOfHealthPotions']
        hasEnoughManaPotions = quantityOfManaPotions > self.value['options']['minimumOfManaPotions']
        capacity = getCapacity(context['screenshot'])
        hasEnoughCapacity = capacity > self.value['options']['minimumOfCapacity']
        shouldIgnore = hasEnoughHealthPotions and hasEnoughManaPotions and hasEnoughCapacity
        return shouldIgnore

    def do(self, context):
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        context['waypoints']['currentIndex'] = self.value['options']['successIndex']
        context['waypoints']['state'] = None
        return context

    def onDidComplete(self, context):
        nextWaypointIndex = getNextArrayIndex(
            context['waypoints']['points'], context['waypoints']['currentIndex'])
        context['waypoints']['currentIndex'] = nextWaypointIndex
        context['waypoints']['state'] = None
        return context
