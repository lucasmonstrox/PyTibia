import numpy as np
from src.repositories.actionBar.core import getSlotCount
from src.shared.typings import Waypoint
from ...typings import Context
from .common.vector import VectorTask
from .buyItem import BuyItemTask
from .closeNpcTradeBox import CloseNpcTradeBoxTask
from .say import SayTask
from .selectChatTab import SelectChatTabTask
from .setChatOff import SetChatOffTask
from .setNextWaypoint import SetNextWaypointTask


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
        # TODO: inherit from context bindings
        itemSlot = {
            'great health potion': 1,
            'great mana potion': 2,
            'great spirit potion': 1,
            'health potion': 1,
            'mana potion': 2,
            'strong health potion': 1,
            'strong mana potion': 2,
            'supreme health potion': 1,
            'ultimate health potion': 1,
            'ultimate mana potion': 2,
            'ultimate spirit potion': 1,
        }
        manaPotionSlot = itemSlot[context['refill']['mana']['item']]
        manaPotionsAmount = getSlotCount(
            context['screenshot'], manaPotionSlot)
        amountOfManaPotionsToBuy = max(0, context['refill']['mana']['quantity'] - \
            manaPotionsAmount)
        healthPotionSlot = itemSlot[context['refill']['health']['item']]
        healthPotionsAmount = getSlotCount(
            context['screenshot'], healthPotionSlot)
        amountOfHealthPotionsToBuy = max(0, context['refill']['health']['quantity'] - \
            healthPotionsAmount)
        self.tasks = [
            SelectChatTabTask('local chat').setParentTask(self).setRootTask(self),
            SayTask('hi').setParentTask(self).setRootTask(self),
            SayTask('trade').setParentTask(self).setRootTask(self),
            BuyItemTask((context['refill']['mana']['item'], amountOfManaPotionsToBuy)).setParentTask(self).setRootTask(self),
            BuyItemTask((context['refill']['health']['item'], amountOfHealthPotionsToBuy)).setParentTask(self).setRootTask(self),
            CloseNpcTradeBoxTask().setParentTask(self).setRootTask(self),
            SetChatOffTask().setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        # TODO: numbait
        labelIndexes = np.argwhere(context['cavebot']['waypoints']['points']['label'] == self.value['options']['waypointLabelToRedirect'])[0]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        indexToRedirect = labelIndexes[0]
        context['cavebot']['waypoints']['currentIndex'] = indexToRedirect
        context['cavebot']['waypoints']['state'] = None
        return context
