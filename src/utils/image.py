import cv2
from numba import njit
import numpy as np
from PIL import Image
from src.shared.typings import GrayImage


# TODO: add unit tests
@njit(cache=True, fastmath=True)
def convertGraysToBlack(arr: GrayImage) -> GrayImage:
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)


# TODO: add unit tests
# TODO: add typings
def RGBtoGray(image) -> GrayImage:
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# TODO: add unit tests
def loadFromRGBToGray(path: str) -> GrayImage:
    return np.array(RGBtoGray(load(path)), dtype=np.uint8)


# TODO: add unit tests
def save(arr: GrayImage, name: str):
    im = Image.fromarray(arr)
    im.save(name)


# TODO: add unit tests
def crop(img: GrayImage, x: int, y: int, width: int, height: int) -> GrayImage:
    return img[y:y + height, x:x + width]


# TODO: add unit tests
# TODO: add typings
def load(path: str):
    return np.array(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), dtype=np.uint8)
