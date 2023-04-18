import cv2
from numba import njit
import numpy as np
from PIL import Image


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@njit(cache=True, fastmath=True)
def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def RGBtoGray(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def loadFromRGBToGray(path):
    return np.array(RGBtoGray(load(path)), dtype=np.uint8)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def save(arr, name):
    im = Image.fromarray(arr)
    im.save(name)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def crop(img, x, y, width, height):
    return img[y:y + height, x:x + width]


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def load(path):
    return np.array(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), dtype=np.uint8)
