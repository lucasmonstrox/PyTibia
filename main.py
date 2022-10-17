import multiprocessing
import numpy as np
import pyautogui
from rx import interval, of, operators, pipe, timer
from rx.scheduler import ThreadPoolScheduler
from rx.subject import Subject
from scipy.spatial import distance
import time
from typing import cast
import battleList.core
import battleList.typing
from chat import chat
import gameplay.cavebot
import gameplay.decision
import gameplay.tasks
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
    'lastWay': 'waypoint',
    'previousRadarCoordinate': None,
    'radarCoordinate': None,
    'walkpoints': {
        'lastCoordinateVisitedAt': time.time(),
        'lastCoordinateVisited': None,
        'lastPressedKey': None,
        'points': np.array([]),
    },
    'waypoints': {
        'currentIndex': 0,
        'points': np.array([
            # ('floor', (33121, 32837, 7), 0),
            # ('floor', (33125, 32835, 7), 0),
            # ('floor', (33125, 32833, 7), 0),
            # ('floor', (33114, 32830, 7), 0),
            # ('floor', (33098, 32830, 7), 0),
            # ('floor', (33098, 32793, 7), 0),
            # ('floor', (33088, 32788, 7), 0),
            # ('moveUp', (33088, 32786, 6), 0),
            # ('floor', (33088, 32785, 6), 0),
            # ('moveDown', (33088, 32783, 7), 0),
            # ('floor', (33078, 32760, 7), 0),
            # ('shovel', (33072, 32760, 7), 0),
            # ('floor', (33072, 32760, 8), 0),
            # ('floor', (33072, 32759, 8), 0),
            # ('floor', (33096, 32762, 8), 0),
            # ('floor', (33067, 32748, 8), 0),
            # ('floor', (33085, 32775, 8), 0),
            # ('floor', (33062, 32788, 8), 0),
            # ('floor', (33079, 32764, 7), 0),
            ('floor', (33078, 32760, 7), 0),
            ('shovel', (33072, 32760, 7), 0),
        ], dtype=waypointType),
        'state': None
    },
    'screenshot': None,
    'tasks': [],
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
        if chat.hasNewLoot(copyOfContext['screenshot']) and copyOfContext['beingAttackedCreature']:
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

    def waypointObservable(context):
        global gameContext
        copyOfContext = context.copy()
        if copyOfContext['waypoints']['currentIndex'] == None:
            copyOfContext['waypoints']['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                copyOfContext['radarCoordinate'], copyOfContext['waypoints']['points'])
        if copyOfContext['way'] == 'lootCorpses':
            walkpoints = gameplay.waypoint.generateFloorWalkpoints(
                copyOfContext['radarCoordinate'], copyOfContext['corpsesToLoot'][0]['radarCoordinate'])
            if len(walkpoints) > 1:
                walkpoints = np.delete(walkpoints, -1, axis=0)
            copyOfContext['walkpoints']['points'] = walkpoints
            if len(copyOfContext['walkpoints']['points']) == 0:
                time.sleep(1)
                slot = hud.core.getSlotFromCoordinate(
                    copyOfContext['radarCoordinate'], copyOfContext['corpsesToLoot'][0]['radarCoordinate'])
                pyautogui.keyDown('shift')
                time.sleep(0.1)
                hud.slot.rightClickSlot(slot, copyOfContext['hudCoordinate'])
                time.sleep(0.1)
                pyautogui.keyUp('shift')
                copyOfContext['corpsesToLoot'] = np.delete(
                    copyOfContext['corpsesToLoot'], 0)
        if copyOfContext['way'] == 'cavebot':
            cavebot, walkpoints = gameplay.cavebot.handleCavebot(
                copyOfContext['battleListCreatures'],
                copyOfContext['cavebot'],
                copyOfContext['hudCreatures'],
                copyOfContext['radarCoordinate'],
                copyOfContext['walkpoints']
            )
            copyOfContext['cavebot'] = cavebot
            copyOfContext['walkpoints'] = walkpoints
        else:
            if copyOfContext['lastWay'] == 'cavebot':
                copyOfContext['walkpoints']['lastCoordinateVisited'] = None
                copyOfContext['walkpoints']['points'] = np.array([])
                copyOfContext['walkpoints']['state'] = None
            copyOfContext['waypoints'] = gameplay.waypoint.handleWaypoint(
                copyOfContext['screenshot'],
                copyOfContext['radarCoordinate'],
                copyOfContext['waypoints'],
            )
            walkpoints = gameplay.waypoint.handleWalkpoints(
                copyOfContext['radarCoordinate'],
                copyOfContext['walkpoints'],
                copyOfContext['waypoints']
            )
        copyOfContext['walkpoints'] = gameplay.waypoint.walk(
            copyOfContext['radarCoordinate'],
            copyOfContext['walkpoints']
        )
        copyOfContext['lastWay'] = copyOfContext['way']
        gameContext = copyOfContext

    decisionObserver.subscribe(waypointObservable)

    def handleTasks(context):
        global gameContext
        copyOfContext = context.copy()
        copiedWaypoints = copyOfContext['waypoints'].copy()
        hasNoTasks = len(copyOfContext['tasks']) == 0
        if hasNoTasks:
            if copyOfContext['way'] == 'waypoint':
                nextWaypointIndex = utils.array.getNextArrayIndex(
                    copiedWaypoints['points'], copyOfContext['waypoints']['currentIndex'])
                nextWaypoint = copyOfContext['waypoints']['points'][nextWaypointIndex]
                if nextWaypoint['type'] == 'floor':
                    floorTasks = gameplay.tasks.makeFloorTasks(
                        copyOfContext, nextWaypoint)
                    for floorTask in floorTasks:
                        copyOfContext['tasks'].append(floorTask)
                elif nextWaypoint['type'] == 'shovel':
                    shovelTasks = gameplay.tasks.makeUseShovelTasks(
                        copyOfContext, nextWaypoint)
                    for shovelTask in shovelTasks:
                        copyOfContext['tasks'].append(shovelTask)
                print('vamos andar')
            else:
                print('vamos atacar')
                # se for para atacar monstros
        gameContext = copyOfContext
        return copyOfContext

    def hasTasksToExecute(context):
        has = len(context['tasks']) > 0
        return has

    taskObserver = decisionObserver.pipe(
        operators.map(handleTasks),
        operators.filter(hasTasksToExecute),
        # operators.do_action(lambda context: 1),
        # reiniciar em caso de erro
        # reiniciar se não terminou corretamente
        # reiniciar após X segundos
    )

    def taskObservable(context):
        global gameContext
        copyOfContext = context.copy()
        task = copyOfContext['tasks'][0]
        execResponse = task['shouldExec'](copyOfContext)
        shouldNotExec = execResponse == False
        if shouldNotExec:
            return
        if task['status'] == 'notStarted':
            task['status'] = 'running'
            # compare time instead of sleeping
            time.sleep(task['delay'])
            task['do'](copyOfContext)
            copyOfContext['tasks'][0] = task
        elif task['status'] == 'running':
            didTaskResponse = task['did'](copyOfContext)
            didTask = didTaskResponse == True
            if didTask:
                copyOfContext['tasks'].pop(0)
        gameContext = copyOfContext

    taskObserver.subscribe(taskObservable)

    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()
