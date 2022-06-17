from battleList import battleList
from hud import hud
from observables import healing
from player import player
from radar import radar
from rx import operators
from rx.scheduler import ThreadPoolScheduler
from utils import utils
import numpy as np
import rx
import time
import pygetwindow as gw
import multiprocessing


waypointType = np.dtype([
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('tolerance', np.uint8)
])
waypoints = np.array([
    ('floor', (33085, 32788, 7), 0),
    ('ramp', (33085, 32786, 6), 0),
    ('floor', (33085, 32785, 6), 0),
    ('ramp', (33085, 32783, 7), 0),
    ('floor', (33038, 32810, 7), 0),
    ('ramp', (33038, 32808, 6), 0),
    ('floor', (33033, 32801, 6), 0),
    ('ramp', (33033, 32799, 5), 0),
    ('floor', (33032, 32779, 5), 0),
    ('ramp', (33032, 32777, 4), 0),
    ('floor', (33032, 32786, 4), 0),
    ('ramp', (33032, 32788, 3), 0),
    ('floor', (33031, 32788, 3), 0),
    ('ramp', (33029, 32788, 2), 0),
    ('floor', (33029, 32781, 2), 0),
    ('ramp', (33029, 32779, 1), 0),
    ('floor', (33029, 32776, 1), 0),
    ('ramp', (33029, 32774, 0), 0),
    ('floor', (33030, 32756, 0), 0),
    ('ramp', (33032, 32756, 1), 0),
    ('floor', (33021, 32746, 1), 0),
    ('ramp', (33019, 32746, 2), 0),
    ('floor', (33016, 32745, 2), 0),
    ('ramp', (33016, 32743, 3), 0),
    ('floor', (33010, 32727, 3), 0),
    ('ramp', (33010, 32725, 4), 0),
    ('floor', (32999, 32703, 4), 0),
    ('ramp', (32999, 32705, 5), 0),
    ('floor', (32998, 32709, 5), 0),
    ('ramp', (32998, 32711, 6), 0),
    ('floor', (32982, 32715, 6), 0),
    ('ramp', (32982, 32717, 7), 0),
    ('floor', (32953, 32769, 7), 0),
    ('floor', (33004, 32750, 7), 0),
    ('ramp', (33006, 32750, 6), 0),
    ('floor', (33015, 32749, 6), 0),
    ('ramp', (33015, 32751, 5), 0),
    ('ramp', (33015, 32753, 4), 0),
    ('floor', (33009, 32770, 4), 0),
    ('ramp', (33009, 32772, 5), 0),
    ('floor', (33004, 32765, 5), 0),
    ('ramp', (33004, 32767, 6), 0),
    ('floor', (33004, 32770, 6), 0),
    ('ramp', (33004, 32772, 7), 0),
    ('floor', (33004, 32772, 7), 10),
    ('floor', (32994, 32815, 7), 10),
    ('floor', (33003, 32831, 7), 10),
    ('floor', (32975, 32802, 7), 10),
    ('floor', (32957, 32824, 7), 10),
    ('floor', (32978, 32832, 7), 10),
    ('floor', (32981, 32857, 7), 10),
    ('floor', (32961, 32861, 7), 10),
    ('floor', (32958, 32834, 7), 10),
    ('floor', (32987, 32799, 7), 10),
    # ('floor', (32981, 32795, 7)),
    # ('floor', (32962, 32814, 7)),
    # ('floor', (32996, 32805, 7)),
    # ('floor', (33005, 32783, 7)),
], dtype=waypointType)
waypointIndex = None
shouldRetrySameWaypoint = True
window = None


def goToWaypoint(screenshot, waypoint, currentPlayerCoordinate):
    isFloorWaypoint = waypoint['type'] == 'floor'
    if isFloorWaypoint:
        radar.goToCoordinate(screenshot, currentPlayerCoordinate, waypoint['coordinate'])
        return
    isRampWaypoint = waypoint['type'] == 'ramp'
    if isRampWaypoint:
        (currentPlayerCoordinateX, currentPlayerCoordinateY, _) = currentPlayerCoordinate
        (waypointCoordinateX, waypointCoordinateY, _) = waypoint['coordinate']
        xDifference = currentPlayerCoordinateX - waypointCoordinateX
        shouldWalkToLeft = xDifference > 0
        if shouldWalkToLeft:
            utils.press('left')
            return
        shouldWalkToRight = xDifference < 0
        if shouldWalkToRight:
            utils.press('right')
            return
        yDifference = currentPlayerCoordinateY - waypointCoordinateY
        if yDifference < 0:
            utils.press('down')
            return
        if yDifference > 0:
            utils.press('up')
            return


def handleCavebot(screenshot, playerCoordinate, battleListCreatures):
    global shouldRetrySameWaypoint
    shouldRetrySameWaypoint = True
    hudCreatures = hud.getCreatures(screenshot, battleListCreatures)
    hasNoHudCreatures = len(hudCreatures) == 0
    if hasNoHudCreatures:
        print('has no hud creatures')
        return
    closestCreature = hud.getClosestCreature(hudCreatures, playerCoordinate, radar.config.walkableFloorsSqms[playerCoordinate[2]])
    hasNoClosestCreature = closestCreature == None
    if hasNoClosestCreature:
        print('has no closest creature')
        return
    hasOnlyOneCreature = len(hudCreatures) == 1
    if hasOnlyOneCreature:
        battleList.attackSlot(screenshot, 0)
    else:
        (x, y) = closestCreature['windowCoordinate']
        utils.rightClick(x, y)
    time.sleep(0.25)


def handleWaypoints(result):
    global shouldRetrySameWaypoint, waypointIndex
    screenshot = result[0]
    coordinate = result[1]
    if waypointIndex == None:
        waypointIndex = radar.getWaypointIndexFromClosestCoordinate(coordinate, waypoints)
    currentWaypoint = waypoints[waypointIndex]
    isCloseToCoordinate = radar.isCloseToCoordinate(
            coordinate, waypoints[waypointIndex]['coordinate'],
            distanceTolerance=currentWaypoint['tolerance'])
    if isCloseToCoordinate:
        waypointIndex = 0 if waypointIndex == len(
            waypoints) - 1 else waypointIndex + 1
        shouldRetrySameWaypoint = False
        player.stop(0.5)
        goToWaypoint(screenshot, waypoints[waypointIndex], coordinate)
        return
    if shouldRetrySameWaypoint:
        shouldRetrySameWaypoint = False
        player.stop(0.5)
        if(currentWaypoint['type'] == 'ramp'):
            waypointIndex = waypointIndex + 1
            currentWaypoint = waypoints[waypointIndex]
        goToWaypoint(screenshot, currentWaypoint, coordinate)


def healingObserver(healthPercentage, manaPercentage):
    percentageToHealWithManaPotion = 65
    percentageToHealWithPotion = 50
    percentageToHealWithSpell = 75
    spellHotkey = 'f1'
    manaPotionHotkey = 'f2'
    healthPotionHotkey = 'f3'
    shouldHealWithHealthPotion = healthPercentage < percentageToHealWithPotion
    if shouldHealWithHealthPotion:
        print('healing with health potion...')
        utils.press(healthPotionHotkey)
        time.sleep(0.25)
        return
    shouldHealWithMana = manaPercentage < percentageToHealWithManaPotion
    if shouldHealWithMana:
        print('healing with mana potion...')
        utils.press(manaPotionHotkey)
        time.sleep(0.25)
        return
    shouldHealWithSpell = healthPercentage < percentageToHealWithSpell or manaPercentage > 90
    if shouldHealWithSpell:
        print('healing with spell...')
        utils.press(spellHotkey)
        time.sleep(0.25)


def getWindow():
    targetWindowTitle = None
    allTitles = gw.getAllTitles()
    for title in allTitles:
        if title.startswith('Tibia -'):
            targetWindowTitle = title
    hasNoTargetWindowTitle = targetWindowTitle == None
    if hasNoTargetWindowTitle:
        return None
    windowTitles = gw.getWindowsWithTitle(targetWindowTitle)
    hasNoWindowsMatchingTitles = len(windowTitles) == 0
    if hasNoWindowsMatchingTitles:
        return None
    return windowTitles[0]


def handleWindow(_):
    global window
    windowIsEmpty = window is None
    if windowIsEmpty:
        window = getWindow()
    return window


def main():
    optimal_thread_count = multiprocessing.cpu_count()
    threadPoolScheduler = ThreadPoolScheduler(optimal_thread_count)
    thirteenFps = 0.0667
    fpsObserver = rx.interval(thirteenFps)
    fpsWithScreenshot = fpsObserver.pipe(
        operators.map(handleWindow),
        operators.filter(lambda window: window is not None),
        operators.map(lambda window: utils.getScreenshot(window)),
    )
    coordinatesObserver = fpsWithScreenshot.pipe(
        operators.map(lambda screenshot: [screenshot, radar.getCoordinate(screenshot)]),
    )
    coordinatesObserver.subscribe(lambda result: print(result[1]))
    battlelistObserver = coordinatesObserver.pipe(
        operators.map(lambda result: [result[0], result[1], battleList.getCreatures(result[0])]),
    )
    cavebotObserver = battlelistObserver.pipe(
        operators.filter(lambda result: len(result[2]) > 0 and not battleList.isAttackingCreature(result[2])),
        operators.subscribe_on(threadPoolScheduler)
    )
    cavebotObserver.subscribe(
        lambda result: handleCavebot(result[0], result[1], result[2])
    )
    waypointObserver = battlelistObserver.pipe(
        operators.filter(lambda result: len(result[2]) == 0),
        operators.subscribe_on(threadPoolScheduler)
    )
    waypointObserver.subscribe(lambda result: handleWaypoints(result))
    # healingObserver = fpsWithScreenshot.pipe(
    #     operators.map(lambda screenshot: (screenshot, player.getHealthPercentage(screenshot))),
    #     operators.map(lambda result: (result[1], player.getManaPercentage(result[0]))),
    #     operators.subscribe_on(threadPoolScheduler)
    # )
    # healingObserver.subscribe(lambda result: healing.healingObserver(result[0], result[1]))
    input("Press Enter key to exit...")


if __name__ == '__main__':
    main()
