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
import gameplay.waypoint
import hud.creatures
import hud.core
import hud.slot
import radar.core
from radar.types import waypointType
import utils.array
import utils.core
import utils.image


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


gameContext = {
    'battleListCreatures': np.array([], dtype=battleList.typing.creatureType),
    'beingAttackedCreature': None,
    'cavvebot': {'status': None},
    'comingFromDirection': None,
    'corpsesToLoot': np.array([], dtype=hud.creatures.creatureType),
    'hudCoordinate': None,
    'hudCreatures': np.array([], dtype=hud.creatures.creatureType),
    'hudImg': None,
    'lastCoordinateVisitedAt': time.time(),
    'lastCoordinateVisited': None,
    'lastPressedKey': None,
    'lastWay': 'waypoint',
    'previousRadarCoordinate': None,
    'radarCoordinate': None,
    'refill': {
        'healthItem': {
            'name': 'ultimate spirit potion',
            'quantity': 140,
        },
        'manaItem': {
            'name': 'mana potion',
            'quantity': 30,
        },
    },
    'waypoints': {
        'currentIndex': None,
        'points': np.array([
            # ('floor', (33125, 32833, 7), 0, {}),
            # ('floor', (33114, 32830, 7), 0, {}),
            # ('floor', (33098, 32830, 7), 0, {}),
            ('floor', (33098, 32793, 7), 0, {}),
            ('floor', (33088, 32788, 7), 0, {}),
            ('moveUpNorth', (33088, 32788, 7), 0, {}),
            # ('moveDown', (33088, 32785, 6), 0, {}),
            # ('floor', (33078, 32760, 7), 0, {}),
            # ('floor', (33078, 32761, 7), 0, {}),
            # ('useShovel', (33072, 32760, 7), 0, {}),
            # ('floor', (33095, 32761, 8), 0, {}),
            # ('floor', (33084, 32770, 8), 0, {}),
            # ('floor', (33062, 32762, 8), 0, {}),
            # ('refillChecker', (33073, 32758, 8), 0, {
            #     'minimumOfManaPotions': 30,
            #     'minimumOfHealthPotions': 30,
            #     'minimumOfCapacity': 200,
            # }),
            # ('useRope', (33072, 32760, 8), 0, {}),
            # ('floor', (33075, 32771, 7), 0, {}),
            # ('moveUpSouth', (33088, 32783, 7), 0, {}),
            # ('moveDownSouth', (33088, 32786, 6), 0, {}),
            # ('floor', (33098, 32793, 7), 0, {}),
            # ('floor', (33099, 32830, 7), 0, {}),
            # ('floor', (33125, 32833, 7), 0, {}),
            # ('refillChecker', (33127, 32834, 7), 0, {}),
            # ('moveUpNorth', (33128, 32827, 7), 0, {}),
            # ('moveUpNorth', (33131, 32817, 6), 0, {}),
            # ('floor', (33128, 32811, 5), 0, {}),
            # ('refill', (33128, 32810, 5), 0, {}),
            # ('moveDownSouth', (33130, 32815, 5), 0, {}),
            # ('moveDownWest', (33124, 32814, 6), 0, {}),
        ], dtype=waypointType),
        'state': None
    },
    'screenshot': None,
    'tasks': None,
    'way': None,
}
hudCreatures = np.array([], dtype=hud.creatures.creatureType)


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
        copyOfContext['radarCoordinate'] = radar.core.getCoordinate(
            copyOfContext['screenshot'], previousRadarCoordinate=copyOfContext['previousRadarCoordinate'])
        copyOfContext['previousRadarCoordinate'] = copyOfContext['radarCoordinate']
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
        operators.filter(lambda result: result['radarCoordinate'] is not None),
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
        if copyOfContext['previousRadarCoordinate'] is None:
            copyOfContext['previousRadarCoordinate'] = copyOfContext['radarCoordinate']
        coordinateDidChange = np.all(
            copyOfContext['previousRadarCoordinate'] == copyOfContext['radarCoordinate']) == False
        if coordinateDidChange:
            radarCoordinate = copyOfContext['radarCoordinate']
            if radarCoordinate[2] != copyOfContext['previousRadarCoordinate'][2]:
                comingFromDirection = None
            elif radarCoordinate[0] != copyOfContext['previousRadarCoordinate'][0] and radarCoordinate[1] != copyOfContext['previousRadarCoordinate'][1]:
                comingFromDirection = None
            elif radarCoordinate[0] != copyOfContext['previousRadarCoordinate'][0]:
                comingFromDirection = 'left' if radarCoordinate[
                    0] > copyOfContext['previousRadarCoordinate'][0] else 'right'
            elif radarCoordinate[1] != copyOfContext['previousRadarCoordinate'][1]:
                comingFromDirection = 'top' if radarCoordinate[
                    1] > copyOfContext['previousRadarCoordinate'][1] else 'bottom'
            copyOfContext['previousRadarCoordinate'] = copyOfContext['radarCoordinate']
        copyOfContext['comingFromDirection'] = comingFromDirection
        gameContext = copyOfContext
        return copyOfContext

    directionObserver = hudImgObserver.pipe(operators.map(resolveDirection))

    def resolveCreatures(context):
        global gameContext, hudCreatures
        copyOfContext = context.copy()
        hudCreatures = hud.creatures.getCreatures(
            copyOfContext['battleListCreatures'], copyOfContext['comingFromDirection'], copyOfContext['hudCoordinate'], copyOfContext['hudImg'], copyOfContext['radarCoordinate'])
        copyOfContext['hudCreatures'] = hudCreatures
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
            copyOfContext['corpsesToLoot'], copyOfContext['hudCreatures'], copyOfContext['radarCoordinate'])
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
                copyOfContext['radarCoordinate'], copyOfContext['waypoints']['points'])
        currentWaypointIndex = copyOfContext['waypoints']['currentIndex']
        nextWaypointIndex = utils.array.getNextArrayIndex(
            copyOfContext['waypoints']['points'], currentWaypointIndex)
        currentWaypoint = copyOfContext['waypoints']['points'][currentWaypointIndex]
        nextWaypoint = copyOfContext['waypoints']['points'][nextWaypointIndex]
        waypointsStateIsEmpty = copyOfContext['waypoints']['state'] == None
        if waypointsStateIsEmpty:
            copyOfContext['waypoints']['state'] = gameplay.waypoint.resolveGoalCoordinate(
                copyOfContext['radarCoordinate'], currentWaypoint)
        result = copyOfContext['radarCoordinate'] == copyOfContext['waypoints']['state']['checkInCoordinate']
        didReachWaypoint = np.all(result) == True
        # hasNoTasks = len(copyOfContext['tasks']) == 0
        if copyOfContext['tasks'] is None:
            copyOfContext['tasks'] = np.array([], dtype=np.dtype([
                ('type', np.str_, 64),
                ('data', np.object_),
            ]))
            copyOfContext['tasks'] = gameplay.resolvers.resolveTasksByWaypointType(
                copyOfContext, currentWaypoint)
        print('tasks', copyOfContext['tasks'])
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
        if didReachWaypoint:
            if len(copyOfContext['tasks']) == 0 or copyOfContext['tasks'][0]['type'] != 'check' or copyOfContext['tasks'][0]['type'] != 'refillChecker' or copyOfContext['tasks'][0]['type'] != 'refill' or copyOfContext['tasks'][0]['type'] != 'say' or copyOfContext['tasks'][0]['type'] != 'buyItem':
                copyOfContext['waypoints']['currentIndex'] = nextWaypointIndex
                copyOfContext['waypoints']['state'] = gameplay.waypoint.resolveGoalCoordinate(
                    copyOfContext['radarCoordinate'], nextWaypoint)
            else:
                print(' n fiz nada pq é check')
        gameContext = copyOfContext
        return copyOfContext

    def hasTasksToExecute(context):
        has = len(context['tasks']) > 0
        return has

    taskObserver = decisionObserver.pipe(
        operators.map(handleTasks),
        operators.filter(hasTasksToExecute),
    )

    def taskObservable(context):
        global gameContext
        copyOfContext = context.copy()
        if len(copyOfContext['tasks']) > 0:
            taskName, task = copyOfContext['tasks'][0]
            if task.status == 'notStarted':
                if task.startedAt == None:
                    task.startedAt = time.time()
                passedTimeSinceLastCheck = time.time() - task.startedAt
                shouldExecNow = passedTimeSinceLastCheck >= task.delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = task.shouldIgnore(
                        copyOfContext) == False
                    shouldNotExecTask = shouldExecResponse == False and task.status != 'running'
                    if shouldNotExecTask:
                        copyOfContext = task.onDidNotComplete(copyOfContext)
                        copyOfContext['tasks'] = np.delete(
                            copyOfContext['tasks'], 0)
                    else:
                        task.status = 'running'
                        copyOfContext = task.do(copyOfContext)
                        if len(copyOfContext['tasks']) > 0:
                            copyOfContext['tasks'][0] = task
            elif task.status == 'running':
                shouldNotRestart = not task.shouldRestart(copyOfContext)
                if shouldNotRestart:
                    didTask = task.did(copyOfContext)
                    if didTask:
                        copyOfContext = task.onDidComplete(copyOfContext)
                        task.finishedAt = time.time()
                        task.status = 'completed'
                        copyOfContext['tasks'][0] = task
            if task.status == 'completed':
                passedTimeSinceTaskCompleted = time.time() - task.finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > task.delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    copyOfContext['tasks'] = np.delete(
                        copyOfContext['tasks'], 0)
        gameContext = copyOfContext
        copyOfContext['lastCoordinateVisited'] = context['radarCoordinate']

    taskObserver.subscribe(taskObservable)

    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()
