import numpy as np
from src.features.actionBar.core import getSlotCount
from ..factories.makeBuyItemTask import makeBuyItemTask
from ..factories.makeCloseNpcTradeBox import makeCloseNpcTradeBoxTask
from ..factories.makeSay import makeSayTask
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfRefillTasks(GroupTaskExecutor):
    def __init__(self, context, waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefill'
        self.tasks = self.generateTasks(context, waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def generateTasks(self, context, _):
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
        return np.array([
            makeSayTask('hi'),
            makeSayTask('trade'),
            makeBuyItemTask((context['refill']['mana']['item'], amountOfManaPotionsToBuy)),
            makeBuyItemTask((context['refill']['health']['item'], amountOfHealthPotionsToBuy)),
            makeCloseNpcTradeBoxTask(),
        ], dtype=Task)

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def onDidComplete(self, context):
        labelIndexes = np.argwhere(context['cavebot']['waypoints']['points']['label'] == self.value['options']['waypointLabelToRedirect'])[0]
        if len(labelIndexes) == 0:
            # TODO: raise error
            return context
        indexToRedirect = labelIndexes[0]
        context['cavebot']['waypoints']['currentIndex'] = indexToRedirect
        context['cavebot']['waypoints']['state'] = None
        return context
