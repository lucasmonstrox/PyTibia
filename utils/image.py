import cv2
import numpy as np


def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def loadAsArray(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE))