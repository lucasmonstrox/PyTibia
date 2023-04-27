import cv2
import numpy as np
from PIL import Image
from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import hashit, locate


# TODO: add types
# TODO: add unit tests
def cacheChain(imageList):
    def decorator(_):
        lastX = None
        lastY = None
        lastW = None
        lastH = None
        lastImgHash = None
        def inner(screenshot: GrayImage) -> Union[BBox, None]:
            nonlocal lastX, lastY, lastW, lastH, lastImgHash
            if lastX != None and lastY != None and lastW != None and lastH != None:
                copiedImg = screenshot[lastY:lastY + lastH, lastX:lastX + lastW]
                copiedImgHash = hashit(copiedImg)
                if copiedImgHash == lastImgHash:
                    return (lastX, lastY, lastW, lastH)
            for image in imageList:
                imagePosition = locate(screenshot, image)
                if imagePosition is not None:
                    (x, y, w, h) = imagePosition
                    lastX = x
                    lastY = y
                    lastW = w
                    lastH = h
                    lastImg = screenshot[lastY:lastY + lastH, lastX:lastX + lastW]
                    lastImgHash = hashit(lastImg)
                    return (x, y, w, h)
            return None
        return inner
    return decorator


# TODO: add unit tests
def convertGraysToBlack(arr: np.ndarray) -> np.ndarray:
    return np.array(np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr), dtype=np.uint8)


# TODO: add unit tests
def RGBtoGray(image: np.ndarray) -> GrayImage:
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
def load(path: str) -> np.ndarray:
    return np.array(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), dtype=np.uint8)
