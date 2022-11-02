import numpy as np
from actionBar.core import getSlotCount
from gameplay.factories.makeBuyItemTask import makeBuyItemTask
from gameplay.factories.makeSayTask import makeSayTask
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.typings import taskType


def makeGroupOfRefillTasks(context, waypoint):
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
        makeSayTask('hi', waypoint),
        makeSayTask('trade', waypoint),
        makeBuyItemTask(context['refill']['mana']
                        ['item'], amountOfManaPotionsToBuy),
        makeBuyItemTask(context['refill']['health']
                        ['item'], amountOfHealthPotionsToBuy),
        makeSetNextWaypointTask(),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
