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
    'comingFromDirection': None,
    'corpsesToLoot': np.array([], dtype=hud.creatures.creatureType),
    'hudCoordinate': None,
    'hudCreatures': np.array([], dtype=hud.creatures.creatureType),
    'hudImg': None,
    'previousRadarCoordinate': None,
    'radarCoordinate': None,
    'waypointsManager': {
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
cavebotManager = {'status': None}
coordinateHudTracker = {'lastCoordinate': None, 'lastHudImg': None}
comingFromDirection = None
hudCreatures = np.array([], dtype=hud.creatures.creatureType)
lastWay = 'waypoint'


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
            copyOfContext['battleListCreatures'], comingFromDirection, copyOfContext['hudCoordinate'], copyOfContext['hudImg'], copyOfContext['radarCoordinate'])
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
        gameContext = copyOfContext
        return copyOfContext

    decisionObserver = lootObserver.pipe(
        operators.map(handleDecision)
    )

    # def waypointObservable(result):
    #     global cavebotManager, coordinateHudTracker, corpsesToLoot, lastWay, walkpointsManager, waypointsManager
    #     if waypointsManager['currentIndex'] == None:
    #         waypointsManager['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
    #             result['radarCoordinate'], waypointsManager['points'])
    #     if result['way'] == 'lootCorpses':
    #         walkpoints = gameplay.waypoint.generateFloorWalkpoints(
    #             result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
    #         if len(walkpoints) > 1:
    #             walkpoints = np.delete(walkpoints, -1, axis=0)
    #         walkpointsManager['points'] = walkpoints
    #         if len(walkpointsManager['points']) == 0:
    #             time.sleep(1)
    #             slot = hud.core.getSlotFromCoordinate(
    #                 result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
    #             pyautogui.keyDown('shift')
    #             time.sleep(0.1)
    #             hud.slot.rightClickSlot(slot, result['hudCoordinate'])
    #             time.sleep(0.1)
    #             pyautogui.keyUp('shift')
    #             corpsesToLoot = np.delete(corpsesToLoot, 0)
    #     if result['way'] == 'cavebot':
    #         cavebotManager, walkpointsManager = gameplay.cavebot.handleCavebot(
    #             result['battleListCreatures'],
    #             cavebotManager,
    #             result['hudCreatures'],
    #             result['radarCoordinate'],
    #             walkpointsManager
    #         )
    #     else:
    #         if lastWay == 'cavebot':
    #             walkpointsManager['lastCoordinateVisited'] = None
    #             walkpointsManager['points'] = np.array([])
    #             walkpointsManager['state'] = None
    #         waypointsManager = gameplay.waypoint.handleWaypoint(
    #             result['screenshot'],
    #             result['radarCoordinate'],
    #             waypointsManager,
    #         )
    #         walkpointsManager = gameplay.waypoint.handleWalkpoints(
    #             result['radarCoordinate'],
    #             walkpointsManager,
    #             waypointsManager
    #         )
    #     walkpointsManager = gameplay.waypoint.walk(
    #         result['radarCoordinate'],
    #         walkpointsManager
    #     )
    #     lastWay = result['way']

    # decisionObserver.subscribe(waypointObservable)

    def isNotDoingTask(task):
        return task['status'] != 'running'

    def handleTasks(context):
        global gameContext
        copyOfContext = context.copy()
        copiedWaypointsManager = copyOfContext['waypointsManager'].copy()
        hasNoTasks = len(copyOfContext['tasks']) == 0
        if hasNoTasks:
            nextWaypointIndex = utils.array.getNextArrayIndex(
                copiedWaypointsManager['points'], context['waypointsManager']['currentIndex'])
            nextWaypoint = context['waypointsManager']['points'][nextWaypointIndex]
            copyOfContext['tasks'].append(
                {
                    'delay': 0.5,
                    'shouldExec': makeIsNearToHole(nextWaypoint['coordinate']),
                    'do': lambda _: True,
                    'status': 'notStarted',
                },
            )
            copyOfContext['tasks'].append({
                'delay': 0,
                'shouldExec': makeIsHoleClosed(nextWaypoint['coordinate']),
                'do': makeOpenHole(nextWaypoint['coordinate']),
                'status': 'notStarted',
            })
            copyOfContext['tasks'].append({
                'delay': 0,
                'shouldExec': lambda _: True,
                'do': lambda _: pyautogui.press('left'),
                'status': 'notStarted',
            })
        gameContext = copyOfContext
        return copyOfContext

    def hasTasksToExecute(context):
        has = len(context['tasks']) > 0
        return has

    def handleNotDoingTask(context):
        task = context['tasks'][0]
        isNotDoing = isNotDoingTask(task)
        return isNotDoing

    taskObserver = lootObserver.pipe(
        operators.map(handleTasks),
        operators.filter(hasTasksToExecute),
        operators.filter(handleNotDoingTask),
        # operators.delay_with_mapper(
        #     lambda context: context['tasks'][0]['delay']),
        # operators.do_action(lambda context: 1),
        # reiniciar em caso de erro
        # reiniciar se não terminou corretamente
        # reiniciar após X segundos
    )

    def makeIsNearToHole(roleRadarCoordinate):
        def isNearToHole(context):
            distances = distance.cdist(
                [context['radarCoordinate']], [roleRadarCoordinate])
            distanceBetweenRoleAndChar = distances[0][0]
            isNear = distanceBetweenRoleAndChar <= 1
            return isNear
        return isNearToHole

    def makeIsHoleClosed(roleRadarCoordinate):
        def isHoleClosed(context):
            slot = hud.core.getSlotFromCoordinate(
                context['radarCoordinate'], roleRadarCoordinate)
            hudImg = context['hudImg']
            slotImg = hud.core.getSlotImg(hudImg, slot)
            isClosed = hud.core.isHoleOpen(slotImg) == False
            return isClosed
        return isHoleClosed

    def makeOpenHole(roleRadarCoordinate):
        def openHole(context):
            slot = hud.core.getSlotFromCoordinate(
                context['radarCoordinate'], roleRadarCoordinate)
            pyautogui.press('f9')
            hud.slot.clickSlot(slot, context['hudCoordinate'])
        return openHole

    def taskObservable(context):
        global gameContext
        copyOfContext = context.copy()
        task = copyOfContext['tasks'][0]
        execResponse = task['shouldExec'](copyOfContext)
        shouldNotExec = execResponse == False
        if shouldNotExec:
            return
        taskIsNotStarted = task['status'] == 'notStarted'
        if taskIsNotStarted:
            task['status'] = 'running'
            time.sleep(task['delay'])
            task['do'](copyOfContext)
            task['status'] = 'finishedSuccessfully'
            copyOfContext['tasks'].pop(0)
        gameContext = copyOfContext

    taskObserver.subscribe(taskObservable)

    # def waypointObservable(result):
    #     global cavebotManager, coordinateHudTracker, corpsesToLoot, lastWay, walkpointsManager, waypointsManager
    #     if waypointsManager['currentIndex'] == None:
    #         waypointsManager['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
    #             result['radarCoordinate'], waypointsManager['points'])
    #     waypointsManager = gameplay.waypoint.handleWaypoint(
    #         result['screenshot'],
    #         result['radarCoordinate'],
    #         waypointsManager,
    #     )
    #     walkpointsManager = gameplay.waypoint.handleWalkpoints(
    #         result['radarCoordinate'],
    #         walkpointsManager,
    #         waypointsManager
    #     )
    #     walkpointsManager = gameplay.waypoint.walk(
    #         result['radarCoordinate'],
    #         walkpointsManager
    #     )

    # decisionObserver.subscribe(waypointObservable)

    # controladores:
    # - verificar os estados das suas tarefas filhas
    # - recalcular tarefas em caso de caminho errado
    # - mandar tarefas serem reiniciadas
    # - mandar para a proxima tarefa
    # - limpar tarefas??

    # Actions:
    # - delay to start
    # - has a durability
    # - can retry
    # - pode entrar em loop
    # - shouldIgnore
    # - talvez, voltar para o estado anterior
    #
    # Executar ações
    # - receber o screenshot
    # - receber a função que verifica se a ação foi executada
    # Action states:
    # - notInitialized
    # - running
    # - error
    # - finishedSuccessfully
    # - finishedUnsuccessfully
    #
    # Actions
    #
    # - attackMonster:
    # -- move mouse to monster
    # -- check if creature is in SQM
    # --- mouse right click
    # --- walkToCoordinate(monster.coordinate)
    #
    # - castSpell
    #
    # - climbDownRamp
    #
    # - climbUpRamp
    #
    # - collectLoot:
    # -- walkToCoordinate(deadMonsterCorpse.coordinate)
    # -- check if is near to monster
    # --- move mouse to monster
    # --- shift + right click
    #
    # - drinkHealthPotion
    #
    # - drinkManaPotion
    #
    # - eatFood
    #
    # - goToHole:
    # -- walkToCoordinate(hole.nearCoordinate)
    # -- check if is near to hole
    # -- check if hole is closed
    # --- open hole
    # -- walkToCoordinate(hole.coordinate)
    #
    # - heal
    #
    # - useShovel:
    # -- walkToCoordinate(hole.nearCoordinate)
    # -- check if is near to hole
    # -- press shovel bind key
    # -- move mouse to hole
    # -- left click
    #
    # - walkToCoordinate:
    # -- andar até a próxima coordenada

    # Criar um sistema de fila com prioridades
    # Criar um observer que faz as ações, da retry em caso de erro e em casa de insucesso

    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()


# TODO:
# - (x) fica parado quando nao tem target para os bichos fora da tela
# - (x) nao se mexer quando a distancia do target é só 1
# - (x) varios errors de friction tile


# Walk:
# - (x) quando está andando e de repente fica parado, recalcular rota e reiniciar walk
# - quando anda pra fora do caminho traçado, recalcular rota e reiniciar walk
# - (x) mudar o calculo path finding para o paths do tibiamaps e ignorar buracos, escadas, etc
# - as vezes da sorry not possible ao andar mesmo sem errar o path, possivelmente batendo sensivelmente nas paredes
# - o bot não ignora as piramides e muda de andar, ignorar coordenadas amarelas pra gerar caminho

# Cavebot:
# - cliques excessivos quando nao consegue atacar o monstro
# - está clicando fora do target porque o boneco está em movimentação
# - (x) as vezes não detecta que a creature está com target e faz varias tentativas
# - (x) as vezes ataca, há target e não segue
# - (x) algumas vezes há target mas ele fica andando pra esquerda/direita ou todo torto
# - quando clica nos edges da hud, acabando clicando nas slots bars
# - quando o target está longe e ainda não atacou e aparece alguem mais proximo, deveria mudar o target
# - o que fazer quando tem target e de repente o target desaparece pois tem q dar a volta?
