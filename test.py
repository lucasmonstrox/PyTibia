from mss import mss
import win32con
import win32ui
import win32gui
import cv2 as cv
# import cupy as cp
from player import player
from radar import radar
import asyncio
import pyautogui
import rx
import numpy as np
from utils import utils
from time import sleep, time
from PIL import Image
from threading import Thread
from skimage import data
from skimage.feature import match_template
from PIL import ImageGrab
from numba import cuda, jit
from timeit import default_timer as timer
from PIL import Image

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

currentWaypointIndex = 0

battleListPos = None

battleListImg = np.array(cv.imread('player/images/battlelist.png'))


def getBattleListPos(screenshot):
    global battleListPos
    # TODO: cache it if window coordinates doesn't change
    return utils.locate(battleListImg, screenshot)


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

# TODO: cancel this function when player start attacking


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


def getBattleListSlotPos(battleListPos, index):
    index = index - 1
    x = battleListPos.left + 4
    y = (battleListPos.top + battleListPos.height) + (index * 21)
    if index > 0:
        y = y + index
    return (x, y)


def getMonsterHashFromArray(monster):
    monster = np.where(np.logical_and(monster >= [50, 50, 50], monster <= [
                       100, 100, 100]), [0, 0, 0], monster)
    monster = np.where(monster == [255, 0, 0], [0, 0, 0], monster)
    monster = np.where(monster == [255, 128, 128], [0, 0, 0], monster)
    monster = np.where(monster == [255, 255, 255], [0, 0, 0], monster)
    return hash(monster.tobytes())


def getMonsterHashByImg(img):
    monster = np.array(img)
    monster = getMonsterHashFromArray(monster)
    return monster


monstersHashes = {
}

shouldRetryWaypoint = True


async def getMonsterBySlot(battleListPos, screenshot, slot):
    index = slot - 1
    x = 0
    y = (index * 21)
    if index > 0:
        y = y + index
    monster = screenshot[y:y + 21]
    # TODO: improve this adding sugar syntax
    isBeingAttacked = (monster[0][0][0] == 255 and monster[0][0][1] == 0 and monster[0][0][2] == 0) or (
        monster[0][0][0] == 255 and monster[0][0][1] == 128 and monster[0][0][2] == 128)
    monsterHash = getMonsterHashFromArray(monster)
    invalidMonster = not monsterHash in monstersHashes
    if invalidMonster:
        return None
    monster = monstersHashes[monsterHash]
    monster = {
        "monster": monster,
        "isBeingAttacked": isBeingAttacked,
        "coordinate": (battleListPos.left + 11, battleListPos.top + battleListPos.height + y + 10)
    }
    return monster


async def getBattleListCreatures(screenshot):
    (left, top) = getBattleListPos(screenshot)
    x = left + 4
    y = (top + battleListPos.height)
    screenshot = screenshot[y:y + 196, x:x + 22]
    im = Image.fromarray(screenshot)
    im.save("gui.png")
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
    markWaypointObserver = rx.create(markWaypointObservable)
    markWaypointObserver.subscribe(
        lambda waypoint: walk(waypoint),
    )


isAttackingMonsters = False


def attackingScanner():
    async def inner():
        global isAttackingMonsters, shouldRetryWaypoint
        while True:
            monsters = await getBattleListCreatures()
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


class WindowCapture:
    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None):
        # find the handle for the window we want to capture.
        # if no window name is given, capture the entire screen
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):
        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj,
                   (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[..., :3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img[..., ::-1]

    def get_borderless_screenshot_at(self, x1, y1, x2, y2):
        sizeX = x2-x1
        sizeY = y2-y1

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, sizeX, sizeY)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (sizeX, sizeY), dcObj, (x1, y1), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (sizeY, sizeX, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[..., :3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img


def getScreenshot(sct):
    window = WindowCapture('Tibia - ADM')
    mon = {
        'top': window.offset_y,
        'left': window.offset_x,
        'width': window.w,
        'height': window.h
    }
    screenshot = sct.grab(mon)
    screenshot = np.array(screenshot)
    screenshot = screenshot[..., :3]
    screenshot = screenshot[..., ::-1]
    return screenshot


# floorImg = np.array(cv.imread('floor-7x.png'))
# grayFloorImg = cv.cvtColor(floorImg, cv.COLOR_RGB2GRAY)


def main():
    loop_time = time()
    sct = mss()
    screenshot = np.array(cv.imread('screenshot.png'))
    # while True:
    #     # screenshot = getScreenshot(sct)
    #     # im = Image.fromarray(screenshot)
    #     # im.save("screenshot.png")
    #     # break
    #     # radar.getCoordinate(screenshot)
    #     # print(radar.getRadarToolsPos(screenshot))
    #     # img = np.array(cv.imread('teste.png'))
    #     # grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #     # print(utils.locate(grayImg, grayFloorImg))
    #     timef = (time() - loop_time)
    #     timef = timef if timef else 1
    #     fps = 1 / timef
    #     print('FPS {}'.format(fps))
    #     loop_time = time()
    # attackingScannerThread = Thread(target=attackingScanner)
    # attackingScannerThread.start()
    walkingScannerThread = Thread(target=walkingScanner)
    walkingScannerThread.start()


if __name__ == '__main__':
    main()
