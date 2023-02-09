import math
from numba import njit
import numpy as np
from . import config, locators


@njit(cache=True, fastmath=True)
def getBeingAttackedCreatures(content, filledSlotsCount):
    beingAttackedCreatures = np.full((filledSlotsCount), False, dtype=np.bool_)
    size = 19
    for i in range(filledSlotsCount):
        y = (i * 22)
        border = content[y, :size]
        for j in range(size):
            if border[j] != 76 and border[j] != 166:
                break
            if j == 18:
                beingAttackedCreatures[i] = True
    return beingAttackedCreatures


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


@njit(cache=True, fastmath=True, nogil=True)
def getFilledSlotsCount(content):
    firstLetterPixels = content[:, 23]
    firstLetterPixelsFlatten = np.ravel(firstLetterPixels)
    booleanIndexes = np.logical_or(firstLetterPixelsFlatten == 192, firstLetterPixelsFlatten == 247)
    contentOfBooleans = np.flatnonzero(booleanIndexes)
    hasNoFilledSlots = len(contentOfBooleans) == 0
    if hasNoFilledSlots:
        return 0
    lastPaintedPixelIndex = contentOfBooleans[-1]
    slotsCount = lastPaintedPixelIndex / 22
    slotsCountRounded = math.ceil(slotsCount)
    return slotsCountRounded
