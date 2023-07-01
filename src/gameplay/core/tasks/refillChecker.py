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
        quantityOfHealthPotions = getSlotCount(context['screenshot'], 1)
        if quantityOfHealthPotions is None:
            return False
        quantityOfManaPotions = getSlotCount(context['screenshot'], 2)
        if quantityOfManaPotions is None:
            return False
        capacity = getCapacity(context['screenshot'])
        if capacity is None:
            return False
        hasEnoughHealthPotions = quantityOfHealthPotions > int(self.waypoint[
            'options']['minimumAmountOfHealthPotions'])
        hasEnoughManaPotions = quantityOfManaPotions > int(self.waypoint[
            'options']['minimumAmountOfManaPotions'])
        hasEnoughCapacity = capacity > int(
            self.waypoint['options']['minimumAmountOfCap'])
        return hasEnoughHealthPotions and hasEnoughManaPotions and hasEnoughCapacity

    # TODO: add unit tests
    def onIgnored(self, context: Context) -> Context:
        # TODO: add function to get waypoint by label
        labelIndexes = [index for index, waypoint in enumerate(
            context['cavebot']['waypoints']['items']) if waypoint['label'] == self.waypoint['options']['waypointLabelToRedirect']]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        context['cavebot']['waypoints']['currentIndex'] = labelIndexes[0]
        context['cavebot']['waypoints']['state'] = None
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['items'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        context['cavebot']['waypoints']['state'] = None
        return context
