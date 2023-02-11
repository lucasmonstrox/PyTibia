import cv2
import numpy as np
from PIL import Image


def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def RGBtoGray(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return grayImage


def loadFromRGBToGray(path):
    loadedRgbImage = load(path)
    grayImage = RGBtoGray(loadedRgbImage)
    return grayImage


def loadAsGrey(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE), dtype=np.uint8)


def load(path):
    return np.array(cv2.imread(path), dtype=np.uint8)


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
