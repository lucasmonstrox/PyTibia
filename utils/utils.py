#import cupy as cp
import cv2
import numpy as np
from PIL import Image


def cacheObjectPos(func):
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if(lastX != None and lastY != None and lastW != None and lastH != None):
            copiedImg = screenshot[lastY:lastY +
                                   lastH, lastX:lastX + lastW]
            copiedImgHash = hash(copiedImg.tostring())
            if copiedImgHash == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        (x, y, w, h) = func(screenshot)
        lastX = x
        lastY = y
        lastW = w
        lastH = h
        lastImgHash = hash(
            screenshot[lastY:lastY + lastH, lastX:lastX + lastW].tobytes())
        return (x, y, w, h)
    return inner


def getCenterOfBounds(bounds):
    center = (bounds.left + bounds.width / 2, bounds.top + bounds.height / 2)
    return center

# def getCenterOfBounds(bounds):
#     (left, top, width, height) = bounds
#     center = (left + width / 2, top + height / 2)
#     return center

# def getCoordinateFromPixel(pixel):
#     x, y = pixel
#     return (x + 31744, y + 30976)


def getCoordinateFromPixel(pixel):
    y, x = pixel
    return (x + 31744, y + 30976)


def getPixelFromCoordinate(coordinate):
    x, y, z = coordinate
    return (y - 30976, x - 31744)


def getSquareMeterSize():
    return 51.455


def graysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def locate(compareImg, img):
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    (left, top) = res[3]
    width = len(img[0])
    height = len(img)
    return (left, top, width, height)


#def saveCpImg(cpArray, name):
#    npArray = cp.asnumpy(cpArray)
#    im = Image.fromarray(npArray)
#    im.save(name)


def saveImg(arr, name):
    im = Image.fromarray(arr)
    im.save(name)
