from player import player
import asyncio
import pyautogui
import rx
import numpy as np
# from radar import radar
from time import sleep, time
from PIL import Image
# from rx.subject import Subject
from threading import Thread
# from player import WindowCapture

waypoints = [
    # # 0
    # {
    #     "type": "floor",
    #     "coordinate": (33121, 32837, 7),
    #     "walkType": "screen"
    # },
    # # 1
    # {
    #     "type": "floor",
    #     "coordinate": (33122, 32837, 7),
    #     "walkType": "screen"
    # },
    # # 2
    # {
    #     "type": "floor",
    #     "coordinate": (33117, 32833, 7),
    #     "walkType": "screen"
    # },
    # {
    #     "type": "floor",
    #     "coordinate": (33085, 32788, 7),
    #     "walkType": "radar"
    # },
    # # 3
    # {
    #     "type": "stairs",
    #     "coordinate": (33085, 32786, 6),
    #     "direction": "up"
    # },
    # # 4
    # {
    #     "type": "floor",
    #     "coordinate": (33085, 32785, 6),
    #     "walkType": "screen"
    # },
    # # 5
    # {
    #     "type": "stairs",
    #     "coordinate": (33085, 32783, 6),
    #     "direction": "up"
    # },
    # # 6
    # {
    #     "type": "floor",
    #     "coordinate": (33038, 32810, 7),
    #     "walkType": "radar"
    # },
    # # 7
    # {
    #     "type": "stairs",
    #     "coordinate": (33038, 32808, 6),
    #     "direction": "up"
    # },
    # # 8
    # {
    #     "type": "floor",
    #     "coordinate": (33033, 32801, 6),
    #     "walkType": "radar"
    # },
    # # 9
    # {
    #     "type": "stairs",
    #     "coordinate": (33033, 32799, 6),
    #     "direction": "up"
    # },
    # # 10
    # {
    #     "type": "floor",
    #     "coordinate": (33032, 32779, 6),
    #     "walkType": "radar"
    # },
    # # 11
    # {
    #     "type": "stairs",
    #     "coordinate": (33032, 32777, 4),
    #     "direction": "up"
    # },
    # # 12
    # {
    #     "type": "floor",
    #     "coordinate": (33032, 32786, 4),
    #     "walkType": "radar"
    # },
    # # 13
    # {
    #     "type": "stairs",
    #     "coordinate": (33032, 32788, 3),
    #     "direction": "down"
    # },
    # # 14
    # {
    #     "type": "floor",
    #     "coordinate": (33031, 32788, 3),
    #     "walkType": "radar"
    # },
    # # 15
    # {
    #     "type": "stairs",
    #     "coordinate": (33029, 32788, 2),
    #     "direction": "left"
    # },
    # # 16
    # {
    #     "type": "floor",
    #     "coordinate": (33029, 32781, 2),
    #     "walkType": "radar"
    # },
    # # 17
    # {
    #     "type": "stairs",
    #     "coordinate": (33029, 32779, 1),
    #     "direction": "up"
    # },
    # # 18
    # {
    #     "type": "floor",
    #     "coordinate": (33029, 32776, 1),
    #     "walkType": "radar"
    # },
    # # 19
    # {
    #     "type": "stairs",
    #     "coordinate": (33029, 32774, 0),
    #     "direction": "up"
    # },
    # # 20
    # {
    #     "type": "floor",
    #     "coordinate": (33030, 32756, 0),
    #     "walkType": "radar"
    # },
    # # 21
    # {
    #     "type": "stairs",
    #     "coordinate": (33032, 32756, 1),
    #     "direction": "right"
    # },
    # # 22
    # {
    #     "type": "floor",
    #     "coordinate": (33021, 32746, 0),
    #     "walkType": "radar"
    # },
    # # 23
    # {
    #     "type": "stairs",
    #     "coordinate": (33019, 32746, 2),
    #     "direction": "left"
    # },
    # # 24
    # {
    #     "type": "floor",
    #     "coordinate": (33016, 32745, 2),
    #     "walkType": "radar"
    # },
    # # 25
    # {
    #     "type": "stairs",
    #     "coordinate": (33016, 32743, 3),
    #     "direction": "up"
    # },
    # # 26
    # {
    #     "type": "floor",
    #     "coordinate": (33010, 32727, 3),
    #     "walkType": "radar"
    # },
    # # 27
    # {
    #     "type": "stairs",
    #     "coordinate": (33010, 32725, 4),
    #     "direction": "up"
    # },
    # # 28
    # {
    #     "type": "floor",
    #     "coordinate": (32999, 32703, 4),
    #     "walkType": "radar"
    # },
    # # 29
    # {
    #     "type": "stairs",
    #     "coordinate": (32999, 32705, 5),
    #     "direction": "down"
    # },
    # # 30
    # {
    #     "type": "floor",
    #     "coordinate": (32998, 32709, 5),
    #     "walkType": "radar"
    # },
    # # 31
    # {
    #     "type": "stairs",
    #     "coordinate": (32998, 32711, 4),
    #     "direction": "down"
    # },
    # # 32
    # {
    #     "type": "floor",
    #     "coordinate": (32982, 32715, 6),
    #     "walkType": "radar"
    # },
    # # 33
    # {
    #     "type": "stairs",
    #     "coordinate": (32982, 32717, 7),
    #     "direction": "down"
    # },
    # # 34
    # {
    #     "type": "floor",
    #     "coordinate": (32958, 32760, 7),
    #     "walkType": "radar"
    # },
    # # 35
    # {
    #     "type": "floor",
    #     "coordinate": (32951, 32785, 7),
    #     "walkType": "radar"
    # },
    # # 36
    # {
    #     "type": "floor",
    #     "coordinate": (33004, 32750, 7),
    #     "walkType": "radar"
    # },
    # # 37
    # {
    #     "type": "stairs",
    #     "coordinate": (33006, 32750, 7),
    #     "direction": "right"
    # },
    # # 38
    # {
    #     "type": "floor",
    #     "coordinate": (33015, 32749, 6),
    #     "walkType": "radar"
    # },
    # # 39
    # {
    #     "type": "stairs",
    #     "coordinate": (33015, 32751, 5),
    #     "direction": "down"
    # },
    # # 40
    # {
    #     "type": "stairs",
    #     "coordinate": (33015, 32753, 4),
    #     "direction": "down"
    # },
    # # 41
    # {
    #     "type": "floor",
    #     "coordinate": (33009, 32770, 4),
    #     "walkType": "radar"
    # },
    # # 42
    # {
    #     "type": "stairs",
    #     "coordinate": (33009, 32772, 5),
    #     "direction": "down"
    # },
    # # 43
    # {
    #     "type": "floor",
    #     "coordinate": (33004, 32765, 5),
    #     "walkType": "radar"
    # },
    # # 44
    # {
    #     "type": "stairs",
    #     "coordinate": (33004, 32767, 5),
    #     "direction": "down"
    # },
    # # 45
    # {
    #     "type": "floor",
    #     "coordinate": (33004, 32770, 6),
    #     "walkType": "radar"
    # },
    # # 46
    # {
    #     "type": "stairs",
    #     "coordinate": (33004, 32772, 7),
    #     "direction": "down"
    # },
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

currentWaypointIndex = 0

battleListPos = None

def getBattleListPos():
    global battleListPos
    # TODO: cache it if window coordinates doesn't change
    if battleListPos == None:
        battleListPos = pyautogui.locateOnScreen('player/images/battlelist.png')
    return battleListPos

def isAttacking():
    global getBattleListPos
    battleListPos = getBattleListPos()
    left = battleListPos.left
    top = battleListPos.top
    width = battleListPos.width
    battleContainerImg = pyautogui.screenshot(region=(left, top, width, 300))
    leftRedPos = pyautogui.locate('player/images/MonstersAttack/LeftRed.png', battleContainerImg, confidence=0.9)
    isAttackingRed = leftRedPos != None
    if isAttackingRed:
        return True
    leftPinkPos = pyautogui.locate('player/images/MonstersAttack/LeftPink.png', battleContainerImg, confidence=0.9)
    isAttackingPink = leftPinkPos != None
    if isAttackingPink:
        return True
    return False

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
        global currentWaypointIndex, isAttackingMonsters, shouldRetryWaypoint, isAttacking, trackWaypointObserver, waypoints
        if isAttackingMonsters:
            return
        currentCoordinateX, currentCoordinateY, currentCoordinateZ = currentCoordinate
        isLastWaypoint = currentWaypointIndex + 1 >= len(waypoints) - 1
        nextWaypointIndex = 0 if isLastWaypoint else currentWaypointIndex + 1
        if shouldRetryWaypoint:
            shouldRetryWaypoint = False
            observer.on_next(waypoints[nextWaypointIndex])
            return
        nextWaypointX, nextWaypointY, nextWaypointZ = waypoints[currentWaypointIndex + 1]['coordinate']
        isSameWaypoint = currentCoordinateX == nextWaypointX and currentCoordinateY == nextWaypointY
        if isSameWaypoint:
            currentWaypointIndex = nextWaypointIndex
            nextIndex = 0 if isLastWaypoint else currentWaypointIndex + 1
            observer.on_next(waypoints[nextIndex])
    
    # TODO: add pipe to avoid observer when player is attacking monsters    
    trackWaypointObserver.subscribe(
        lambda waypoint: markWaypointInner(waypoint),
    )

markWaypointObserver = rx.create(markWaypointObservable)

def walk(waypoint):
    if waypoint['type'] == 'floor':
        if waypoint['walkType'] == 'radar':
            player.goToCoordinateByRadarClick(waypoint['coordinate'])
            return
        if waypoint['walkType'] == 'screen':
            player.goToCoordinateByScreenClick(waypoint['coordinate'])
            return
        return
    if waypoint['type'] == 'stairs':
        sleep(0.5)
        pyautogui.press(waypoint['direction'])

def getBattleListSlotPos(battleListPos, index):
    index = index - 1
    x = battleListPos.left + 4
    y = (battleListPos.top + battleListPos.height) + (index * 21)
    if index > 0:
        y = y + index
    return (x, y)

def getMonsterHashFromArray(imgAsArray):
    monster = np.where(np.logical_and(imgAsArray >= [50, 50, 50], imgAsArray <= [100, 100, 100]), [0, 0, 0], imgAsArray)
    return hash(monster.tobytes())

def getMonsterHashByImg(img):
    monster = np.array(img)
    monster = getMonsterHashFromArray(monster)
    return monster

monstersHashes = {
    getMonsterHashByImg(Image.open('monsters/images/battlelist/centipede.png').convert('RGB')): { "name": "Centipede" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/cobra.png').convert('RGB')): { "name": "Cobra" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/crocodile.png').convert('RGB')): { "name": "Crocodile" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/lizard-sentinel.png').convert('RGB')): { "name": "Lizard Sentinel" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/lizard-snakecharmer.png').convert('RGB')): { "name": "Lizard Snakecharmer" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/lizard-templar.png').convert('RGB')): { "name": "Lizard Templar" },
    getMonsterHashByImg(Image.open('monsters/images/battlelist/spit-nettle.png').convert('RGB')): { "name": "Spit Nettle" }
}

shouldRetryWaypoint = True

async def getMonsterBySlot(battleListPos, screenshot, slot):
    index = slot - 1
    x = 0
    y = (index * 21)
    if index > 0:
        y = y + index
    imgAsArray = screenshot[y:y + 21]
    monsterHash = getMonsterHashFromArray(imgAsArray)
    invalidMonster = not monsterHash in monstersHashes
    if invalidMonster:
        return None
    monster = monstersHashes[monsterHash]
    monster = { "monster": monster, "coordinate": (battleListPos.left + 11, battleListPos.top + battleListPos.height + y + 10)}
    return monster

async def getBattleListMonsters():
    battleListPos = getBattleListPos()
    x = battleListPos.left + 4
    y = (battleListPos.top + battleListPos.height)
    screenshot = np.array(
        pyautogui.screenshot(region=(x, y, 22, 196))
    )
    possibleMonsters = await asyncio.gather(
        getMonsterBySlot(battleListPos, screenshot, 1),
        getMonsterBySlot(battleListPos, screenshot, 2),
        getMonsterBySlot(battleListPos, screenshot, 3),
        getMonsterBySlot(battleListPos, screenshot, 4),
        getMonsterBySlot(battleListPos, screenshot, 5),
        getMonsterBySlot(battleListPos, screenshot, 6),
        getMonsterBySlot(battleListPos, screenshot, 7),
        getMonsterBySlot(battleListPos, screenshot, 8),
        getMonsterBySlot(battleListPos, screenshot, 9),
    )
    monsters = np.array([])
    for monster in possibleMonsters:
        if monster == None:
            continue
        monsters = np.append(monsters, monster)
    return monsters

def walkingScanner():
    markWaypointObserver.subscribe(
        lambda waypoint: walk(waypoint),
    )

isAttackingMonsters = False

def attackingScanner():
    async def inner():
        global isAttackingMonsters, shouldRetryWaypoint
        while True:
            isAttackingMonsters = isAttacking()
            if isAttackingMonsters:
                continue
            monsters = await getBattleListMonsters()
            hasNoMonstersToAttack = len(monsters) == 0
            if hasNoMonstersToAttack:
                continue
            pyautogui.press('esc')
            sleep(0.5)
            x, y = monsters[0]['coordinate']
            pyautogui.click(x + 30, y)
            pyautogui.moveTo(x - 100, y - 100)
            shouldRetryWaypoint = True
    asyncio.run(inner())
  
def main():
    # loop_time = time()
    # while True:
    #     print(player.getCoordinate())
    #     # print(asyncio.run(getBattleListMonsters()))
    #     timef = (time() - loop_time)
    #     timef = timef if timef else 1
    #     print('FPS {}'.format(1 / timef))
    #     print('  ')
    #     print('  ')
    #     print('  ')
    #     loop_time = time()
        # print("Elapsed time:", t1_stop, t1_start)
    # player.goToCoordinate((33094, 32790, 7))
    # player.goToCoordinateByScreenClick((33094, 32790, 7))
    # player.goToCoordinateByRadarClick((33094, 32790, 7))
    attackingScannerThread = Thread(target=attackingScanner)
    attackingScannerThread.start()
    walkingScannerThread = Thread(target=walkingScanner)
    walkingScannerThread.start()

if __name__ == '__main__':
    main()