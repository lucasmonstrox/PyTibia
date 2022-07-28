import cv2
import numpy as np
import pytesseract
from PIL.Image import Image


def convertGraysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


def BGRtoGray(screenshot):
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    return screenshot


def RGBtoGray(screenshot):
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    return screenshot


def loadAsArray(path):
    return np.array(cv2.imread(path, cv2.IMREAD_GRAYSCALE))


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


def toString(screenshot, param):
    paramStr = '--oem 3 --psm ' + param
    messages = pytesseract.image_to_string(screenshot, lang=None, config=paramStr)
    return messages


def toTextData(image):
    return pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
