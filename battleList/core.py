import math
from nptyping import Int8, NDArray, Shape, Structure
import numpy as np
from typing import Any
from battleList import config, types
import utils.core
import utils.image
import utils.mouse


# TODO: add typings
# TODO: add unit tests
# TODO: improve clean code
def attackSlot(screenshot, slot):
    pos = getContainerTopBarPos(screenshot)
    x = pos[0] + config.slot['height']
    y = pos[1] + 13 + (slot * 22) + 22 // 2
    utils.mouse.leftClick(x, y)


# TODO: add typings
# TODO: add unit tests
@utils.core.cacheObjectPos
def getContainerBottomBarPos(img):
    return utils.core.locate(img, config.container["bottomBarImg"])


# TODO: add typings
# TODO: add unit tests
@utils.core.cacheObjectPos
def getContainerTopBarPos(img):
    return utils.core.locate(img, config.container['topBarImg'])


# TODO: add typings
# TODO: add unit tests
# TODO: improve clean code
def getContent(screenshot):
    containerTopBarPos = getContainerTopBarPos(screenshot)
    cannotGetContainerTopBarPos = containerTopBarPos is None
    if cannotGetContainerTopBarPos:
        return None
    (contentLeft, contentTop, _, contentHeight) = containerTopBarPos
    startingY = contentTop + contentHeight
    endingX = contentLeft + config.container["width"]
    content = screenshot[startingY:, contentLeft:endingX]
    containerBottomBarPos = getContainerBottomBarPos(content)
    cannotGetContainerBottomBarPos = containerBottomBarPos is None
    if cannotGetContainerBottomBarPos:
        return None
    content = content[:containerBottomBarPos[1] - 11, :]
    return content


# TODO: add typings
# TODO: add unit tests
# TODO: improve clean code
def getCreatureNameImg(slotImg):
    creatureNameImg = slotImg[3:11 + 3, 23:23 + 131]
    creatureNameImg = utils.image.convertGraysToBlack(creatureNameImg)
    return creatureNameImg


def getCreatureSlotImg(content: NDArray[Any, Int8], slot: int) -> NDArray[Shape["20, 156"], Int8]:
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config.slot["height"] + config.slot["gap"])
    finishingY = startingY + config.slot["height"]
    slotImg = content[startingY:finishingY, :]
    return slotImg


# TODO: add typings
# TODO: add unit tests
def getCreatureFromSlot(content, slot):
    slotImg = getCreatureSlotImg(content, slot)
    isBeingAttacked = isCreatureBeingAttacked(slotImg)
    creatureNameImg = getCreatureNameImg(slotImg)
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    unknownCreature = not creatureNameImgHash in config.creatures["nameImgHashes"]
    if unknownCreature:
        return ("Unknown", isBeingAttacked)
    creatureName = config.creatures["nameImgHashes"][creatureNameImgHash]
    return (creatureName, isBeingAttacked)


# TODO: add typings
# TODO: add unit tests
def getCreatures(screenshot):
    content = getContent(screenshot)
    utils.image.save(content, 'content.png')
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    contentTooSmall = content.shape[0] < config.slot["height"]
    if contentTooSmall:
        return None
    content = unhighlightName(content)
    slotsCount = getFilledSlotsCount(content)
    creatures = np.array([getCreatureFromSlot(content, creature)
                         for creature in np.arange(slotsCount)], dtype=types.creatureType)
    return creatures


# TODO: add typings
# TODO: add unit tests
# TODO: improve clean code
def getFilledSlotsCount(content):
    content = np.ravel(content[:, 23:24])
    paintedPixelsIndexes = np.nonzero(
        np.where(
            content == config.creatures["namePixelColor"],
            True,
            False
        )
    )[0]
    hasNoFilledSlots = len(paintedPixelsIndexes) == 0
    if hasNoFilledSlots:
        return 0
    lastCreatureIndex = paintedPixelsIndexes[len(paintedPixelsIndexes) - 1]
    slotsCount = math.ceil(
        lastCreatureIndex / (config.slot["height"] + config.slot["gap"]))
    return slotsCount


def isAttackingSomeCreature(creatures: NDArray[Any, Structure["name: Str, isBeingAttacked: Bool"]]) -> bool:
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature


def isCreatureBeingAttacked(slotImg: NDArray[Shape["20, 156"], Int8]) -> bool:
    attackColor = 76
    highlightedAttackColor = 166
    upperBorderOfCreatureIcon = slotImg[0:1, 0:19].flatten()
    isCreatureBeingAttacked = np.all(np.logical_or(
        upperBorderOfCreatureIcon == attackColor, upperBorderOfCreatureIcon == highlightedAttackColor))
    return isCreatureBeingAttacked


# TODO: add typings
# TODO: add unit tests
def unhighlightName(creatureNameImg):
    unhighlightedName = np.where(
        creatureNameImg == config.creatures["highlightedNamePixelColor"],
        config.creatures["namePixelColor"],
        creatureNameImg
    )
    return unhighlightedName
