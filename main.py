import multiprocessing
import pyautogui
from rx import interval, operators
from rx.scheduler import ThreadPoolScheduler
import time
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
from src.gameplay.healing.observers.healingBySpells import healingBySpellsObserver
from src.gameplay.healing.observers.healingByPotions import healingByPotionsObserver
from src.features.gameWindow.creatures import getClosestCreature


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    optimalThreadCount = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimalThreadCount)
    fpsCounter = 0.015625
    fpsObserver = interval(fpsCounter)
    
    def handleGameData(_):
        global gameContext
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

    gameObserver = fpsObserver.pipe(operators.map(handleGameData))

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

    gameplayObserver = gameObserver.pipe(
        operators.map(handleGameplayTasks),
        operators.subscribe_on(threadPoolScheduler),
    )

    def gameplayObservable(context):
        global gameContext
        if gameContext['currentTask'] is not None:
            gameContext = gameContext['currentTask'].do(context)
        gameContext['radar']['lastCoordinateVisited'] = gameContext['radar']['coordinate']

    healingByPotionsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    healingBySpellsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))
    comboSpellsObservable = gameObserver.pipe(operators.subscribe_on(threadPoolScheduler))

    try:
        healingByPotionsObservable.subscribe(healingByPotionsObserver)
        healingBySpellsObservable.subscribe(healingBySpellsObserver)
        comboSpellsObservable.subscribe(comboSpellsObserver)
        gameplayObserver.subscribe(gameplayObservable)
        while True:
            time.sleep(1)
            continue
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()