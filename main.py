import kivy.context
import multiprocessing
import numpy as np
import pyautogui
from time import sleep
import win32gui
from rx import interval, operators
from rx.scheduler import ThreadPoolScheduler
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.context import gameContext
from src.gameplay.combo import comboSpellsObserver
from src.gameplay.core.middlewares.battleList import setBattleListMiddleware
from src.gameplay.core.middlewares.chat import setChatTabsMiddleware
from src.gameplay.core.middlewares.gameWindow import setDirection, setHandleLoot, setGameWindowCreatures, setGameWindowMiddleware
from src.gameplay.core.middlewares.playerStatus import setMapPlayerStatusMiddleware
from src.gameplay.core.middlewares.radar import setRadarMiddleware, setWaypointIndex
from src.gameplay.core.middlewares.screenshot import setScreenshot
from src.gameplay.core.middlewares.tasks import setCleanUpTasksMiddleware
from src.gameplay.core.middlewares.window import setTibiaWindowMiddleware
from src.gameplay.core.tasks.groupOfLootCorpse import GroupOfLootCorpseTasks
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
from src.ui.app import MyApp
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    optimalThreadCount = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimalThreadCount)
    fpsCounter = 0.015625
    fpsObserver = interval(fpsCounter)

    def handleGameData(_):
        global gameContext
        if 'taskOrchestrator' not in gameContext:
            gameContext['taskOrchestrator'] = TasksOrchestrator()
        gameContext = setTibiaWindowMiddleware(gameContext)
        if gameContext['pause']:
            return gameContext
        gameContext = setScreenshot(gameContext)
        gameContext = setRadarMiddleware(gameContext)
        gameContext = setChatTabsMiddleware(gameContext)
        gameContext = setBattleListMiddleware(gameContext)
        gameContext = setGameWindowMiddleware(gameContext)
        gameContext = setDirection(gameContext)
        gameContext = setGameWindowCreatures(gameContext)
        gameContext = setHandleLoot(gameContext)
        gameContext = setWaypointIndex(gameContext)
        gameContext = setMapPlayerStatusMiddleware(gameContext)
        gameContext = setCleanUpTasksMiddleware(gameContext)
        return gameContext

    gameObserver = fpsObserver.pipe(
        operators.map(handleGameData),
        operators.filter(lambda ctx: ctx['pause'] == False),
    )

    def releaseKeys(gameContext):
        if gameContext['lastPressedKey'] is not None:
            pyautogui.keyUp(gameContext['lastPressedKey'])
            gameContext['lastPressedKey'] = None
        return gameContext

    def handleGameplayTasks(context):
        global gameContext
        gameContext = context
        if gameContext['taskOrchestrator'].getCurrentTask(gameContext) is not None and gameContext['taskOrchestrator'].getCurrentTask(gameContext).name == 'groupOfSelectLootTab':
            return gameContext
        # if len(gameContext['loot']['corpsesToLoot']) > 0:
        #     gameContext['way'] = 'lootCorpses'
        #     if gameContext['taskOrchestrator'].getCurrentTask() is not None and gameContext['taskOrchestrator'].getCurrentTask().name != 'groupOfLootCorpse':
        #         gameContext['currentTask'] = None
        #     if gameContext['currentTask'] is None:
        #         gameContext = releaseKeys(gameContext)
        #         # TODO: get closest dead corpse
        #         firstDeadCorpse = gameContext['loot']['corpsesToLoot'][0]
        #         gameContext['currentTask'] = GroupOfLootCorpseTasks(firstDeadCorpse)
        #     gameContext['gameWindow']['previousMonsters'] = gameContext['gameWindow']['monsters']
        #     return gameContext
        # if hasCreaturesToAttack(context):
        #     targetCreature = getClosestCreature(gameContext['gameWindow']['creatures'], gameContext['radar']['coordinate'])
        #     if targetCreature is not None:
        #         gameContext['way'] = 'cavebot'
        #     else:
        #         gameContext['way'] = 'waypoint'
        # else:
        #     gameContext['way'] = 'waypoint'
        # if hasCreaturesToAttack(context) and shouldAskForCavebotTasks(gameContext):
        #     hasCurrentTaskAfterCheck = gameContext['currentTask'] is not None
        #     isTryingToAttackClosestCreature = hasCurrentTaskAfterCheck and (gameContext['currentTask'].name == 'groupOfAttackClosestCreature' or gameContext['currentTask'].name == 'groupOfFollowTargetCreature')
        #     isNotTryingToAttackClosestCreature = not isTryingToAttackClosestCreature
        #     if isNotTryingToAttackClosestCreature:
        #         newCurrentTask = resolveCavebotTasks(context)
        #         hasCurrentTask2 = gameContext['currentTask'] is not None
        #         if hasCurrentTask2:
        #             hasTargetCreature = gameContext['cavebot']['targetCreature'] is not None or gameContext['cavebot']['closestCreature'] is not None
        #             if hasTargetCreature:
        #                 gameContext = releaseKeys(gameContext)
        #                 gameContext['currentTask'] = newCurrentTask
        #         else:
        #             hasNewCurrentTask = newCurrentTask is not None
        #             if hasNewCurrentTask:
        #                 gameContext = releaseKeys(gameContext)
        #                 gameContext['currentTask'] = newCurrentTask
        gameContext['way'] = 'waypoint'
        if gameContext['way'] == 'waypoint':
            if gameContext['taskOrchestrator'].getCurrentTask(gameContext) is None:
                currentWaypointIndex = gameContext['cavebot']['waypoints']['currentIndex']
                currentWaypoint = gameContext['cavebot']['waypoints']['points'][currentWaypointIndex]
                resolvedTasksByWaypoint = resolveTasksByWaypoint(context, currentWaypoint)
                gameContext['taskOrchestrator'].setRootTask(resolvedTasksByWaypoint)
        gameContext['gameWindow']['previousMonsters'] = gameContext['gameWindow']['monsters']
        return gameContext

    gameplayObservable = gameObserver.pipe(
        operators.filter(lambda ctx: ctx['pause'] == False),
        operators.map(handleGameplayTasks),
        operators.subscribe_on(threadPoolScheduler),
    )

    def gameplayObserver(context):
        global gameContext
        if gameContext['pause']:
            return
        if gameContext['taskOrchestrator'].getCurrentTask(gameContext) is not None:
            gameContext = gameContext['taskOrchestrator'].do(context)
        gameContext['radar']['lastCoordinateVisited'] = gameContext['radar']['coordinate']

    # def continueWhenIsNotChatTask(context):
    #     if context['currentTask'] is None:
    #         return True
    #     chatTask = ['depositGold', 'groupOfRefill']
    #     return context['currentTask'].name not in chatTask

    # eatFoodObservable = gameObserver.pipe(
    #     operators.filter(continueWhenIsNotChatTask),
    #     operators.subscribe_on(threadPoolScheduler)
    # )
    # healingPriorityObservable = gameObserver.pipe(
    #     operators.filter(continueWhenIsNotChatTask),
    #     operators.subscribe_on(threadPoolScheduler)
    # )
    # healingByPotionsObservable = gameObserver.pipe(
    #     operators.filter(continueWhenIsNotChatTask),
    #     operators.subscribe_on(threadPoolScheduler)
    # )
    # healingBySpellsObservable = gameObserver.pipe(
    #     operators.filter(continueWhenIsNotChatTask),
    #     operators.subscribe_on(threadPoolScheduler)
    # )
    # comboSpellsObservable = gameObserver.pipe(
    #     operators.filter(continueWhenIsNotChatTask),
    #     operators.subscribe_on(threadPoolScheduler)
    # )

    class GameContext:
        def addWaypoint(self, waypoint):
            global gameContext
            gameContext['cavebot']['waypoints']['points'] = np.append(gameContext['cavebot']['waypoints']['points'], np.array([waypoint], dtype=Waypoint))

        def focusInTibia(self):
            global gameContext
            win32gui.ShowWindow(gameContext['window'], 3)
            win32gui.SetForegroundWindow(gameContext['window'])

        def play(self):
            global gameContext
            self.focusInTibia()
            sleep(1)
            gameContext['pause'] = False

        def pause(self):
            global gameContext
            gameContext['pause'] = True
            gameContext['taskOrchestrator'].reset()
            gameContext = releaseKeys(gameContext)

        def getCoordinate(self):
            global gameContext
            screenshot = getScreenshot()
            coordinate = getCoordinate(screenshot, previousCoordinate=gameContext['radar']['previousCoordinate'])
            return coordinate

        def toggleHealingPotionsByKey(self, healthPotionType, enabled):
            global gameContext
            gameContext['healing']['potions'][healthPotionType]['enabled'] = enabled

        def setHealthPotionHotkeyByKey(self, healthPotionType, hotkey):
            global gameContext
            gameContext['healing']['potions'][healthPotionType]['hotkey'] = hotkey

        def setHealthPotionHpPercentageLessThanOrEqual(self, healthPotionType, hpPercentage):
            global gameContext
            gameContext['healing']['potions'][healthPotionType]['hpPercentageLessThanOrEqual'] = hpPercentage

        def toggleManaPotionsByKey(self, manaPotionType, enabled):
            global gameContext
            gameContext['healing']['potions'][manaPotionType]['enabled'] = enabled

        def setManaPotionManaPercentageLessThanOrEqual(self, manaPotionType, manaPercentage):
            global gameContext
            gameContext['healing']['potions'][manaPotionType]['manaPercentageLessThanOrEqual'] = manaPercentage

        def toggleHealingSpellsByKey(self, contextKey, enabled):
            global gameContext
            gameContext['healing']['spells'][contextKey]['enabled'] = enabled

        def setHealingSpellsHpPercentage(self, contextKey, hpPercentage):
            global gameContext
            gameContext['healing']['spells'][contextKey]['hpPercentageLessThanOrEqual'] = hpPercentage

        def setHealingSpellsHotkey(self, contextKey, hotkey):
            global gameContext
            gameContext['healing']['spells'][contextKey]['hotkey'] = hotkey

    try:
        # eatFoodObservable.subscribe(eatFoodObserver)
        # healingPriorityObservable.subscribe(healingPriorityObserver)
        # healingByPotionsObservable.subscribe(healingByPotionsObserver)
        # healingBySpellsObservable.subscribe(healingBySpellsObserver)
        # comboSpellsObservable.subscribe(comboSpellsObserver)
        gameplayObservable.subscribe(gameplayObserver)
        kivy.context.register_context('game', GameContext)
        MyApp().run()
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()