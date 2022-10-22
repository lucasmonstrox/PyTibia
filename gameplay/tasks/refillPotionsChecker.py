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
        'shouldExec': lambda context: shouldExecRefillPotionsCheckerTask(context, waypoint),
        'do': lambda context: doRefillPotionsChecker(context),
        'did': lambda _: True,
        'didNotComplete': lambda context: didNotComplete(context),
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': waypoint,
    }
    return ('refillPotionsChecker', task)


def doSay(context, phrase):
    chat.chat.sendMessage(context['screenshot'], phrase)
    return context


def doBuyItem(context, itemName):
    refill.buyItems([('mana-potion', 20)])
    return context


def makeBuyItem(itemName, waypoint):
    task = {
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delayBeforeStart': 2,
        'delayAfterComplete': 2,
        'shouldExec': lambda context: True,
        'do': lambda context: doBuyItem(context, itemName),
        'did': lambda _: True,
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
        'didNotComplete': lambda context: True,
        'shouldRestart': lambda context: False,
        'status': 'notStarted',
        'value': {'phrase': phrase, 'waypoint': waypoint},
    }
    return ('say', task)


def makeRefillTasks(waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    tasksToAppend = np.array([
        makeSay('hi', waypoint),
        makeSay('trade', waypoint),
        makeBuyItem('mana-potion', waypoint),
        # makeBuyItem('', waypoint),
        # makeSelectNpcTab(waypoint),
        # makeSay('trade'),
        # calcular quantos health potions falta
        # calcular quantos mana potions falta
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


def shouldExecRefillPotionsCheckerTask(context, waypoint):
    quantityOfHealthPotions = actionBar.core.getSlotCount(
        context['screenshot'], '1')
    quantityOfManaPotions = actionBar.core.getSlotCount(
        context['screenshot'], '2')
    hasNotEnoughHealthPotions = quantityOfHealthPotions < waypoint['options'][
        'minimumOfHealthPotions']
    hasNotEnoughManaPotions = quantityOfManaPotions < waypoint['options'][
        'minimumOfManaPotions']
    shouldExec = hasNotEnoughHealthPotions and hasNotEnoughManaPotions
    return shouldExec
