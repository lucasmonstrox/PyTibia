import cv2
import numpy as np
import pyautogui
import random
import time
from time import sleep
import xxhash
import dxcam


camera = dxcam.create()


def cacheObjectPos(func):
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if lastX != None and lastY != None and lastW != None and lastH != None:
            copiedImg = np.ascontiguousarray(screenshot[lastY:lastY +
                                                              lastH, lastX:lastX + lastW])
            copiedImgHash = hashit(copiedImg)
            if copiedImgHash == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        res = func(screenshot)
        didntMatch = res is None
        if didntMatch:
            return None
        (x, y, w, h) = res
        lastX = x
        lastY = y
        lastW = w
        lastH = h
        lastImg = np.ascontiguousarray(
            screenshot[lastY:lastY + lastH, lastX:lastX + lastW])
        lastImgHash = hashit(lastImg)
        return (x, y, w, h)

    return inner


def getCenterOfBounds(bounds):
    (left, top, width, height) = bounds
    center = (left + width / 2, top + height / 2)
    return center


def getCoordinateFromPixel(pixel):
    x, y = pixel
    return x + 31744, y + 30976


def getPixelFromCoordinate(coordinate):
    x, y, _ = coordinate
    return x - 31744, y - 30976


def getSquareMeterSize():
    return 51.455


def hashit(arr):
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).intdigest()


def hashitHex(arr):
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).hexdigest()


def locate(compareImg, img, confidence=0.85):
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    matchConfidence = res[1]
    didntMatch = matchConfidence <= confidence
    if didntMatch:
        return None
    (x, y) = res[3]
    width = len(img[0])
    height = len(img)
    return x, y, width, height


def locateMultiple(compareImg, img, confidence=0.85):
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    resultList = []
    for pt in zip(*loc[::-1]):
        resultList.append((pt[0], pt[1], len(compareImg[0]), len(compareImg)))
    return resultList


def getScreenshot():
    if not camera.is_capturing:
        camera.start(target_fps=60, video_mode=True)
    screenshot = camera.get_latest_frame()
    screenshot = np.array(screenshot)
    return screenshot


def stopScreenshotCamera():
    camera.stop()
    camera.release()


def press(key, delay=150):
    pyautogui.keyDown(key)
    sleep(delay / 1000)
    pyautogui.keyUp(key)


def typeKeyboard(phrase):
    words = list(phrase)
    for word in words:
        time.sleep(random.randrange(70, 190) / 1000)
        press(word)
    time.sleep(random.randrange(70, 190) / 1000)
    press('enter')


def randomCoord(x, y, width, height):
    x = random.randrange(x, x + width)
    y = random.randrange(y, y + height)
    return (x, y)
