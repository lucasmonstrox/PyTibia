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
from src.gameplay.core.middlewares.gameWindow import setDirection, setHandleLoot, setGameWindowCreatures, setGameWindowMiddleware
from src.gameplay.core.middlewares.playerStatus import setMapPlayerStatusMiddleware
from src.gameplay.core.middlewares.radar import setRadarMiddleware, setWaypointIndex
from src.gameplay.core.middlewares.screenshot import setScreenshot
from src.gameplay.targeting import hasCreaturesToAttack
from src.gameplay.core.tasks.groupOfLootCorpse import GroupOfLootCorpseTasks
from src.gameplay.resolvers import resolveTasksByWaypoint
from src.gameplay.healing.observers.eatFood import eatFoodObserver
from src.gameplay.healing.observers.healingBySpells import healingBySpellsObserver
from src.gameplay.healing.observers.healingByPotions import healingByPotionsObserver
from src.repositories.radar.core import getCoordinate
from src.repositories.radar.typings import Waypoint
from src.utils.core import getScreenshot
from src.ui.app import MyApp
from src.repositories.gameWindow.creatures import getClosestCreature


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    optimalThreadCount = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimalThreadCount)
    fpsCounter = 0.015625
    fpsObserver = interval(fpsCounter)
    
    def minimizeWindow(hwnd):
        win32gui.ShowWindow(hwnd, win32gui.SW_MINIMIZE)

    def maximizeWindow(hwnd):
        win32gui.ShowWindow(hwnd, 3)

    def focusWindow(hwnd):
        win32gui.SetForegroundWindow(hwnd)

    def handleGameData(_):
        global gameContext
        if gameContext['window'] is None:
            gameContext['window'] = win32gui.FindWindow(None, 'Tibia - Lucas Monstro')
        if gameContext['pause']:
            return gameContext
        gameContext = setScreenshot(gameContext)
        gameContext = setRadarMiddleware(gameContext)
        gameContext = setBattleListMiddleware(gameContext)
        gameContext = setGameWindowMiddleware(gameContext)
        gameContext = setDirection(gameContext)
        gameContext = setGameWindowCreatures(gameContext)
        gameContext = setHandleLoot(gameContext)
        gameContext = setWaypointIndex(gameContext)
        gameContext = setMapPlayerStatusMiddleware(gameContext)
        return gameContext

    gameObserver = fpsObserver.pipe(
        operators.map(handleGameData),
        operators.filter(lambda ctx: ctx['pause'] == False),
    )

    def handleGameplayTasks(context):
        global gameContext
        gameContext = context
        hasCurrentTask = gameContext['currentTask'] is not None
        if hasCurrentTask and gameContext['currentTask'].name != 'lureCreatures' and (gameContext['currentTask'].status == 'completed' or len(gameContext['currentTask'].tasks) == 0):
            gameContext['currentTask'] = None
        hasCreaturesToAttackInCavebot = hasCreaturesToAttack(context)
        hasCorpsesToLoot = len(gameContext['loot']['corpsesToLoot']) > 0 
        if hasCorpsesToLoot and not hasCreaturesToAttackInCavebot:
            gameContext['way'] = 'lootCorpses'
            if gameContext['currentTask'] is not None and gameContext['currentTask'].name != 'groupOfLootCorpse':
                gameContext['currentTask'] = None
            if gameContext['currentTask'] is None:
                # TODO: get closest dead corpse
                firstDeadCorpse = gameContext['loot']['corpsesToLoot'][0]
                gameContext['currentTask'] = GroupOfLootCorpseTasks(context, firstDeadCorpse)
            gameContext['gameWindow']['previousMonsters'] = gameContext['gameWindow']['monsters']
            return gameContext
        elif gameContext['currentTask'] is not None and gameContext['currentTask'].name == 'lureCreatures':
            gameContext['way'] = 'waypoint'
        elif hasCreaturesToAttackInCavebot:
            targetCreature = getClosestCreature(gameContext['gameWindow']['creatures'], gameContext['radar']['coordinate'])
            hasTargetCreature = targetCreature != None
            if hasTargetCreature:
                gameContext['way'] = 'cavebot'
            else:
                gameContext['way'] = 'waypoint'
        else:
            gameContext['way'] = 'waypoint'
        if hasCreaturesToAttack(context) and shouldAskForCavebotTasks(gameContext):
            hasCurrentTaskAfterCheck = gameContext['currentTask'] is not None
            isTryingToAttackClosestCreature = hasCurrentTaskAfterCheck and (gameContext['currentTask'].name == 'groupOfAttackClosestCreature' or gameContext['currentTask'].name == 'groupOfFollowTargetCreature')
            isNotTryingToAttackClosestCreature = not isTryingToAttackClosestCreature
            if isNotTryingToAttackClosestCreature:
                newCurrentTask = resolveCavebotTasks(context)
                hasCurrentTask2 = gameContext['currentTask'] is not None
                if hasCurrentTask2:
                    hasTargetCreature = gameContext['cavebot']['targetCreature'] is not None or gameContext['cavebot']['closestCreature'] is not None
                    if hasTargetCreature:
                        hasKeyPressed = gameContext['lastPressedKey'] is not None
                        if hasKeyPressed:
                            pyautogui.keyUp(gameContext['lastPressedKey'])
                            gameContext['lastPressedKey'] = None
                        gameContext['currentTask'] = newCurrentTask
                else:
                    hasNewCurrentTask = newCurrentTask is not None
                    if hasNewCurrentTask:
                        hasKeyPressed = gameContext['lastPressedKey'] is not None
                        if hasKeyPressed:
                            pyautogui.keyUp(gameContext['lastPressedKey'])
                            gameContext['lastPressedKey'] = None
                        gameContext['currentTask'] = newCurrentTask
        elif gameContext['way'] == 'waypoint':
            if gameContext['currentTask'] == None:
                currentWaypointIndex = gameContext['cavebot']['waypoints']['currentIndex']
                currentWaypoint = gameContext['cavebot']['waypoints']['points'][currentWaypointIndex]
                gameContext['currentTask'] = resolveTasksByWaypoint(context, currentWaypoint)
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
        if gameContext['currentTask'] is not None:
            gameContext = gameContext['currentTask'].do(context)
        gameContext['radar']['lastCoordinateVisited'] = gameContext['radar']['coordinate']

    eatFoodObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    healingByPotionsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    healingBySpellsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    comboSpellsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    
    class GameContext:
        def addWaypoint(self, waypoint):
            global gameContext
            gameContext['cavebot']['waypoints']['points'] = np.append(gameContext['cavebot']['waypoints']['points'], np.array([waypoint], dtype=Waypoint))

        def focusInTibia(self):
            global gameContext
            maximizeWindow(gameContext['window'])
            focusWindow(gameContext['window'])

        def play(self):
            self.focusInTibia()
            sleep(1)
            gameContext['pause'] = False

        def pause(self):
            gameContext['pause'] = True
            gameContext['currentTask'] = None
            if gameContext['lastPressedKey'] is not None:
                pyautogui.keyUp(gameContext['lastPressedKey'])
                gameContext['lastPressedKey'] = None

        def getCoordinate(self):
            global gameContext
            screenshot = getScreenshot()
            coordinate = getCoordinate(screenshot, previousCoordinate=gameContext['previousCoordinate'])
            return coordinate

    try:
        eatFoodObservable.subscribe(eatFoodObserver)
        healingByPotionsObservable.subscribe(healingByPotionsObserver)
        healingBySpellsObservable.subscribe(healingBySpellsObserver)
        comboSpellsObservable.subscribe(comboSpellsObserver)
        gameplayObservable.subscribe(gameplayObserver)
        kivy.context.register_context('game', GameContext)
        MyApp().run()
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()