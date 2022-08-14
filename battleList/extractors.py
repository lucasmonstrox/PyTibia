import math
import numpy as np
from . import config, locators
import utils.core
import utils.image


def getContent(screenshot):
    containerTopBarPos = locators.getContainerTopBarPos(screenshot)
    cannotGetContainerTopBarPos = containerTopBarPos is None
    if cannotGetContainerTopBarPos:
        return None
    (contentLeft, contentTop, _, contentHeight) = containerTopBarPos
    startingY = contentTop + contentHeight
    endingX = contentLeft + config.container["dimensions"]["width"]
    content = screenshot[startingY:, contentLeft:endingX]
    containerBottomBarPos = locators.getContainerBottomBarPos(content)
    cannotGetContainerBottomBarPos = containerBottomBarPos is None
    if cannotGetContainerBottomBarPos:
        return None
    content = content[:containerBottomBarPos[1] - 11, :]
    return content


def getCreatureNameImg(slotImg):
    creatureNameImg = slotImg[3:11 + 3, 23:23 + 131]
    creatureNameImg = utils.image.convertGraysToBlack(creatureNameImg)
    return creatureNameImg


def getCreatureSlotImg(content, slot):
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config.slot["dimensions"]["height"] + config.slot["grid"]["gap"])
    finishingY = startingY + config.slot["dimensions"]["height"]
    slotImg = content[startingY:finishingY, :]
    utils.image.save(slotImg, "slotImg.png")
    return slotImg


def getFilledSlotsCount(content):
    content = np.ravel(content[:, 23:24])
    contentOfBooleans = np.where(
        np.logical_or(
            content == config.creatures["namePixelColor"],
            content == config.creatures["highlightedNamePixelColor"]
        ),
        1, 0)
    truePixelsIndexes = np.nonzero(contentOfBooleans)[0]
    hasNoFilledSlots = len(truePixelsIndexes) == 0
    if hasNoFilledSlots:
        return 0
    lastIndexOfTruePixelsIndexes = len(truePixelsIndexes) - 1
    lastTrueIndexOfPixelsIndexes = truePixelsIndexes[lastIndexOfTruePixelsIndexes]
    slotsCount = math.ceil(
        lastTrueIndexOfPixelsIndexes / (config.slot["dimensions"]["height"] + config.slot["grid"]["gap"]))
    return slotsCount


# TODO: add unit tests
def getUpperBorderOfCreatureIcon(slotImg):
    upperBorderOfCreatureIcon = slotImg[0:1, 0:19].flatten()
    return upperBorderOfCreatureIcon
