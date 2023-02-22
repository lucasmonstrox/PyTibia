import dxcam
import multiprocessing
import numpy as np
import pyautogui
from rx import interval, operators
from rx.scheduler import ThreadPoolScheduler
from time import sleep, time
import actionBar.core
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
import player.core
import radar.core
from radar.types import coordinateType, waypointType
import utils.array
import utils.core
import utils.image
import skills.core
import timeit
import pyautogui


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


camera = dxcam.create()
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
    'corpsesToLoot': np.array([], dtype=hud.creatures.creatureType),
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
    'monsters': np.array([], dtype=hud.creatures.creatureType),
    'players': np.array([], dtype=hud.creatures.creatureType),
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
hudCreatures = np.array([], dtype=hud.creatures.creatureType)


def main():
    # rgbScreenshot = utils.core.getScreenshot(camera)
    grayScreenshot = utils.image.loadFromRGBToGray('screenshot.png')
    # grayScreenshot = utils.image.RGBtoGray(rgbScreenshot)
    gameContext['previousCoordinate'] = radar.core.getCoordinate(grayScreenshot)
    battleListCreatures = battleList.core.getCreatures(grayScreenshot)
    hudSize = hud.core.hudSizes[gameContext['resolution']]
    hudCoordinate = hud.core.getCoordinate(grayScreenshot, hudSize)
    hudImg = hud.core.getImgByCoordinate(grayScreenshot, hudCoordinate, hudSize)
    # hudCreatures = hud.creatures.getCreatures(battleListCreatures, 'left', hudCoordinate, hudImg, gameContext['previousCoordinate'], gameContext['resolution'])
    # print('hudCreatures', hudCreatures)   

    def handle():
        global gameContext
        # handle screenshot
        rgbScreenshot = utils.core.getScreenshot(camera)
        gameContext['screenshot'] = utils.image.RGBtoGray(rgbScreenshot)
        # handle coordinate
        gameContext['coordinate'] = radar.core.getCoordinate(gameContext['screenshot'], previousCoordinate=gameContext['previousCoordinate'])
        # handle battle list
        gameContext['battleListCreatures'] = battleList.core.getCreatures(
            gameContext['screenshot'])
        hasBattleListCreatures = len(gameContext['battleListCreatures']) > 0
        gameContext['cavebot']['isAttackingSomeCreature'] = battleList.core.isAttackingSomeCreature(gameContext['battleListCreatures']) if hasBattleListCreatures else False
        # handle hud coordinate
        hudSize = hud.core.hudSizes[gameContext['resolution']]
        gameContext['hud']['coordinate'] = hud.core.getCoordinate(
            gameContext['screenshot'], hudSize)
        # handle hud image
        hudSize = hud.core.hudSizes[gameContext['resolution']]
        gameContext['hudImg'] = hud.core.getImgByCoordinate(
            gameContext['screenshot'], gameContext['hud']['coordinate'], hudSize)
        # resolve direction
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
        # handle hud creatures
        hudCreatures = hud.creatures.getCreatures(
            gameContext['battleListCreatures'], gameContext['comingFromDirection'], gameContext['hud']['coordinate'], gameContext['hudImg'], gameContext['coordinate'], gameContext['resolution'])
        gameContext['monsters'] = hud.creatures.getCreaturesByType(hudCreatures, 'monster')
        gameContext['players'] = hud.creatures.getCreaturesByType(hudCreatures, 'player')
        gameContext['cavebot']['targetCreature'] = hud.creatures.getTargetCreature(gameContext['monsters'])
        # handle loot
        if gameContext['cavebot']['targetCreature'] is not None and chat.core.hasNewLoot(gameContext['screenshot']):
            gameContext['corpsesToLoot'] = np.append(gameContext['corpsesToLoot'], [gameContext['cavebot']['targetCreature']], axis=0)
        # handle decision
        gameContext['way'] = gameplay.decision.getWay(
            gameContext['corpsesToLoot'], gameContext['monsters'], gameContext['coordinate'])
        # handle current waypoint index
        if gameContext['cavebot']['waypoints']['currentIndex'] == None:
            gameContext['cavebot']['waypoints']['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                gameContext['coordinate'], gameContext['cavebot']['waypoints']['points'])
    
    # def shouldAskForCavebotTasks(context):
    #     isNotCavebotWay = context['way'] != 'cavebot'
    #     if isNotCavebotWay:
    #         return False
    #     if context['currentTask'] is None:
    #         return True
    #     endlessTasks = ['groupOfLootCorpse', 'groupOfRefillChecker', 'groupOfSingleWalk', 'groupOfUseRope', 'groupOfUseShovel']
    #     should = (context['currentTask'].name not in endlessTasks)
    #     return should
    
    # def handleTasks(context):
    #     global gameContext
    #     gameContext = context.copy()
    #     hasCurrentTask = gameContext['currentTask'] is not None
    #     if hasCurrentTask and (gameContext['currentTask'].status == 'completed' or len(gameContext['currentTask'].tasks) == 0):
    #         gameContext['currentTask'] = None
    #     if shouldAskForCavebotTasks(context):
    #         hasCurrentTaskAfterCheck = gameContext['currentTask'] is not None
    #         isTryingToAttackClosestCreature = hasCurrentTaskAfterCheck and (gameContext['currentTask'].name == 'groupOfAttackClosestCreature' or gameContext['currentTask'].name == 'groupOfFollowTargetCreature')
    #         isNotTryingToAttackClosestCreature = not isTryingToAttackClosestCreature
    #         if isNotTryingToAttackClosestCreature:
    #             newCurrentTask = gameplay.cavebot.resolveCavebotTasks(gameContext)
    #             hasCurrentTask2 = gameContext['currentTask'] is not None
    #             if hasCurrentTask2:
    #                 hasTargetCreature = context['cavebot']['targetCreature'] is not None or context['cavebot']['closestCreature'] is not None
    #                 if hasTargetCreature:
    #                     hasKeyPressed = gameContext['lastPressedKey'] is not None
    #                     if hasKeyPressed:
    #                         pyautogui.keyUp(gameContext['lastPressedKey'])
    #                         gameContext['lastPressedKey'] = None
    #                     gameContext['currentTask'] = newCurrentTask
    #             else:
    #                 hasNewCurrentTask = newCurrentTask is not None
    #                 if hasNewCurrentTask:
    #                     hasKeyPressed = gameContext['lastPressedKey'] is not None
    #                     if hasKeyPressed:
    #                         pyautogui.keyUp(gameContext['lastPressedKey'])
    #                         gameContext['lastPressedKey'] = None
    #                     gameContext['currentTask'] = newCurrentTask
    #     elif gameContext['way'] == 'lootCorpses':
    #         if gameContext['currentTask'] is None:
    #             # TODO: get closest dead corpse
    #             firstDeadCorpse = gameContext['corpsesToLoot'][0]
    #             gameContext['currentTask'] = GroupOfLootCorpseTasks(gameContext, firstDeadCorpse)
    #     elif gameContext['way'] == 'waypoint':
    #         if gameContext['currentTask'] == None:
    #             currentWaypointIndex = gameContext['cavebot']['waypoints']['currentIndex']
    #             currentWaypoint = gameContext['cavebot']['waypoints']['points'][currentWaypointIndex]
    #             gameContext['currentTask'] = gameplay.resolvers.resolveTasksByWaypointType(gameContext, currentWaypoint)
    #     gameContext = gameContext
    #     return gameContext

    # def hasTaskToExecute(context):
    #     has = context['currentTask'] is not None
    #     return has

    # taskObserver = decisionObserver.pipe(
    #     operators.map(handleTasks),
    #     operators.filter(hasTaskToExecute),
    #     operators.subscribe_on(threadPoolScheduler),
    # )

    # def taskObservable(context):
    #     global gameContext
    #     gameContext = context.copy()
    #     gameContext = context['currentTask'].exec(gameContext)
    #     gameContext['lastCoordinateVisited'] = context['coordinate']
    #     gameContext = gameContext
    # res = timeit.repeat(lambda: hud.creatures.getCreaturesByType(hudCreatures, 'monster'), repeat=10, number=1)
    # print('res', res)
    # res = timeit.repeat(lambda: hud.creatures.getCreaturesBars(hudImg, len(battleListCreatures)), repeat=10, number=1)
    # print('res', res)
    # res = timeit.repeat(lambda: hud.creatures.getCreatures(battleListCreatures, 'left', hudCoordinate, hudImg, gameContext['previousCoordinate'], gameContext['resolution']), repeat=10, number=1)
    # res = timeit.repeat(lambda: pyautogui.press('w'), repeat=10, number=1)
    # hudImg = utils.image.loadFromRGBToGray('hudImg.png')
    utils.image.save(hudImg, 'hudImg.png')
    bars = hud.creatures.getCreaturesBars(hudImg)
    print(bars, len(bars))
    # hudCreatures = hud.creatures.getCreatures(battleListCreatures, 'left', hudCoordinate, hudImg, gameContext['previousCoordinate'], gameContext['resolution'])
    # print(bars, len(bars))
    # hudCreatures = hud.creatures.getCreatures(battleListCreatures, 'left', hudCoordinate, hudImg, gameContext['previousCoordinate'], gameContext['resolution'])
    # print(bars, len(bars))
    # print('hudCreatures', hudCreatures)
    # res = timeit.repeat(lambda: hud.creatures.getCreaturesBars(hudImg), repeat=10, number=1)
    # print('res', res)
    # res = timeit.repeat(lambda: handle(), repeat=10, number=1)
    # print('res', res)


if __name__ == '__main__':
    main()
