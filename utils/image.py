import cv2
import numpy as np
from PIL.Image import Image


def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def loadAsArray(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE))


def save(arr, name):
    im = Image.fromarray(arr)
    im.save(name)
