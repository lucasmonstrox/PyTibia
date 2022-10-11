import multiprocessing
import numpy as np
import pyautogui
from rx import interval, of, operators, pipe, timer
from rx.scheduler import ThreadPoolScheduler
from rx.subject import Subject
import time
from typing import cast
import battleList.core
from chat import chat
import gameplay.cavebot
import gameplay.decision
import gameplay.waypoint
import hud.creatures
import hud.core
import hud.slot
import radar.core
from radar.types import waypointType
import utils.core
import utils.image


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

beingAttackedCreature = None
cavebotManager = {'status': None}
coordinateHudTracker = {'lastCoordinate': None, 'lastHudImg': None}
comingFromDirection = None
corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
hudCreatures = np.array([], dtype=hud.creatures.creatureType)
lastWay = 'waypoint'
previousRadarCoordinate = None
walkpointsManager = {
    'lastCoordinateVisitedAt': time.time(),
    'lastCoordinateVisited': None,
    'lastPressedKey': None,
    'points': np.array([]),
}
waypointsManager = {
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
        ('floor', (33072, 32759, 8), 0),
        ('floor', (33096, 32762, 8), 0),
        ('floor', (33067, 32748, 8), 0),
        ('floor', (33085, 32775, 8), 0),
        ('floor', (33062, 32788, 8), 0),
        # stonerefinner
        # ('floor', (33037,31977,13), 0),
        # ('floor', (33039,32021,13), 0),
        # ('floor', (33078,32017,13), 0),
        # ('floor', (33041,32041,13), 0),
        # ('floor', (33079,32042,13), 0),
        # ('floor', (33034,32053,13), 0),

        # teste em curvas
        # ('floor', (33093, 32788, 7), 0),
        # ('floor', (33088, 32788, 7), 0),

        # teste em linha reta
        # ('floor', (33089, 32789, 7), 0),
        # ('floor', (33084, 32789, 7), 0),
    ], dtype=waypointType),
    'state': None
}


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    thirteenFps = 0.00833333333
    fpsObserver = interval(thirteenFps)
    fpsWithScreenshot = fpsObserver.pipe(
        operators.map(lambda _: {'screenshot': utils.image.RGBtoGray(
            utils.core.getScreenshot())}),
    )

    def getCoordinate(screenshot):
        global previousRadarCoordinate
        radarCoordinate = radar.core.getCoordinate(
            screenshot, previousRadarCoordinate=previousRadarCoordinate)
        return radarCoordinate

    coordinatesObserver = fpsWithScreenshot.pipe(
        operators.filter(lambda result: result['screenshot'] is not None),
        operators.map(lambda result: {
            'radarCoordinate': getCoordinate(result['screenshot']),
            'screenshot': result['screenshot'],
        })
    )

    battleListObserver = coordinatesObserver.pipe(
        operators.map(lambda result: {
            'battleListCreatures': battleList.core.getCreatures(result['screenshot']),
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
        })
    )

    hudCoordinateObserver = battleListObserver.pipe(
        operators.filter(lambda result: result['radarCoordinate'] is not None),
        operators.map(lambda result: {
            'battleListCreatures': result['battleListCreatures'],
            'hudCoordinate': hud.core.getCoordinate(result['screenshot']),
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
        })
    )

    hudImgObserver = hudCoordinateObserver.pipe(
        operators.map(lambda result: {
            'battleListCreatures': result['battleListCreatures'],
            'hudCoordinate': result['hudCoordinate'],
            'hudImg': hud.core.getImgByCoordinate(result['screenshot'], result['hudCoordinate']),
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
        })
    )

    def resolveDirection(result):
        global comingFromDirection, previousRadarCoordinate
        # Se a coordenada anterior for None, setar com o valor da coordenada atual
        if previousRadarCoordinate is None:
            previousRadarCoordinate = result['radarCoordinate']
        coordinateDidChange = np.all(
            previousRadarCoordinate == result['radarCoordinate']) == False
        if coordinateDidChange:
            radarCoordinate = result['radarCoordinate']
            # Verificar se mudou de andar
            if radarCoordinate[2] != previousRadarCoordinate[2]:
                comingFromDirection = None
            # Verificar se foi teleport/lag
            elif radarCoordinate[0] != previousRadarCoordinate[0] and radarCoordinate[1] != previousRadarCoordinate[1]:
                comingFromDirection = None
            elif radarCoordinate[0] != previousRadarCoordinate[0]:
                # Verificar se está vindo da esquerda/direita
                # - Para determinar se está vindo da esquerda, basta o x da coordenada atual ser maior que o x da coordenada anterior
                # - Para determinar se está vindo da direita, basta o x da coordenada atual ser menor que o x da coordenada anterior
                comingFromDirection = 'left' if radarCoordinate[
                    0] > previousRadarCoordinate[0] else 'right'
            elif radarCoordinate[1] != previousRadarCoordinate[1]:
                # Verificar cima/baixa
                # - Para determinar se está vindo de cima, basta o y da coordenada atual ser menor que o y da coordenada anterior
                # - Para determinar se está vindo de baixo, basta o y da coordenada atual ser maior que o y da coordenada anterior
                comingFromDirection = 'top' if radarCoordinate[
                    1] > previousRadarCoordinate[1] else 'bottom'
            previousRadarCoordinate = result['radarCoordinate']
        return {
            'battleListCreatures': result['battleListCreatures'],
            'comingFromDirection': comingFromDirection,
            'hudCoordinate': result['hudCoordinate'],
            'hudCreatures': hudCreatures,
            'hudImg': result['hudImg'],
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
        }

    directionObserver = hudImgObserver.pipe(operators.map(resolveDirection))

    def resolveCreatures(result):
        global comingFromDirection, previousRadarCoordinate
        hudCreatures = hud.creatures.getCreatures(
            result['battleListCreatures'], comingFromDirection, result['hudCoordinate'], result['hudImg'], result['radarCoordinate'])
        return {
            'battleListCreatures': result['battleListCreatures'],
            'comingFromDirection': result['comingFromDirection'],
            'hudCoordinate': result['hudCoordinate'],
            'hudCreatures': hudCreatures,
            'hudImg': result['hudImg'],
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
        }

    hudCreaturesObserver = directionObserver.pipe(
        operators.map(resolveCreatures))

    def lootObservable(result):
        global beingAttackedCreature, corpsesToLoot
        screenshot = result['screenshot']
        hudCreatures = result['hudCreatures']
        beingAttackedIndexes = np.where(
            hudCreatures['isBeingAttacked'] == True)[0]
        hasCreatureBeingAttacked = len(beingAttackedIndexes) > 0
        if chat.hasNewLoot(screenshot) and beingAttackedCreature:
            corpsesToLoot = np.append(
                corpsesToLoot, [beingAttackedCreature], axis=0)
        if hasCreatureBeingAttacked:
            beingAttackedCreature = hudCreatures[beingAttackedIndexes[0]]
        else:
            beingAttackedCreature = None
        return corpsesToLoot

    lootObserver = hudCreaturesObserver.pipe(operators.map(lambda result: {
        'battleListCreatures': result['battleListCreatures'],
        'comingFromDirection': result['comingFromDirection'],
        'corpsesToLoot': lootObservable(result),
        'hudCoordinate': result['hudCoordinate'],
        'hudCreatures': result['hudCreatures'],
        'hudImg': result['hudImg'],
        'radarCoordinate': result['radarCoordinate'],
        'screenshot': result['screenshot'],
    }))

    decisionObserver = lootObserver.pipe(
        operators.map(lambda result: {
            'battleListCreatures': result['battleListCreatures'],
            'comingFromDirection': result['comingFromDirection'],
            'hudCoordinate': result['hudCoordinate'],
            'hudCreatures': result['hudCreatures'],
            'hudImg': result['hudImg'],
            'radarCoordinate': result['radarCoordinate'],
            'screenshot': result['screenshot'],
            'way': gameplay.decision.getWay(result['corpsesToLoot'], result['hudCreatures'], result['radarCoordinate']),
        })
    )

    def waypointObservable(result):
        global cavebotManager, coordinateHudTracker, corpsesToLoot, lastWay, walkpointsManager, waypointsManager
        if waypointsManager['currentIndex'] == None:
            waypointsManager['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                result['radarCoordinate'], waypointsManager['points'])
        if result['way'] == 'lootCorpses':
            walkpoints = gameplay.waypoint.generateFloorWalkpoints(
                result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
            if len(walkpoints) > 1:
                walkpoints = np.delete(walkpoints, -1, axis=0)
            walkpointsManager['points'] = walkpoints
            if len(walkpointsManager['points']) == 0:
                time.sleep(1)
                slot = hud.core.getSlotFromCoordinate(
                    result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
                pyautogui.keyDown('shift')
                time.sleep(0.1)
                hud.slot.rightClickSlot(slot, result['hudCoordinate'])
                time.sleep(0.1)
                pyautogui.keyUp('shift')
                corpsesToLoot = np.delete(corpsesToLoot, 0)
        if result['way'] == 'cavebot':
            cavebotManager, walkpointsManager = gameplay.cavebot.handleCavebot(
                result['battleListCreatures'],
                cavebotManager,
                result['hudCreatures'],
                result['radarCoordinate'],
                walkpointsManager
            )
        else:
            if lastWay == 'cavebot':
                walkpointsManager['lastCoordinateVisited'] = None
                walkpointsManager['points'] = np.array([])
                walkpointsManager['state'] = None
            waypointsManager = gameplay.waypoint.handleWaypoint(
                result['screenshot'],
                result['radarCoordinate'],
                waypointsManager,
            )
            walkpointsManager = gameplay.waypoint.handleWalkpoints(
                result['radarCoordinate'],
                walkpointsManager,
                waypointsManager
            )
        walkpointsManager = gameplay.waypoint.walk(
            result['radarCoordinate'],
            walkpointsManager
        )
        lastWay = result['way']

    decisionObserver.subscribe(waypointObservable)

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
# - mudar o calculo path finding para o paths do tibiamaps e ignorar buracos, escadas, etc
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

# Detecção:
# - (x) as vezes os monstros estão com slots 255
# - detectar npcs
# - detectar objetos bloqueante
