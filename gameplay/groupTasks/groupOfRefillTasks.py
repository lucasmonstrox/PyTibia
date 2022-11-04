import numpy as np
from time import time
from actionBar.core import getSlotCount
from gameplay.factories.makeBuyItemTask import makeBuyItemTask
from gameplay.factories.makeCloseNpcTradeBox import makeCloseNpcTradeBoxTask
from gameplay.factories.makeSayTask import makeSayTask
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType


class GroupOfRefillTasks(GroupTaskExecutor):
    def __init__(self, context, waypoint):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefill'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, waypoint)
        self.value = waypoint

    def generateTasks(self, context, waypoint):
        # TODO: inherit from context bindings
        itemSlot = {
            'great health potion': '1',
            'great mana potion': '2',
            'great spirit potion': '1',
            'health potion': '1',
            'mana potion': '2',
            'strong health potion': '1',
            'strong mana potion': '2',
            'supreme health potion': '1',
            'ultimate health potion': '1',
            'ultimate mana potion': '2',
            'ultimate spirit potion': '1',
        }
        # TODO: take slot quantity automatically
        manaPotionSlot = itemSlot[context['refill']['mana']['item']]
        manaPotionsAmount = getSlotCount(
            context['screenshot'], manaPotionSlot)
        amountOfManaPotionsToBuy = context['refill']['mana']['quantity'] - \
            manaPotionsAmount
        # TODO: take slot quantity automatically
        healthPotionSlot = itemSlot[context['refill']['health']['item']]
        healthPotionsAmount = getSlotCount(
            context['screenshot'], healthPotionSlot)
        amountOfHealthPotionsToBuy = context['refill']['health']['quantity'] - \
            healthPotionsAmount
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([
            makeSayTask('hi'),
            makeSayTask('trade'),
            makeBuyItemTask(
                (context['refill']['mana']['item'], amountOfManaPotionsToBuy)),
            makeBuyItemTask((context['refill']['health']
                            ['item'], amountOfHealthPotionsToBuy)),
            makeCloseNpcTradeBoxTask(),
            makeSetNextWaypointTask(waypoint),
        ], dtype=taskType)
        tasks = np.append(tasks, [tasksToAppend])
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
