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

cavebotManager = {
    "status": None
}
lastWay = 'waypoint'
previousCoordinate = None
walkpointsManager = {
    "lastCoordinateVisitedAt": time.time(),
    "lastCoordinateVisited": None,
    "lastPressedKey": None,
    "points": np.array([]),
}
waypointsManager = {
    "currentIndex": 0,
    "points": np.array([
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
    "state": None
}


def shouldExecuteWaypoint(battleListCreatures):
    hasNoBattleListCreatures = len(battleListCreatures) == 0
    return hasNoBattleListCreatures


beingAttackedCreature = None
corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
coordinateHudTracker = {
    "lastCoordinate": None,
    "lastHudImg": None,
    "currentCoordinate": None,
}
hudCreatures = np.array([], dtype=hud.creatures.creatureType)
lastDisplacedXPixels = 0
lastDisplacedYPixels = 0
lastXPercentage = 0
lastYPercentage = 0


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    thirteenFps = 0.00833333333
    fpsObserver = interval(thirteenFps)
    fpsWithScreenshot = fpsObserver.pipe(
        operators.map(lambda _: {"screenshot": utils.image.RGBtoGray(
            utils.core.getScreenshot())}),
    )

    def getCoordinate(screenshot):
        global previousCoordinate
        previousCoordinate = radar.core.getCoordinate(
            screenshot, previousCoordinate=previousCoordinate)
        return previousCoordinate
    coordinatesObserver = fpsWithScreenshot.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": getCoordinate(result["screenshot"]),
        })
    )
    battleListObserver = coordinatesObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": battleList.core.getCreatures(result["screenshot"])
        })
    )

    hudCoordinateObserver = battleListObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCoordinate": hud.core.getCoordinate(result['screenshot']),
        })
    )

    hudImgObserver = hudCoordinateObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCoordinate": result['hudCoordinate'],
            "hudImg": hud.core.getImgByCoordinate(result['screenshot'], result['hudCoordinate'])
        })
    )

    def resolveCreatures(result):
        global coordinateHudTracker, hudCreatures, lastDisplacedXPixels, lastDisplacedYPixels, lastXPercentage, lastYPercentage
        displacedXPixels = 0
        displacedYPixels = 0
        if coordinateHudTracker["currentCoordinate"] is None:
            coordinateHudTracker["currentCoordinate"] = result['radarCoordinate']
            coordinateHudTracker['lastHudImg'] = result['hudImg']
        hudSlice = result['hudImg'][64:80, 96:-96]
        hudImgPercentageLocate = utils.core.locate(
            coordinateHudTracker['lastHudImg'], hudSlice)
        if hudImgPercentageLocate is not None:
            if result['radarCoordinate'][0] != coordinateHudTracker["currentCoordinate"][0]:
                isComingFromLeft = coordinateHudTracker["currentCoordinate"][0] < result['radarCoordinate'][0]
                add32 = 32 if isComingFromLeft else -32
                xPercentage = hudImgPercentageLocate[0] - 96
                displacedXPixels = add32 - \
                    (xPercentage - lastDisplacedXPixels)
                lastXPercentage = xPercentage
            if result['radarCoordinate'][1] != coordinateHudTracker["currentCoordinate"][1]:
                isComingFromTop = coordinateHudTracker["currentCoordinate"][1] < result['radarCoordinate'][1]
                yPercentage = hudImgPercentageLocate[1] - 64
                add32 = 32 if isComingFromTop else -32
                displacedYPixels = add32 - \
                    (yPercentage - lastDisplacedYPixels)
        lastDisplacedXPixels = displacedXPixels
        lastDisplacedYPixels = displacedYPixels
        if result['radarCoordinate'] != coordinateHudTracker["currentCoordinate"]:
            coordinateHudTracker = {
                "lastHudImg": result['hudImg'],
                "currentCoordinate": result['radarCoordinate'],
            }
        hudCreatures = hud.creatures.getCreatures(
            result["battleListCreatures"], result['hudCoordinate'], result['hudImg'], result["radarCoordinate"], displacedXPixels=displacedXPixels, displacedYPixels=displacedYPixels)
        return {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCoordinate": result['hudCoordinate'],
            "hudCreatures": hudCreatures,
            "hudImg": result['hudImg'],
        }
    hudCreaturesObserver = hudImgObserver.pipe(operators.map(resolveCreatures))

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
    hudCreaturesObserver.subscribe(lootObservable)

    decisionObserver = hudCreaturesObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCoordinate": result['hudCoordinate'],
            "hudCreatures": result["hudCreatures"],
            "hudImg": result['hudImg'],
            "way": gameplay.decision.getWay(corpsesToLoot, result['hudCreatures'], result['radarCoordinate']),
        })
    )
    waypointObserver = decisionObserver.pipe(
        operators.filter(lambda result: True),
    )

    def waypointObservable(result):
        global cavebotManager, coordinateHudTracker, corpsesToLoot, lastWay, walkpointsManager, waypointsManager
        if waypointsManager['currentIndex'] == None:
            waypointsManager['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                result['radarCoordinate'], waypointsManager['points'])
        # if result['way'] == 'lootCorpses':
        #     walkpoints = gameplay.waypoint.generateFloorWalkpoints(
        #         result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
        #     print('caminhos até o bicho morto', len(walkpoints))
        #     if len(walkpoints) > 1:
        #         walkpoints = np.delete(walkpoints, -1, axis=0)
        #     walkpointsManager['points'] = walkpoints
        #     print('dps do delete',
        #           len(walkpointsManager['points']))
        #     if len(walkpointsManager['points']) == 0:
        #         time.sleep(1)
        #         print('radarCoordinate do monstro',
        #               corpsesToLoot[0]['radarCoordinate'])
        #         slot = hud.core.getSlotFromCoordinate(
        #             result['radarCoordinate'], corpsesToLoot[0]['radarCoordinate'])
        #         pyautogui.keyDown('shift')
        #         time.sleep(0.1)
        #         hud.slot.rightClickSlot(slot, result['hudCoordinate'])
        #         time.sleep(0.1)
        #         pyautogui.keyUp('shift')
        #         corpsesToLoot = np.delete(corpsesToLoot, 0)
        # if result['way'] == 'cavebot':
        #     cavebotManager, walkpointsManager = gameplay.cavebot.handleCavebot(
        #         result['battleListCreatures'],
        #         cavebotManager,
        #         result['hudCreatures'],
        #         result['radarCoordinate'],
        #         walkpointsManager
        #     )
        # else:
        #     if lastWay == 'cavebot':
        #         walkpointsManager['lastCoordinateVisited'] = None
        #         walkpointsManager['points'] = np.array([])
        #         walkpointsManager['state'] = None
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
        # walkpointsManager = gameplay.waypoint.walk(
        #     result['radarCoordinate'],
        #     walkpointsManager
        # )
        # lastWay = result['way']
    waypointObserver.subscribe(waypointObservable)
    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()


# TODO:
# - clicando sem querer nas actionBar slots quando os monstros estão nas edges da hud
# - (x) fica parado quando nao tem target para os bichos fora da tela
# - (x) nao se mexer quando a distancia do target é só 1
# - cliques excessivos quando nao consegue atacar o monstro
# - (x) varios errors de friction tile
# - quando o target está longe e ainda não atacou e aparece alguem mais proximo, mudar o target
# - o bot não ignora as piramides e muda de andar, ignorar coordenadas amarelas pra gerar caminho
# - o que fazer quando tem target e de repente perde o target?
# - melhorar o target de ataque dependendo da direção

# Problemas walk:
# - (x) quando está andando e de repente fica parado, recalcular rota e reiniciar walk
# - quando anda pra fora do caminho traçado, recalcular rota e reiniciar walk
# - mudar o calculo path finding para o paths do tibiamaps e ignorar buracos, escadas, etc
# - as vezes da sorry not possible ao andar mesmo sem errar o path, possivelmente batendo sensivelmente nas paredes


# Problemas cavebot:
# - está clicando fora do target porque o boneco está em movimentação
# - as vezes não detecta que a creature está com target e faz varias tentativas
# - as vezes ataca, há target e não segue
# - algumas vezes há target mas ele fica andando pra esquerda/direita ou todo torto
# - quando clica nos edges da hud, acabando clicando nas slots bars
# - ao clicar numa criatura com target e ir pra cima e a criatura desaparecer, ele fica indo e voltado. A idéia é aumentar o gap.

# Coisas por detectar:
# - detectar npcs
# - detectar objetos bloqueante

# Lógica ideal:
# - visualizar, parar, atacar e correr atrás do bicho
