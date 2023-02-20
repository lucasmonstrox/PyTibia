import numpy as np
from actionBar.core import getSlotCount
from skills.core import getCapacity
from utils.array import getNextArrayIndex
from .baseTask import BaseTask


class RefillCheckerTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 0
        self.delayAfterComplete = 1
        self.name = 'refillChecker'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: get correct binds for health potion
        quantityOfHealthPotions = getSlotCount(context['screenshot'], 1)
        if quantityOfHealthPotions is None:
            return False
        # TODO: get correct binds for mana potion
        quantityOfManaPotions = getSlotCount(context['screenshot'], 2)
        if quantityOfManaPotions is None:
            return False
        hasEnoughHealthPotions = quantityOfHealthPotions > self.value[
            'options']['minimumOfHealthPotions']
        hasEnoughManaPotions = quantityOfManaPotions > self.value['options']['minimumOfManaPotions']
        capacity = getCapacity(context['screenshot'])
        if capacity is None:
            return False
        hasEnoughCapacity = capacity > self.value['options']['minimumOfCapacity']
        shouldIgnore = hasEnoughHealthPotions and hasEnoughManaPotions and hasEnoughCapacity
        return shouldIgnore

    def onIgnored(self, context):
        labelIndexes = np.argwhere(context['cavebot']['waypoints']['points']['label'] == self.value['options']['waypointLabelToRedirect'])[0]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        indexToRedirect = labelIndexes[0]
        context['cavebot']['waypoints']['currentIndex'] = indexToRedirect
        context['cavebot']['waypoints']['state'] = None
        return context

    def onDidComplete(self, context):
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        context['cavebot']['waypoints']['state'] = None
        return context
