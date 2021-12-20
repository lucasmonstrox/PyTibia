import d3dshot
import cupy as cp
import cv2
import numpy as np
from PIL import Image
import pygetwindow as gw
import xxhash

d3 = d3dshot.create(capture_output='numpy')


def cacheObjectPos(func):
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if(lastX != None and lastY != None and lastW != None and lastH != None):
            copiedImg = np.ascontiguousarray(screenshot[lastY:lastY +
                                                        lastH, lastX:lastX + lastW])
            copiedImgHash = hashit(copiedImg)
            if copiedImgHash == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        (x, y, w, h) = func(screenshot)
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
    center = (bounds.left + bounds.width / 2, bounds.top + bounds.height / 2)
    return center

# def getCenterOfBounds(bounds):
#     (left, top, width, height) = bounds
#     center = (left + width / 2, top + height / 2)
#     return center


def getCoordinateFromPixel(pixel):
    x, y = pixel
    return (x + 31744, y + 30976)


def getPixelFromCoordinate(coordinate):
    x, y, _ = coordinate
    return (y - 30976, x - 31744)


def getSquareMeterSize():
    return 51.455


def graysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def hashit(arr):
    return xxhash.xxh64(np.ascontiguousarray(arr)).intdigest()


def locate(compareImg, img):
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    (x, y) = res[3]
    width = len(img[0])
    height = len(img)
    return (x, y, width, height)


def getScreenshot():
    window = gw.getWindowsWithTitle('Tibia - ADM')[0]
    region = (window.top, window.left, window.width - 15, window.height)
    screenshot = d3.screenshot(region=region)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = np.array(screenshot)
    return screenshot


def saveImg(arr, name):
    im = Image.fromarray(arr)
    im.save(name)
