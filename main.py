import multiprocessing
import numpy as np
import pyautogui
from rx import interval, of, operators, pipe, timer
from rx.scheduler import ThreadPoolScheduler
from rx.subject import Subject
import time
import battleList.core
import battleList.typing
from chat import core
import gameplay.cavebot
import gameplay.decision
import gameplay.resolvers
import gameplay.typings
import gameplay.waypoint
import hud.creatures
import hud.core
import hud.slot
import radar.core
from radar.types import waypointType
from gameplay.taskExecutor import TaskExecutor
import utils.array
import utils.core
import utils.image


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


gameContext = {
    'backpacks': {
        'main': 'brocade backpack',
        'gold': 'beach backpack',
        'loot': 'fur backpack',
    },
    'battleListCreatures': np.array([], dtype=battleList.typing.creatureType),
    'beingAttackedCreature': None,
    'cavebot': {'status': None},
    'comingFromDirection': None,
    'corpsesToLoot': np.array([], dtype=hud.creatures.creatureType),
    'currentGroupTask': None,
    'hudCoordinate': None,
    'hudImg': None,
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
    'waypoints': {
        'currentIndex': None,
        'points': np.array([
            # yalahar
            ('walk', (32741, 31294, 11), 0, {}),
            ('walk', (32704, 31270, 11), 0, {}),
            ('walk', (32685, 31286, 11), 0, {}),
            ('walk', (32713, 31305, 11), 0, {}),
            ('walk', (32741, 31295, 11), 0, {}),
            # verificar se tem items pra depositar
            # ('walk', (33127, 32830, 7), 0, {}),
            # ('walk', (33126, 32834, 7), 0, {}),
            # ('depositItems', (33126, 32841, 7), 0, {}),
            # verificar se tem dinheiro pra depositar
            # verificar se precisa de comprar potions
            # ('walk', (33125, 32833, 7), 0, {}),
            # ('walk', (33114, 32830, 7), 0, {}),
            # ('walk', (33098, 32830, 7), 0, {}),
            # ('walk', (33098, 32793, 7), 0, {}),
            # ('walk', (33088, 32788, 7), 0, {}),
            # ('moveUpNorth', (33088, 32788, 7), 0, {}),
            # ('walk', (33088, 32785, 6), 0, {}),
            # ('moveDownNorth', (33088, 32785, 6), 0, {}),
            # ('walk', (33073, 32760, 7), 0, {}),
            # ('useShovel', (33072, 32760, 7), 0, {}),
            # ('walk', (33095, 32761, 8), 0, {}),
            # ('walk', (33084, 32770, 8), 0, {}),
            # ('walk', (33062, 32762, 8), 0, {}),
            # ('walk', (33072, 32760, 8), 0, {}),
            # ('walk', (33076, 32757, 8), 0, {}),
            # ('walk', (33072, 32759, 8), 0, {}),
            # ('refillChecker', (33072, 32760, 8), 0, {
            #     'minimumOfManaPotions': 100,
            #     'minimumOfHealthPotions': 100,
            #     'minimumOfCapacity': 200,
            #     'successIndex': 12,
            # }),
            # ('walk', (33072, 32760, 8), 0, {}),
            # ('useRope', (33072, 32760, 8), 0, {}),
            # ('walk', (33088, 32783, 7), 0, {}),
            # ('moveUpSouth', (33088, 32783, 7), 0, {}),
            # ('walk', (33088, 32786, 6), 0, {}),
            # ('moveDownSouth', (33088, 32786, 6), 0, {}),
            # ('walk', (33098, 32793, 7), 0, {}),
            # ('walk', (33099, 32830, 7), 0, {}),
            # ('walk', (33125, 32833, 7), 0, {}),

            # ('walk', (33126, 32834, 7), 0, {}),
            # ('depositItems', (33126, 32834, 7), 0, {}),

            # ('refillChecker', (33127, 32834, 7), 0, {}),
            # ('walk', (33128, 32827, 7), 0, {}),
            # ('moveUpNorth', (33128, 32827, 7), 0, {}),
            # ('walk', (33130, 32817, 6), 0, {}),
            # ('moveUpNorth', (33130, 32817, 6), 0, {}),
            # ('walk', (33128, 32811, 5), 0, {}),
            # ('refill', (33128, 32810, 5), 0, {}),
            # ('walk', (33130, 32815, 5), 0, {}),
            # ('moveDownSouth', (33130, 32815, 5), 0, {}),
            # ('walk', (33124, 32814, 6), 0, {}),
            # ('moveDownWest', (33124, 32814, 6), 0, {}),
        ], dtype=waypointType),
        'state': None
    },
    'screenshot': None,
    # 'tasks': np.array([], dtype=gameplay.typings.taskType),
    'way': None,
}
hudCreatures = np.array([], dtype=hud.creatures.creatureType)
taskExecutor = TaskExecutor()


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    thirteenFps = 0.00833333333
    fpsObserver = interval(thirteenFps)

    def handleScreenshot(_):
        global gameContext
        copyOfContext = gameContext.copy()
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        copyOfContext['screenshot'] = screenshot
        gameContext = copyOfContext
        return copyOfContext

    fpsWithScreenshot = fpsObserver.pipe(
        operators.map(handleScreenshot),
    )

    def handleCoordinate(context):
        global gameContext
        copyOfContext = context.copy()
        copyOfContext['coordinate'] = radar.core.getCoordinate(
            copyOfContext['screenshot'], previousCoordinate=copyOfContext['previousCoordinate'])
        copyOfContext['previousCoordinate'] = copyOfContext['coordinate']
        gameContext = copyOfContext
        return copyOfContext

    coordinatesObserver = fpsWithScreenshot.pipe(
        operators.filter(lambda result: result['screenshot'] is not None),
        operators.map(handleCoordinate)
    )

    def handleBattleListCreatures(context):
        global gameContext
        copyOfContext = context.copy()
        copyOfContext['battleListCreatures'] = battleList.core.getCreatures(
            copyOfContext['screenshot'])
        gameContext = copyOfContext
        return copyOfContext

    battleListObserver = coordinatesObserver.pipe(
        operators.map(handleBattleListCreatures)
    )

    def handleHudCoordinate(context):
        global gameContext
        copyOfContext = context.copy()
        copyOfContext['hudCoordinate'] = hud.core.getCoordinate(
            copyOfContext['screenshot'])
        gameContext = copyOfContext
        return copyOfContext

    hudCoordinateObserver = battleListObserver.pipe(
        operators.filter(lambda result: result['coordinate'] is not None),
        operators.map(handleHudCoordinate)
    )

    def handleHudImg(context):
        global gameContext
        copyOfContext = context.copy()
        copyOfContext['hudImg'] = hud.core.getImgByCoordinate(
            copyOfContext['screenshot'], copyOfContext['hudCoordinate'])
        gameContext = copyOfContext
        return copyOfContext

    hudImgObserver = hudCoordinateObserver.pipe(
        operators.map(handleHudImg)
    )

    def resolveDirection(context):
        global gameContext
        copyOfContext = context.copy()
        comingFromDirection = None
        if copyOfContext['previousCoordinate'] is None:
            copyOfContext['previousCoordinate'] = copyOfContext['coordinate']
        coordinateDidChange = np.all(
            copyOfContext['previousCoordinate'] == copyOfContext['coordinate']) == False
        if coordinateDidChange:
            coordinate = copyOfContext['coordinate']
            if coordinate[2] != copyOfContext['previousCoordinate'][2]:
                comingFromDirection = None
            elif coordinate[0] != copyOfContext['previousCoordinate'][0] and coordinate[1] != copyOfContext['previousCoordinate'][1]:
                comingFromDirection = None
            elif coordinate[0] != copyOfContext['previousCoordinate'][0]:
                comingFromDirection = 'left' if coordinate[
                    0] > copyOfContext['previousCoordinate'][0] else 'right'
            elif coordinate[1] != copyOfContext['previousCoordinate'][1]:
                comingFromDirection = 'top' if coordinate[
                    1] > copyOfContext['previousCoordinate'][1] else 'bottom'
            copyOfContext['previousCoordinate'] = copyOfContext['coordinate']
        copyOfContext['comingFromDirection'] = comingFromDirection
        gameContext = copyOfContext
        return copyOfContext

    directionObserver = hudImgObserver.pipe(operators.map(resolveDirection))

    def resolveCreatures(context):
        global gameContext, hudCreatures
        copyOfContext = context.copy()
        hudCreatures = hud.creatures.getCreatures(
            copyOfContext['battleListCreatures'], copyOfContext['comingFromDirection'], copyOfContext['hudCoordinate'], copyOfContext['hudImg'], copyOfContext['coordinate'])
        monsters = hud.creatures.getCreatureByType(hudCreatures, 'monster')
        players = hud.creatures.getCreatureByType(hudCreatures, 'player')
        copyOfContext['monsters'] = monsters
        copyOfContext['players'] = players
        gameContext = copyOfContext
        return copyOfContext

    hudCreaturesObserver = directionObserver.pipe(
        operators.map(resolveCreatures))

    def handleLoot(context):
        global gameContext
        copyOfContext = context.copy()
        corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
        beingAttackedIndexes = np.where(
            hudCreatures['isBeingAttacked'] == True)[0]
        hasCreatureBeingAttacked = len(beingAttackedIndexes) > 0
        if core.hasNewLoot(copyOfContext['screenshot']) and copyOfContext['beingAttackedCreature']:
            corpsesToLoot = np.append(copyOfContext['corpsesToLoot'], [
                                      copyOfContext['beingAttackedCreature']], axis=0)
        beingAttackedCreature = None
        if hasCreatureBeingAttacked:
            beingAttackedCreature = hudCreatures[beingAttackedIndexes[0]]
        copyOfContext['beingAttackedCreature'] = beingAttackedCreature
        copyOfContext['corpsesToLoot'] = corpsesToLoot
        gameContext = copyOfContext
        return copyOfContext

    lootObserver = hudCreaturesObserver.pipe(operators.map(handleLoot))

    def handleDecision(context):
        global gameContext
        copyOfContext = context.copy()
        copyOfContext['way'] = gameplay.decision.getWay(
            copyOfContext['corpsesToLoot'], copyOfContext['monsters'], copyOfContext['coordinate'])
        gameContext = copyOfContext
        return copyOfContext

    decisionObserver = lootObserver.pipe(
        operators.map(handleDecision)
    )

    def handleTasks(context):
        global gameContext
        copyOfContext = context.copy()
        if copyOfContext['waypoints']['currentIndex'] == None:
            copyOfContext['waypoints']['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                copyOfContext['coordinate'], copyOfContext['waypoints']['points'])
        currentWaypointIndex = copyOfContext['waypoints']['currentIndex']
        print('handleTasks.currentWaypointIndex', currentWaypointIndex)
        nextWaypointIndex = utils.array.getNextArrayIndex(
            copyOfContext['waypoints']['points'], currentWaypointIndex)
        print('handleTasks.nextWaypointIndex', nextWaypointIndex)
        currentWaypoint = copyOfContext['waypoints']['points'][currentWaypointIndex]
        nextWaypoint = copyOfContext['waypoints']['points'][nextWaypointIndex]
        waypointsStateIsEmpty = copyOfContext['waypoints']['state'] == None
        if waypointsStateIsEmpty:
            copyOfContext['waypoints']['state'] = gameplay.waypoint.resolveGoalCoordinate(
                copyOfContext['coordinate'], currentWaypoint)
        result = copyOfContext['coordinate'] == copyOfContext['waypoints']['state']['checkInCoordinate']
        didReachWaypoint = np.all(result) == True
        if copyOfContext['currentGroupTask'] == None:
            copyOfContext['currentGroupTask'] = gameplay.resolvers.resolveTasksByWaypointType(
                copyOfContext, currentWaypoint)
        if copyOfContext['way'] == 'cavebot':
            isTryingToAttackClosestCreature = len(
                copyOfContext['tasks']) > 0 and copyOfContext['tasks'][0]['type'] == 'attackClosestCreature'
            if isTryingToAttackClosestCreature:
                print('to tentando atacar')
            else:
                tasks = gameplay.cavebot.resolveCavebotTasks(copyOfContext)
                if tasks is not None:
                    if copyOfContext['lastPressedKey'] is not None:
                        pyautogui.keyUp(copyOfContext['lastPressedKey'])
                        copyOfContext['lastPressedKey'] = None
                    copyOfContext['tasks'] = tasks
        if copyOfContext['currentGroupTask']:
            print('nome da task é', copyOfContext['currentGroupTask'].name)
            print(copyOfContext['currentGroupTask'].tasks)
        if didReachWaypoint:
            allowedTasks = np.array(
                ['groupOfDepositItems', 'groupOfRefill', 'groupOfRefillChecker', 'groupOfUseShovel'])
            if copyOfContext['currentGroupTask'] == None or np.any(copyOfContext['currentGroupTask'].name == allowedTasks) == False:
                # print('chegou no waypoint e vamo embora')
                copyOfContext['waypoints']['currentIndex'] = nextWaypointIndex
                copyOfContext['waypoints']['state'] = gameplay.waypoint.resolveGoalCoordinate(
                    copyOfContext['coordinate'], nextWaypoint)
                # print('currentIndex',
                #       copyOfContext['waypoints']['currentIndex'])
        gameContext = copyOfContext
        return copyOfContext

    def hasTaskToExecute(context):
        has = context['currentGroupTask'] is not None
        return has

    taskObserver = decisionObserver.pipe(
        operators.map(handleTasks),
        operators.filter(hasTaskToExecute),
    )

    def taskObservable(context):
        global gameContext, taskExecutor
        copyOfContext = context.copy()
        copyOfContext = taskExecutor.exec(copyOfContext)
        copyOfContext['lastCoordinateVisited'] = context['coordinate']
        gameContext = copyOfContext

    taskObserver.subscribe(taskObservable)

    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()

# abrir bp principal
# abrir bp que está setada para loot
# se houver loots
# -- abrir depot
# -- abrir chest setado para itens
# -- arrastar item a item para o chest e paginar nas backpacks
