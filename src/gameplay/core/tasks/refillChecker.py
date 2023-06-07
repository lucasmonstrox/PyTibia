import numpy as np
from src.repositories.actionBar.core import getSlotCount
from src.repositories.skills.core import getCapacity
from src.shared.typings import Waypoint
from src.utils.array import getNextArrayIndex
from ...typings import Context
from .common.base import BaseTask


class RefillCheckerTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'refillChecker'
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.waypoint = waypoint

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        # TODO: get correct binds for health potion
        quantityOfHealthPotions = getSlotCount(context['screenshot'], 1)
        if quantityOfHealthPotions is None:
            return False
        # TODO: get correct binds for mana potion
        quantityOfManaPotions = getSlotCount(context['screenshot'], 2)
        if quantityOfManaPotions is None:
            return False
        hasEnoughHealthPotions = quantityOfHealthPotions > self.waypoint[
            'options']['minimumOfHealthPotions']
        hasEnoughManaPotions = quantityOfManaPotions > self.waypoint['options']['minimumOfManaPotions']
        capacity = getCapacity(context['screenshot'])
        if capacity is None:
            return False
        hasEnoughCapacity = capacity > self.waypoint['options']['minimumOfCapacity']
        shouldIgnoreTask = hasEnoughHealthPotions and hasEnoughManaPotions and hasEnoughCapacity
        return shouldIgnoreTask

    # TODO: add unit tests
    def onIgnored(self, context: Context) -> Context:
        labelIndexes = np.argwhere(context['cavebot']['waypoints']['points']['label'] == self.waypoint['options']['waypointLabelToRedirect'])[0]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        indexToRedirect = labelIndexes[0]
        context['cavebot']['waypoints']['currentIndex'] = indexToRedirect
        context['cavebot']['waypoints']['state'] = None
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        context['cavebot']['waypoints']['state'] = None
        return context
