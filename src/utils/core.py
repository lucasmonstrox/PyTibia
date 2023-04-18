import cv2
import dxcam
import numpy as np
import pyautogui
import random
import time
import xxhash


camera = dxcam.create(output_color='GRAY')


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def cacheObjectPosition(func):
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None
    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if lastX != None and lastY != None and lastW != None and lastH != None:
            copiedImg = screenshot[lastY:lastY + lastH, lastX:lastX + lastW]
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
        lastImg = screenshot[lastY:lastY + lastH, lastX:lastX + lastW]
        lastImgHash = hashit(lastImg)
        return (x, y, w, h)
    return inner


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getCenterOfBounds(bounds):
    (left, top, width, height) = bounds
    center = (left + width / 2, top + height / 2)
    return center


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getCoordinateFromPixel(pixel):
    x, y = pixel
    return x + 31744, y + 30976


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getPixelFromCoordinate(coordinate):
    x, y, _ = coordinate
    return x - 31744, y - 30976


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def hashit(arr):
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).intdigest()


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def hashitHex(arr):
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).hexdigest()


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
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


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def locateMultiple(compareImg, img, confidence=0.85):
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    resultList = []
    for pt in zip(*loc[::-1]):
        resultList.append((pt[0], pt[1], len(compareImg[0]), len(compareImg)))
    return resultList


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getScreenshot():
    global camera
    if not camera.is_capturing:
        camera.start(target_fps=240, video_mode=False)
    screenshot = camera.get_latest_frame()
    screenshotHeight = len(screenshot)
    screenshotWidth = len(screenshot[0])
    screenshotReshaped = np.array(screenshot, dtype=np.uint8).reshape((screenshotHeight, screenshotWidth))
    return screenshotReshaped


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def press(key, delay=150):
    pyautogui.keyDown(key)
    time.sleep(delay / 1000)
    pyautogui.keyUp(key)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def typeKeyboard(phrase):
    words = list(phrase)
    for word in words:
        time.sleep(random.randrange(70, 190) / 1000)
        press(word)
    time.sleep(random.randrange(70, 190) / 1000)
    press('enter')


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def randomCoord(x, y, width, height):
    x = random.randrange(x, x + width)
    y = random.randrange(y, y + height)
    return (x, y)
