import dxcam
import multiprocessing
import numpy as np
import pyautogui
from rx import interval, operators
from rx.scheduler import ThreadPoolScheduler
from time import sleep
import battleList.core
import battleList.typing
import chat.core
import gameplay.cavebot
import gameplay.decision
from gameplay.tasks.groupOfLootCorpse import GroupOfLootCorpseTasks
import gameplay.resolvers
import gameplay.typings
import gameplay.waypoint
import hud.core
import hud.creatures
import hud.slot
import hud.typing
import player.core
import radar.core
from radar.types import coordinateType, waypointType
import utils.array
import utils.core
import utils.image
import skills.core


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


camera = dxcam.create(output_color='GRAY')
gameContext = {
    'backpacks': {
        'main': 'brocade backpack',
        'gold': 'beach backpack',
        'loot': 'fur backpack',
    },
    'battleListCreatures': np.array([], dtype=battleList.typing.creatureType),
    'cavebot': {
        'holesOrStairs': np.array([
            (33306, 32284, 5),
            (33306, 32284, 6),
            (33309, 32284, 6),
            (33312, 32281, 7),
            (33309, 32284, 7),
            (33312, 32281, 8),
            (33300, 32290, 8),
        ], dtype=coordinateType),
        'isAttackingSomeCreature': False,
        'running': True,
        'targetCreature': None,
        'waypoints': {
            'currentIndex': None,
            'points': np.array([
                ('', 'walk', (33214, 32459, 8), {}),
                ('', 'walk', (33214, 32456, 8), {}),
                ('', 'moveUpNorth', (33214, 32456, 8), {}),
                ('', 'walk', (33214, 32450, 7), {}),  #indo para cave
                ('', 'walk', (33220, 32428, 7), {}),
                ('', 'walk', (33216, 32392, 7), {}),
                ('', 'walk', (33251, 32364, 7), {}),
                ('', 'walk', (33277, 32329, 7), {}),
                ('', 'walk', (33301, 32291, 7), {}),
                ('', 'walk', (33302, 32289, 7), {}), # chegou na cave
                ('caveStart', 'walk', (33301, 32278, 7), {}), # 10
                ('', 'walk', (33312, 32278, 7), {}), # 11
                ('', 'walk', (33318, 32283, 7), {}), # 12
                ('', 'walk', (33312, 32280, 7), {}), # 13
                ('', 'moveDownSouth', (33312, 32280, 7), {}), # 14
                ('', 'walk', (33302, 32283, 8), {}), # 15
                ('', 'walk', (33300, 32289, 8), {}), # 16
                ('', 'moveDownSouth', (33300, 32289, 8), {}), # 17
                ('', 'walk', (33302, 32281, 9), {}), # 18
                ('', 'walk', (33312, 32280, 9), {}), # 19
                ('', 'walk', (33312, 32289, 9), {}), # 20
                ('', 'walk', (33300, 32291, 9), {}), # 21
                ('', 'moveUpNorth', (33300, 32291, 9), {}), # 22
                ('', 'walk', (33302, 32283, 8), {}), # 23
                ('', 'walk', (33312, 32282, 8), {}), # 24
                ('', 'moveUpNorth', (33312, 32282, 8), {}), # 25
                ('', 'walk', (33311, 32285, 7), {}), # 26
                ('', 'walk', (33309, 32285, 7), {}), # 27
                ('', 'moveUpNorth', (33309, 32285, 7), {}), # 28
                ('', 'walk', (33310, 32278, 6), {}), # 29
                ('', 'walk', (33309, 32283, 6), {}), # 30
                ('', 'moveDownSouth', (33309, 32283, 6), {}), # 31
                ('', 'walk', (33305, 32289, 7), {}), # 32
                ('', 'refillChecker', (33306, 32289, 7), { # 33
                    'minimumOfManaPotions': 1,
                    'minimumOfHealthPotions': 1,
                    'minimumOfCapacity': 200,
                    'waypointLabelToRedirect': 'caveStart',
                }),
                ('', 'walk', (33264,32321,7), {}), # 31
            ], dtype=waypointType),
            'state': None
        },
    },
    'comingFromDirection': None,
    'corpsesToLoot': np.array([], dtype=hud.typing.creatureType),
    'currentTask': None,
    'healing': {
        'minimumToBeHealedUsingPotion': 60,
        'minimumToBeHealedUsingSpell': 85,
        'cureSpell': 'exura med ico',
    },
    'hotkeys': {
        'eatFood': 'f7',
        'healthPotion': 'f1',
        'manaPotion': 'f2',
        'cure': 'f3',
        'rope': 'f8',
        'shovel': 'f9',
    },
    'hud': {
        'coordinate': None,
        'img': None,
    },
    'lastCoordinateVisited': None,
    'lastPressedKey': None,
    'lastWay': 'waypoint',
    'monsters': np.array([], dtype=hud.typing.creatureType),
    'players': np.array([], dtype=hud.typing.creatureType),
    'previousCoordinate': None,
    'coordinate': None,
    'refill': {
        'health': {
            'item': 'health potion',
            'quantity': 140,
        },
        'mana': {
            'item': 'mana potion',
            'quantity': 30,
        },
    },
    'resolution': 1080,
    'targetCreature': None,
    'screenshot': None,
    'way': None,
    'window': None
}
hudCreatures = np.array([], dtype=hud.typing.creatureType)


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    fpsCounter = 0.01666666666 # 60 fps
    fpsObserver = interval(fpsCounter)

    def handleScreenshot(_):
        global gameContext
        gameContext['screenshot'] = utils.core.getScreenshot(camera)
        return gameContext

    fpsWithScreenshot = fpsObserver.pipe(
        operators.map(handleScreenshot),
    )

    def handleCoordinate(context):
        global gameContext
        gameContext = context
        gameContext['coordinate'] = radar.core.getCoordinate(
            gameContext['screenshot'], previousCoordinate=gameContext['previousCoordinate'])
        gameContext['previousCoordinate'] = gameContext['coordinate']
        return gameContext

    coordinatesObserver = fpsWithScreenshot.pipe(
        operators.filter(lambda result: result['screenshot'] is not None),
        operators.filter(
            lambda _: gameContext['cavebot']['running'] == True),
        operators.map(handleCoordinate)
    )

    def handleBattleListCreatures(context):
        global gameContext
        gameContext = context
        gameContext['battleListCreatures'] = battleList.core.getCreatures(
            gameContext['screenshot'])
        hasBattleListCreatures = len(gameContext['battleListCreatures']) > 0
        gameContext['cavebot']['isAttackingSomeCreature'] = battleList.core.isAttackingSomeCreature(gameContext['battleListCreatures']) if hasBattleListCreatures else False
        return gameContext

    battleListObserver = coordinatesObserver.pipe(
        operators.map(handleBattleListCreatures)
    )

    def handleHudCoordinate(context):
        global gameContext
        gameContext = context
        hudSize = hud.core.hudSizes[gameContext['resolution']]
        gameContext['hud']['coordinate'] = hud.core.getCoordinate(
            gameContext['screenshot'], hudSize)
        return gameContext

    hudCoordinateObserver = battleListObserver.pipe(
        operators.filter(lambda result: result['coordinate'] is not None),
        operators.map(handleHudCoordinate)
    )

    def handleHudImg(context):
        global gameContext
        gameContext = context
        hudSize = hud.core.hudSizes[gameContext['resolution']]
        gameContext['hudImg'] = hud.core.getImgByCoordinate(
            gameContext['screenshot'], gameContext['hud']['coordinate'], hudSize)
        return gameContext

    hudImgObserver = hudCoordinateObserver.pipe(
        operators.map(handleHudImg)
    )

    def resolveDirection(context):
        global gameContext
        gameContext = context
        comingFromDirection = None
        if gameContext['previousCoordinate'] is None:
            gameContext['previousCoordinate'] = gameContext['coordinate']
        coordinateDidChange = np.all(
            gameContext['previousCoordinate'] == gameContext['coordinate']) == False
        if coordinateDidChange:
            coordinate = gameContext['coordinate']
            if coordinate[2] != gameContext['previousCoordinate'][2]:
                comingFromDirection = None
            elif coordinate[0] != gameContext['previousCoordinate'][0] and coordinate[1] != gameContext['previousCoordinate'][1]:
                comingFromDirection = None
            elif coordinate[0] != gameContext['previousCoordinate'][0]:
                comingFromDirection = 'left' if coordinate[
                    0] > gameContext['previousCoordinate'][0] else 'right'
            elif coordinate[1] != gameContext['previousCoordinate'][1]:
                comingFromDirection = 'top' if coordinate[
                    1] > gameContext['previousCoordinate'][1] else 'bottom'
            gameContext['previousCoordinate'] = gameContext['coordinate']
        gameContext['comingFromDirection'] = comingFromDirection
        return gameContext

    directionObserver = hudImgObserver.pipe(operators.map(resolveDirection))

    def resolveCreatures(context):
        global gameContext, hudCreatures
        gameContext = context
        hudCreatures = hud.creatures.getCreatures(
            gameContext['battleListCreatures'], gameContext['comingFromDirection'], gameContext['hud']['coordinate'], gameContext['hudImg'], gameContext['coordinate'])
        hudCreaturesCount = len(hudCreatures)
        hasNoHudCreatures = hudCreaturesCount == 0
        gameContext['monsters'] = np.array([], dtype=hud.typing.creatureType) if hasNoHudCreatures else hud.creatures.getCreaturesByType(hudCreatures, 'monster')
        gameContext['players'] = np.array([], dtype=hud.typing.creatureType) if hasNoHudCreatures else hud.creatures.getCreaturesByType(hudCreatures, 'player')
        gameContext['cavebot']['targetCreature'] = hud.creatures.getTargetCreature(gameContext['monsters'])
        return gameContext

    hudCreaturesObserver = directionObserver.pipe(operators.map(resolveCreatures))

    def handleLoot(context):
        if gameContext['cavebot']['targetCreature'] is not None and chat.core.hasNewLoot(gameContext['screenshot']):
            gameContext['corpsesToLoot'] = np.append(gameContext['corpsesToLoot'], [gameContext['cavebot']['targetCreature']], axis=0)
        return gameContext

    lootObserver = hudCreaturesObserver.pipe(operators.map(handleLoot))

    def mapDecision(context):
        global gameContext
        gameContext = context
        gameContext['way'] = gameplay.decision.getWay(
            gameContext['corpsesToLoot'], gameContext['monsters'], gameContext['coordinate'])
        return gameContext

    def mapCurrentWaypointIndex(context):
        if gameContext['cavebot']['waypoints']['currentIndex'] == None:
            gameContext['cavebot']['waypoints']['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                gameContext['coordinate'], gameContext['cavebot']['waypoints']['points'])
        return gameContext

    decisionObserver = lootObserver.pipe(
        operators.map(mapDecision),
        operators.map(mapCurrentWaypointIndex),
    )
    
    def shouldAskForCavebotTasks(context):
        isNotCavebotWay = context['way'] != 'cavebot'
        if isNotCavebotWay:
            return False
        if context['currentTask'] is None:
            return True
        endlessTasks = ['groupOfLootCorpse', 'groupOfRefillChecker', 'groupOfSingleWalk', 'groupOfUseRope', 'groupOfUseShovel']
        should = (context['currentTask'].name not in endlessTasks)
        return should
    
    def handleTasks(context):
        global gameContext
        gameContext = context
        hasCurrentTask = gameContext['currentTask'] is not None
        if hasCurrentTask and (gameContext['currentTask'].status == 'completed' or len(gameContext['currentTask'].tasks) == 0):
            gameContext['currentTask'] = None
        if shouldAskForCavebotTasks(gameContext):
            hasCurrentTaskAfterCheck = gameContext['currentTask'] is not None
            isTryingToAttackClosestCreature = hasCurrentTaskAfterCheck and (gameContext['currentTask'].name == 'groupOfAttackClosestCreature' or gameContext['currentTask'].name == 'groupOfFollowTargetCreature')
            isNotTryingToAttackClosestCreature = not isTryingToAttackClosestCreature
            if isNotTryingToAttackClosestCreature:
                newCurrentTask = gameplay.cavebot.resolveCavebotTasks(context)
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
        elif gameContext['way'] == 'lootCorpses':
            if gameContext['currentTask'] is None:
                # TODO: get closest dead corpse
                firstDeadCorpse = gameContext['corpsesToLoot'][0]
                gameContext['currentTask'] = GroupOfLootCorpseTasks(context, firstDeadCorpse)
        elif gameContext['way'] == 'waypoint':
            if gameContext['currentTask'] == None:
                currentWaypointIndex = gameContext['cavebot']['waypoints']['currentIndex']
                currentWaypoint = gameContext['cavebot']['waypoints']['points'][currentWaypointIndex]
                gameContext['currentTask'] = gameplay.resolvers.resolveTasksByWaypointType(context, currentWaypoint)
        return gameContext

    def hasTaskToExecute(context):
        has = gameContext['currentTask'] is not None
        return has

    taskObserver = decisionObserver.pipe(
        operators.map(handleTasks),
        operators.filter(hasTaskToExecute),
        operators.subscribe_on(threadPoolScheduler),
    )

    def taskObservable(context):
        global gameContext
        gameContext = context
        gameContext = gameContext['currentTask'].exec(context)
        gameContext['lastCoordinateVisited'] = gameContext['coordinate']
        
    healingObserver = fpsWithScreenshot.pipe(
        operators.subscribe_on(threadPoolScheduler)
    )

    def healingObservable(context):
        gameContext = context
        cures = {
            'exura infir ico': 10,
            'exura ico': 40,
            'exura med ico': 90,
            'exura gran ico': 200,
            'utura': 40,
            'utura gran': 165,
        }
        hp = player.core.getHealthPercentage(gameContext['screenshot'])
        couldntGetHp = hp is None
        if couldntGetHp:
            return
        mana = player.core.getManaPercentage(gameContext['screenshot'])
        couldntGetMana = mana is None
        if couldntGetMana:
            return
        shouldHealUsingPotion = gameContext['healing']['minimumToBeHealedUsingPotion'] >= hp
        if shouldHealUsingPotion:
            pyautogui.press(gameContext['hotkeys']['healthPotion'])
            sleep(0.25)
            return
        shouldHealUsingSpell = gameContext['healing']['minimumToBeHealedUsingSpell'] >= hp
        if shouldHealUsingSpell:
            hasEnoughMana = mana >= cures[gameContext['healing']['cureSpell']]
            if hasEnoughMana:
                pyautogui.press(gameContext['hotkeys']['cure'])
                sleep(0.25)

    spellObserver = fpsWithScreenshot.pipe(
        operators.subscribe_on(threadPoolScheduler)
    )
    
    def spellObservable(context):
        global hudCreatures
        mana = skills.core.getMana(gameContext['screenshot'])
        couldntGetMana = mana is None
        if couldntGetMana:
            return
        canHaste = not player.core.hasSpecialCondition(gameContext['screenshot'], 'haste')
        if mana > 60 and canHaste:
            pyautogui.press('f6')

    try:
        spellObserver.subscribe(spellObservable)
        healingObserver.subscribe(healingObservable)
        taskObserver.subscribe(taskObservable)
        while True:
            sleep(1)
            continue
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()
