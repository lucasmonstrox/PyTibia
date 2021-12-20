from battleList import battleList
from player import player
from radar import radar
import asyncio
import pyautogui
import rx
import numpy as np
from utils import utils
from time import sleep, time
from threading import Thread
from timeit import default_timer as timer

currentWaypointIndex = 0

waypoints = [
    # 0
    {
        "type": "floor",
        "coordinate": (33121, 32837, 7),
        "walkType": "screen"
    },
    # 1
    {
        "type": "floor",
        "coordinate": (33122, 32837, 7),
        "walkType": "screen"
    },
    # 2
    {
        "type": "floor",
        "coordinate": (33117, 32833, 7),
        "walkType": "screen"
    },
    {
        "type": "floor",
        "coordinate": (33085, 32788, 7),
        "walkType": "radar"
    },
    # 3
    {
        "type": "stairs",
        "coordinate": (33085, 32786, 6),
        "direction": "up"
    },
    # 4
    {
        "type": "floor",
        "coordinate": (33085, 32785, 6),
        "walkType": "screen"
    },
    # 5
    {
        "type": "stairs",
        "coordinate": (33085, 32783, 6),
        "direction": "up"
    },
    # 6
    {
        "type": "floor",
        "coordinate": (33038, 32810, 7),
        "walkType": "radar"
    },
    # 7
    {
        "type": "stairs",
        "coordinate": (33038, 32808, 6),
        "direction": "up"
    },
    # 8
    {
        "type": "floor",
        "coordinate": (33033, 32801, 6),
        "walkType": "radar"
    },
    # 9
    {
        "type": "stairs",
        "coordinate": (33033, 32799, 6),
        "direction": "up"
    },
    # 10
    {
        "type": "floor",
        "coordinate": (33032, 32779, 6),
        "walkType": "radar"
    },
    # 11
    {
        "type": "stairs",
        "coordinate": (33032, 32777, 4),
        "direction": "up"
    },
    # 12
    {
        "type": "floor",
        "coordinate": (33032, 32786, 4),
        "walkType": "radar"
    },
    # 13
    {
        "type": "stairs",
        "coordinate": (33032, 32788, 3),
        "direction": "down"
    },
    # 14
    {
        "type": "floor",
        "coordinate": (33031, 32788, 3),
        "walkType": "radar"
    },
    # 15
    {
        "type": "stairs",
        "coordinate": (33029, 32788, 2),
        "direction": "left"
    },
    # 16
    {
        "type": "floor",
        "coordinate": (33029, 32781, 2),
        "walkType": "radar"
    },
    # 17
    {
        "type": "stairs",
        "coordinate": (33029, 32779, 1),
        "direction": "up"
    },
    # 18
    {
        "type": "floor",
        "coordinate": (33029, 32776, 1),
        "walkType": "radar"
    },
    # 19
    {
        "type": "stairs",
        "coordinate": (33029, 32774, 0),
        "direction": "up"
    },
    # 20
    {
        "type": "floor",
        "coordinate": (33030, 32756, 0),
        "walkType": "radar"
    },
    # 21
    {
        "type": "stairs",
        "coordinate": (33032, 32756, 1),
        "direction": "right"
    },
    # 22
    {
        "type": "floor",
        "coordinate": (33021, 32746, 0),
        "walkType": "radar"
    },
    # 23
    {
        "type": "stairs",
        "coordinate": (33019, 32746, 2),
        "direction": "left"
    },
    # 24
    {
        "type": "floor",
        "coordinate": (33016, 32745, 2),
        "walkType": "radar"
    },
    # 25
    {
        "type": "stairs",
        "coordinate": (33016, 32743, 3),
        "direction": "up"
    },
    # 26
    {
        "type": "floor",
        "coordinate": (33010, 32727, 3),
        "walkType": "radar"
    },
    # 27
    {
        "type": "stairs",
        "coordinate": (33010, 32725, 4),
        "direction": "up"
    },
    # 28
    {
        "type": "floor",
        "coordinate": (32999, 32703, 4),
        "walkType": "radar"
    },
    # 29
    {
        "type": "stairs",
        "coordinate": (32999, 32705, 5),
        "direction": "down"
    },
    # 30
    {
        "type": "floor",
        "coordinate": (32998, 32709, 5),
        "walkType": "radar"
    },
    # 31
    {
        "type": "stairs",
        "coordinate": (32998, 32711, 4),
        "direction": "down"
    },
    # 32
    {
        "type": "floor",
        "coordinate": (32982, 32715, 6),
        "walkType": "radar"
    },
    # 33
    {
        "type": "stairs",
        "coordinate": (32982, 32717, 7),
        "direction": "down"
    },
    # 34
    {
        "type": "floor",
        "coordinate": (32958, 32760, 7),
        "walkType": "radar"
    },
    # 35
    {
        "type": "floor",
        "coordinate": (32951, 32785, 7),
        "walkType": "radar"
    },
    # 36
    {
        "type": "floor",
        "coordinate": (33004, 32750, 7),
        "walkType": "radar"
    },
    # 37
    {
        "type": "stairs",
        "coordinate": (33006, 32750, 7),
        "direction": "right"
    },
    # 38
    {
        "type": "floor",
        "coordinate": (33015, 32749, 6),
        "walkType": "radar"
    },
    # 39
    {
        "type": "stairs",
        "coordinate": (33015, 32751, 5),
        "direction": "down"
    },
    # 40
    {
        "type": "stairs",
        "coordinate": (33015, 32753, 4),
        "direction": "down"
    },
    # 41
    {
        "type": "floor",
        "coordinate": (33009, 32770, 4),
        "walkType": "radar"
    },
    # 42
    {
        "type": "stairs",
        "coordinate": (33009, 32772, 5),
        "direction": "down"
    },
    # 43
    {
        "type": "floor",
        "coordinate": (33004, 32765, 5),
        "walkType": "radar"
    },
    # 44
    {
        "type": "stairs",
        "coordinate": (33004, 32767, 5),
        "direction": "down"
    },
    # 45
    {
        "type": "floor",
        "coordinate": (33004, 32770, 6),
        "walkType": "radar"
    },
    # 46
    {
        "type": "stairs",
        "coordinate": (33004, 32772, 7),
        "direction": "down"
    },
    # 45
    {
        "type": "floor",
        "coordinate": (33001, 32791, 7),
        "walkType": "radar"
    },
    # 46
    {
        "type": "floor",
        "coordinate": (32998, 32788, 7),
        "walkType": "radar"
    },
    # 47
    {
        "type": "floor",
        "coordinate": (32986, 32794, 7),
        "walkType": "radar"
    },
    # 48
    {
        "type": "floor",
        "coordinate": (32995, 32813, 7),
        "walkType": "radar"
    },
    # 49
    {
        "type": "floor",
        "coordinate": (32976, 32825, 7),
        "walkType": "radar"
    },
]


def trackWaypointObservable(observer, scheduler):
    while True:
        playerCurrentCoordinate = player.getCoordinate()
        observer.on_next(playerCurrentCoordinate)


trackWaypointObserver = rx.create(trackWaypointObservable)

# TODO: get closest waypoint to continue if possible


def markWaypointObservable(observer, scheduler):
    """
    Waypoint types:
    floor
    hole
    stairs
    """
    global trackWaypointObserver

    def markWaypointInner(currentCoordinate):
        global currentWaypointIndex, isAttackingMonsters, shouldRetryWaypoint, trackWaypointObserver, waypoints
        if isAttackingMonsters:
            return
        currentCoordinateX, currentCoordinateY, currentCoordinateZ = currentCoordinate
        isLastWaypoint = currentWaypointIndex + 1 >= len(waypoints) - 1
        nextWaypointIndex = 0 if isLastWaypoint else currentWaypointIndex + 1
        if shouldRetryWaypoint:
            shouldRetryWaypoint = False
            observer.on_next(waypoints[nextWaypointIndex])
            return
        nextWaypointX, nextWaypointY, nextWaypointZ = waypoints[
            currentWaypointIndex + 1]['coordinate']
        isSameWaypoint = currentCoordinateX == nextWaypointX and currentCoordinateY == nextWaypointY
        if isSameWaypoint:
            currentWaypointIndex = -1 if isLastWaypoint else nextWaypointIndex
            nextIndex = 0 if isLastWaypoint else currentWaypointIndex + 1
            observer.on_next(waypoints[nextIndex])

    # TODO: add pipe to avoid observer when player is attacking monsters
    trackWaypointObserver.subscribe(
        lambda waypoint: markWaypointInner(waypoint),
    )


def walk(waypoint):
    global isAttackingMonsters
    if isAttackingMonsters:
        return
    sleep(3)
    if waypoint['type'] == 'floor':
        if waypoint['walkType'] == 'radar':
            player.goToCoordinateByRadarClick(waypoint['coordinate'])
            return
        if waypoint['walkType'] == 'screen':
            player.goToCoordinateByScreenClick(waypoint['coordinate'])
            return
        return
    if waypoint['type'] == 'stairs':
        pyautogui.press(waypoint['direction'])


monstersHashes = {
}

shouldRetryWaypoint = True


def walkingScanner():
    markWaypointObserver = rx.create(markWaypointObservable)
    markWaypointObserver.subscribe(
        lambda waypoint: walk(waypoint),
    )


isAttackingMonsters = False


def attackingScanner():
    async def inner():
        global isAttackingMonsters, shouldRetryWaypoint
        while True:
            monsters = battleList.getCreatures()
            hasNoMonstersToAttack = len(monsters) == 0
            if hasNoMonstersToAttack:
                isAttackingMonsters = False
                continue
            monsterIsBeingAttacked = False
            for monster in monsters:
                if monster['isBeingAttacked']:
                    monsterIsBeingAttacked = True
                    continue
            if monsterIsBeingAttacked:
                isAttackingMonsters = True
                continue
            pyautogui.press('esc')
            if player.isHoldingAttack():
                player.enableFollowingAttack()
            x, y = monsters[0]['coordinate']
            pyautogui.click(x + 30, y)
            shouldRetryWaypoint = True
    asyncio.run(inner())


def main():
    # attackingScannerThread = Thread(target=attackingScanner)
    # attackingScannerThread.start()
    # walkingScannerThread = Thread(target=walkingScanner)
    # walkingScannerThread.start()
    print(1)


if __name__ == '__main__':
    main()
