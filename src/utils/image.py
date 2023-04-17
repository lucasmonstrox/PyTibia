import cv2
from numba import njit
import numpy as np
from PIL import Image


@njit(cache=True, fastmath=True)
def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def RGBtoGray(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def loadFromRGBToGray(path):
    return np.array(RGBtoGray(load(path)), dtype=np.uint8)


def loadAsGrey(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE), dtype=np.uint8)


def save(arr, name):
    im = Image.fromarray(arr)
    im.save(name)


def crop(img, x, y, width, height):
    return img[y:y + height, x:x + width]


def load(path):
    return np.array(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), dtype=np.uint8)
