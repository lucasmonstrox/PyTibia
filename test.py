# import kivy.context
import numpy as np
import pyautogui
from time import sleep
import win32gui
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.context import context
from src.gameplay.combo import comboSpellsObserver
from src.gameplay.core.middlewares.battleList import setBattleListMiddleware
from src.gameplay.core.middlewares.chat import setChatTabsMiddleware
from src.gameplay.core.middlewares.gameWindow import setDirectionMiddleware, setHandleLootMiddleware, setGameWindowCreaturesMiddleware, setGameWindowMiddleware
from src.gameplay.core.middlewares.playerStatus import setMapPlayerStatusMiddleware
from src.gameplay.core.middlewares.radar import setRadarMiddleware, setWaypointIndexMiddleware
from src.gameplay.core.middlewares.screenshot import setScreenshotMiddleware
from src.gameplay.core.middlewares.tasks import setCleanUpTasksMiddleware
from src.gameplay.core.middlewares.window import setTibiaWindowMiddleware
from src.gameplay.core.tasks.lootCorpse import LootCorpseTask
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.resolvers import resolveTasksByWaypoint
from src.gameplay.healing.observers.eatFood import eatFoodObserver
from src.gameplay.healing.observers.healingBySpells import healingBySpellsObserver
from src.gameplay.healing.observers.healingByPotions import healingByPotionsObserver
from src.gameplay.healing.observers.healingPriority import healingPriorityObserver
from src.gameplay.targeting import hasCreaturesToAttack
from src.repositories.gameWindow.creatures import getClosestCreature
from src.repositories.radar.core import getCoordinate
from src.repositories.radar.typings import Waypoint
from src.utils.core import getScreenshot
# from src.ui.app import MyApp
import timeit
import numpy as np
from src.repositories.battleList.core import getBeingAttackedCreatureCategory
from src.repositories.chat.core import hasNewLoot
from src.repositories.gameWindow.config import gameWindowSizes
from src.repositories.gameWindow.core import getCoordinate, getImageByCoordinate
from src.repositories.gameWindow.creatures import getCreatures, getCreaturesByType, getDifferentCreaturesBySlots, getTargetCreature
from src.repositories.gameWindow.typings import Creature

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def handleGameData(context):
    # if 'tasksOrchestrator' not in context:
    #     context['tasksOrchestrator'] = TasksOrchestrator()
    context = setTibiaWindowMiddleware(context)
    # if context['pause']:
    #     return context
    context = setScreenshotMiddleware(context)
    context = setRadarMiddleware(context)
    context = setChatTabsMiddleware(context)
    context = setBattleListMiddleware(context)
    context = setGameWindowMiddleware(context)
    context = setDirectionMiddleware(context)
    context = setGameWindowCreaturesMiddleware(context)
    # context = setHandleLootMiddleware(context)
    context = setWaypointIndexMiddleware(context)
    context = setMapPlayerStatusMiddleware(context)
    context = setCleanUpTasksMiddleware(context)
    return context

def releaseKeys(context):
    if context['lastPressedKey'] is not None:
        pyautogui.keyUp(context['lastPressedKey'])
        context['lastPressedKey'] = None
    return context

def handleGameplayTasks(context):
    # TODO: mover isso fora daqui
    context['cavebot']['closestCreature'] = getClosestCreature(context['gameWindow']['monsters'], context['radar']['coordinate'])
    currentTask = context['tasksOrchestrator'].getCurrentTask(context)
    if currentTask is not None and currentTask.name == 'selectLootTab':
        return context
    if len(context['loot']['corpsesToLoot']) > 0:
        context['way'] = 'lootCorpses'
        if currentTask is not None and currentTask.name != 'lootCorpse':
            context['tasksOrchestrator'].setRootTask(None)
        if context['tasksOrchestrator'].getCurrentTask() is None:
            # TODO: get closest dead corpse
            firstDeadCorpse = context['loot']['corpsesToLoot'][0]
            context['tasksOrchestrator'].setRootTask(LootCorpseTask(firstDeadCorpse))
        context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
        return context
    hasCreaturesToAttackAfterCheck = hasCreaturesToAttack(context)
    if hasCreaturesToAttackAfterCheck:
        if context['cavebot']['closestCreature'] is not None:
            context['way'] = 'cavebot'
        else:
            context['way'] = 'waypoint'
    else:
        context['way'] = 'waypoint'
    if hasCreaturesToAttackAfterCheck and shouldAskForCavebotTasks(context):
        currentRootTask = currentTask.rootTask if currentTask is not None else None
        isTryingToAttackClosestCreature = currentRootTask is not None and (currentRootTask.name == 'attackClosestCreature')
        if not isTryingToAttackClosestCreature:
            context = resolveCavebotTasks(context)
    elif context['way'] == 'waypoint':
        if context['tasksOrchestrator'].getCurrentTask(context) is None:
            currentWaypointIndex = context['cavebot']['waypoints']['currentIndex']
            currentWaypoint = context['cavebot']['waypoints']['points'][currentWaypointIndex]
            context['tasksOrchestrator'].setRootTask(resolveTasksByWaypoint(context, currentWaypoint))
    context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
    return context


import pyautogui
from time import time, sleep

context = handleGameData(context)

# TODO: add unit tests
beingAttackedCreatureCategory = getBeingAttackedCreatureCategory(context['battleList']['creatures'])
context['battleList']['beingAttackedCreatureCategory'] = beingAttackedCreatureCategory
context['gameWindow']['creatures'] = getCreatures(
    context['battleList']['creatures'], context['comingFromDirection'], context['gameWindow']['coordinate'], context['gameWindow']['image'], context['radar']['coordinate'], beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=context['gameWindow']['walkedPixelsInSqm'])
# hasNoGameWindowCreatures = len(context['gameWindow']['creatures']) == 0
# context['gameWindow']['monsters'] = np.array([], dtype=Creature) if hasNoGameWindowCreatures else getCreaturesByType(context['gameWindow']['creatures'], 'monster')
# context['gameWindow']['players'] = np.array([], dtype=Creature) if hasNoGameWindowCreatures else getCreaturesByType(context['gameWindow']['creatures'], 'player')

def cenas():
    global context, beingAttackedCreatureCategory
    # context['gameWindow']['creatures'] = getCreatures(
        # context['battleList']['creatures'], context['comingFromDirection'], context['gameWindow']['coordinate'], context['gameWindow']['image'], context['radar']['coordinate'], beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=context['gameWindow']['walkedPixelsInSqm'])
    context = handleGameData(context)
    # context = handleGameplayTasks(context)
    # context = context['tasksOrchestrator'].do(context)
    # context['radar']['lastCoordinateVisited'] = context['radar']['coordinate']
    # healingByPotionsObserver(context)
    # comboSpellsObserver(context)

# res = timeit.repeat(lambda: cenas(), repeat=10, number=1)
# print('res', res)

while True:
    startTime = time()
    context = handleGameData(context)
    # context = handleGameplayTasks(context)
    # context = context['tasksOrchestrator'].do(context)
    context['radar']['lastCoordinateVisited'] = context['radar']['coordinate']
    # healingByPotionsObserver(context)
    # comboSpellsObserver(context)
    endTime = time()
    diff = endTime - startTime
    sleep(max(0.175 - diff, 0))