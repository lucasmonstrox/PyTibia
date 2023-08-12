import numpy as np
from src.repositories.actionBar.core import getSlotCount
from src.shared.typings import Waypoint
from ...typings import Context
from .common.vector import VectorTask
from .buyItem import BuyItemTask
from .closeNpcTradeBox import CloseNpcTradeBoxTask
from .enableChat import EnableChatTask
from .say import SayTask
from .selectChatTab import SelectChatTabTask
from .setChatOff import SetChatOffTask


class RefillTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'refill'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.waypoint = waypoint

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        healthPotionsAmount = getSlotCount(context['screenshot'], 1)
        manaPotionsAmount = getSlotCount(context['screenshot'], 2)
        amountOfManaPotionsToBuy = max(
            0, self.waypoint['options']['manaPotion']['quantity'] - manaPotionsAmount)
        amountOfHealthPotionsToBuy = max(
            0, self.waypoint['options']['healthPotion']['quantity'] - healthPotionsAmount)
        self.tasks = [
            SelectChatTabTask('local chat').setParentTask(
                self).setRootTask(self),
            EnableChatTask().setParentTask(self).setRootTask(self),
            SayTask('hi').setParentTask(self).setRootTask(self),
            EnableChatTask().setParentTask(self).setRootTask(self),
            SayTask('trade').setParentTask(self).setRootTask(self),
            SetChatOffTask().setParentTask(self).setRootTask(self),
            BuyItemTask(self.waypoint['options']['manaPotion']['item'], amountOfManaPotionsToBuy).setParentTask(
                self).setRootTask(self),
            BuyItemTask(self.waypoint['options']['healthPotion']['item'], amountOfHealthPotionsToBuy).setParentTask(
                self).setRootTask(self),
            CloseNpcTradeBoxTask().setParentTask(self).setRootTask(self),
        ]
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        # TODO: numbait
        labelIndexes = np.argwhere(context['cavebot']['waypoints']['items']
                                   ['label'] == self.waypoint['options']['waypointLabelToRedirect'])[0]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        context['cavebot']['waypoints']['currentIndex'] = labelIndexes[0]
        context['cavebot']['waypoints']['state'] = None
        return context
