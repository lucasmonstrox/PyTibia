import multiprocessing
import numpy as np
import pyautogui
from rx import interval, of, operators, pipe, timer
from rx.scheduler import ThreadPoolScheduler
from rx.subject import Subject
import time
from typing import cast
import battleList.core
import gameplay.cavebot
import gameplay.decision
import gameplay.waypoint
import hud.creatures
import radar.core
from radar.types import waypointType
import utils.core
import utils.image


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


# TODO:
# - clicando sem querer nas actionBar slots quando os monstros estão nas edges da hud
# - (x) fica parado quando nao tem target para os bichos fora da tela
# - (x) nao se mexer quando a distancia do target é só 1
# - cliques excessivos quando nao consegue atacar o monstro
# - varios errors de friction tile
# - quando o target está longe e ainda não atacou e aparece alguem mais proximo, mudar o target
# - o bot não ignora as piramides e muda de andar, ignorar coordenadas amarelas pra gerar caminho
# - o que fazer quando tem target e de repente perde o target?

previousCoordinate = None
walkpointsManager = {
    "coordinateDidChange": True,
    "currentIndex": 0,
    "lastCoordinateVisited": None,
    "lastCrossedTime": 0,
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
        # ('floor', (33076, 32756, 8), 0),
        # ('floor', (33083, 32761, 8), 0),
        # ('floor', (33090, 32765, 8), 0),
        # ('floor', (33096, 32762, 8), 0),
        # ('floor', (33098, 32758, 8), 0),
        # ('floor', (33099, 32765, 8), 0),
        # ('floor', (33072, 32760, 8), 0),

        # test 2000
        # ('floor', (33082, 32596, 6), 0),
        # ('floor', (33094, 32600, 6), 0),
        # ('floor', (33092, 32618, 6), 0),
        # ('floor', (33119, 32603, 6), 0),

        # teste em curvas
        # ('floor', (33082, 32788, 7), 0),
        # ('floor', (33088, 32788, 7), 0),
        # ('floor', (33092, 32791, 7), 0),
        # ('floor', (33084, 32791, 7), 0),

        # teste em linha reta
        ('floor', (33089, 32789, 7), 0),
        ('floor', (33084, 32789, 7), 0),
    ], dtype=waypointType),
    "state": None
}


def shouldExecuteWaypoint(battleListCreatures):
    hasNoBattleListCreatures = len(battleListCreatures) == 0
    return hasNoBattleListCreatures


# def switch_map(mapper):
#     mapper_ = mapper or cast(of)
#     return pipe(
#         operators.map(mapper_),
#         operators.switch_latest(),
#     )


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    thirteenFps = 0.0166
    fpsObserver = interval(thirteenFps)
    # mouseObserver = Subject()
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
    hudCreaturesObserver = battleListObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCreatures": hud.creatures.getCreatures(result["screenshot"], result["battleListCreatures"], result["radarCoordinate"])
        })
    )
    decisionObserver = hudCreaturesObserver.pipe(
        operators.map(lambda result: {
            "screenshot": result["screenshot"],
            "radarCoordinate": result["radarCoordinate"],
            "battleListCreatures": result["battleListCreatures"],
            "hudCreatures": result["hudCreatures"],
            "way": gameplay.decision.getWay(result['hudCreatures'], result['radarCoordinate']),
        })
    )
    # cavebotObserver = decisionObserver.pipe(
    #     operators.filter(lambda result: result['way'] == 'cavebot'),
    # )
    # def cavebotObservable(result):
    #     global walkpointsManager
    #     walkpointsManager = gameplay.cavebot.handleCavebot(
    #         result['battleListCreatures'],
    #         result['hudCreatures'],
    #         result['radarCoordinate'],
    #         walkpointsManager
    #     )
    # cavebotObserver.subscribe(cavebotObservable)
    waypointObserver = decisionObserver.pipe(
        operators.filter(lambda result: True),
    )

    def waypointObservable(result):
        global walkpointsManager, waypointsManager
        if waypointsManager['currentIndex'] == None:
            waypointsManager['currentIndex'] = radar.core.getClosestWaypointIndexFromCoordinate(
                result['radarCoordinate'], waypointsManager['points'])
        result['way'] = 'waypoint'
        if result['way'] == 'cavebot':
            walkpointsManager = gameplay.cavebot.handleCavebot(
                result['battleListCreatures'],
                result['hudCreatures'],
                result['radarCoordinate'],
                walkpointsManager
            )
        else:
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
    waypointObserver.subscribe(waypointObservable)
    # mousePoint = mouseObserver.pipe(
    #     switch_map(lambda items: timer(0, 0.005).pipe(
    #         operators.map(lambda i: items[i]),
    #         operators.take(len(items))
    #     )),
    # )
    # mousePoint.subscribe(
    #     lambda res: pyautogui.moveTo(res[0], res[1]),
    #     lambda err: print('err', err),
    #     lambda: print('complete'),
    # )
    while True:
        time.sleep(10)
        continue


if __name__ == '__main__':
    main()
