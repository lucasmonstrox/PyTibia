# import kivy.context
import numpy as np
import pyautogui
from time import sleep, time
import win32gui
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.context import gameContext
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


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    global gameContext

    def handleGameData(context):
        context = setTibiaWindowMiddleware(context)
        if context['pause']:
            return context
        context = setScreenshotMiddleware(context)
        context = setRadarMiddleware(context)
        context = setChatTabsMiddleware(context)
        context = setBattleListMiddleware(context)
        context = setGameWindowMiddleware(context)
        context = setDirectionMiddleware(context)
        context = setGameWindowCreaturesMiddleware(context)
        context = setHandleLootMiddleware(context)
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
                context['tasksOrchestrator'].setRootTask(resolveTasksByWaypoint(currentWaypoint))
        context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
        return context

    def continueWhenIsNotChatTask(context):
        currentTask = context['tasksOrchestrator'].getCurrentTask(context)
        if currentTask is None:
            return True
        chatTask = ['depositGold', 'refill']
        return currentTask.name not in chatTask

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
            gameContext['tasksOrchestrator'].reset()
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
        while True:
            if gameContext['pause']:
                continue
            startTime = time()
            gameContext = handleGameData(gameContext)
            gameContext = handleGameplayTasks(gameContext)
            gameContext = gameContext['tasksOrchestrator'].do(gameContext)
            gameContext['radar']['lastCoordinateVisited'] = gameContext['radar']['coordinate']
            healingByPotionsObserver(gameContext)
            comboSpellsObserver(gameContext)
            endTime = time()
            diff = endTime - startTime
            sleep(max(0.045 - diff, 0))
        # kivy.context.register_context('game', GameContext)
        # MyApp().run()
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()