import numpy as np
import time
import actionBar.core
import chat.chat
import gameplay.baseTasks
from refill import refill


def doRefillPotionsChecker(context):
    context['waypoints']['currentIndex'] += 1
    context['waypoints']['state'] = None
    return context


def didNotComplete(context):
    context['waypoints']['currentIndex'] = 0
    context['waypoints']['state'] = None
    return context


def makeRefillPotionsCheckerTask(waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: shouldExecRefillPotionsCheckerTask(context),
        'do': lambda context: doRefillPotionsChecker(context),
        'did': lambda _: True,
        'didComplete': lambda context: context,
        'didNotComplete': lambda context: didNotComplete(context),
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('refillPotionsChecker', task)


def doSay(context, phrase):
    chat.chat.sendMessage(context['screenshot'], phrase)
    return context


def doBuyItem(context, itemName, quantity):
    refill.buyItems(context['screenshot'], [(itemName, quantity)])
    return context


def didBuyItemComplete(context):
    context['waypoints']['currentIndex'] += 1
    context['waypoints']['state'] = None
    return context


def makeBuyItem(itemName, quantity):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda _: True,
        'do': lambda context: doBuyItem(context, itemName, quantity),
        'did': lambda _: True,
        'didComplete': lambda context: context,
        'didNotComplete': lambda context: True,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': itemName,
    }
    return ('buyItem', task)


def makeSay(phrase, waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: True,
        'do': lambda context: doSay(context, phrase),
        'did': lambda _: True,
        'didComplete': lambda context: context,
        'didNotComplete': lambda context: True,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': {'phrase': phrase, 'waypoint': waypoint},
    }
    return ('say', task)


def makeRefillTasks(context, waypoint):
    itemSlot = {
        'ultimate spirit potion': '1',
        'mana potion': '2',
    }
    # TODO: take slot quantity automatically
    manaPotionSlot = itemSlot[context['refill']['manaItem']['name']]
    manaPotionsAmount = actionBar.core.getSlotCount(
        context['screenshot'], manaPotionSlot)
    amountOfManaPotionsToBuy = context['refill']['manaItem']['quantity'] - \
        manaPotionsAmount
    # TODO: take slot quantity automatically
    healthPotionSlot = itemSlot[context['refill']['healthItem']['name']]
    healthPotionsAmount = actionBar.core.getSlotCount(
        context['screenshot'], healthPotionSlot)
    amountOfHealthPotionsToBuy = context['refill']['healthItem']['quantity'] - \
        healthPotionsAmount
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    tasksToAppend = np.array([
        makeSay('hi', waypoint),
        # makeSay('trade', waypoint),
        # makeBuyItem(context['refill']['manaItem']
        #             ['name'], amountOfManaPotionsToBuy),
        # makeBuyItem(context['refill']['healthItem']
        #             ['name'], amountOfHealthPotionsToBuy),
        gameplay.baseTasks.makeSetNextWaypoint(),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks


def makeRefillPotionsCheckerTasks(waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    tasksToAppend = np.array([
        makeRefillPotionsCheckerTask(waypoint),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks


def shouldExecRefillPotionsCheckerTask(context):
    quantityOfHealthPotions = actionBar.core.getSlotCount(
        context['screenshot'], '1')
    quantityOfManaPotions = actionBar.core.getSlotCount(
        context['screenshot'], '2')
    hasNotEnoughHealthPotions = quantityOfHealthPotions < context['refill'][
        'healthItem']['quantity']
    hasNotEnoughManaPotions = quantityOfManaPotions < context['refill'][
        'manaItem']['quantity']
    shouldExec = hasNotEnoughHealthPotions or hasNotEnoughManaPotions
    return shouldExec
