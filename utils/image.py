import cv2
import numpy as np
from PIL import Image


def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def RGBtoGray(screenshot):
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    return screenshot


def loadFromRGBToGray(path):
    img = RGBtoGray(load(path))
    return img


def loadAsGrey(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE))


def load(path):
    return np.array(cv2.imread(path))


def save(arr, name):
    im = Image.fromarray(arr)
    im.save(name)


def crop(img, x, y, width, height):
    return img[y:y + height, x:x + width]


def load(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def filterColorRange(image, upperBound, lowerBound):
    imagemask = cv2.inRange(image, np.array(lowerBound), np.array(upperBound))
    return imagemask
