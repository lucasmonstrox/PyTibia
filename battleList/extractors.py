import math
from numba import njit
import numpy as np
from . import config, locators


@njit(cache=True, fastmath=True)
def getBeingAttackedCreatures(content, filledSlotsCount):
    for i in range(filledSlotsCount):
        y = (i * 22)
        for j in range(19):
            bar = content[y, :19]
            if bar[j] != 76 and bar[j] != 166:
                break
            if j == 18:
                yield True
        if i < filledSlotsCount - 1:
            yield False
        

def getContent(screenshot):
    containerTopBarPos = locators.getContainerTopBarPos(screenshot)
    cannotGetContainerTopBarPos = containerTopBarPos is None
    if cannotGetContainerTopBarPos:
        return None
    (contentLeft, contentTop, _, contentHeight) = containerTopBarPos
    startingY = contentTop + contentHeight
    endingX = contentLeft + config.container['dimensions']['width']
    content = screenshot[startingY:, contentLeft:endingX]
    containerBottomBarPos = locators.getContainerBottomBarPos(content)
    cannotGetContainerBottomBarPos = containerBottomBarPos is None
    if cannotGetContainerBottomBarPos:
        return None
    content = content[:containerBottomBarPos[1] - 11, :]
    return content


@njit(cache=True, fastmath=True)
def getCreaturesNamesImages(content, filledSlotsCount):
    creaturesNamesImages = np.zeros((filledSlotsCount, 115), dtype=np.uint8)
    for i in range(filledSlotsCount):
        y = 11 + (i * 22)
        img = content[y:y + 1, 23:138][0]
        for j in range(img.shape[0]):
            if img[j] == 192 or img[j] == 247:
                creaturesNamesImages[i, j] = 192
    return creaturesNamesImages


@njit(cache=True, fastmath=True)
def getFilledSlotsCount(content):
    i = len(content[:, 23])
    while(i > 0):
        if content[:, 23][i - 1] == 192 or content[:, 23][i - 1] == 247:
            return math.ceil(i / 22)
        i = i - 1
    return 0
