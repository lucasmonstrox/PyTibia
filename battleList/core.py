import math
import numpy as np
from battleList import config, types
import utils.core
import utils.image


@utils.core.cacheObjectPos
def getContainerBottomBarPos(screenshot: types.UINT8_VECTOR) -> types.UINT8_VECTOR:
    return utils.core.locate(screenshot, config.container["bottomBarImg"])


@utils.core.cacheObjectPos
def getContainerTopBarPos(screenshot: types.UINT8_VECTOR) -> types.UINT8_VECTOR:
    return utils.core.locate(screenshot, config.container['topBarImg'])


def getContent(screenshot: types.UINT8_VECTOR) -> types.UINT8_VECTOR:
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


def getCreatureNameImg(slotImg: types.SLOT_IMG) -> types.CREATURE_NAME_IMG:
    creatureNameImg = slotImg[3:11 + 3, 23:23 + 131]
    creatureNameImg = utils.image.convertGraysToBlack(creatureNameImg)
    return creatureNameImg


def getCreatureSlotImg(content: types.UINT8_VECTOR, slot: int) -> types.SLOT_IMG:
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config.slot["height"] + config.slot["gap"])
    finishingY = startingY + config.slot["height"]
    slotImg = content[startingY:finishingY, :]
    return slotImg


# TODO: add unit tests
def getCreatureFromSlot(content: types.UINT8_VECTOR, slot: int) -> types.CREATURE:
    slotImg = getCreatureSlotImg(content, slot)
    isBeingAttacked = isCreatureBeingAttacked(slotImg)
    creatureNameImg = getCreatureNameImg(slotImg)
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    unknownCreature = not creatureNameImgHash in config.creatures["nameImgHashes"]
    if unknownCreature:
        return ("Unknown", isBeingAttacked)
    creatureName = config.creatures["nameImgHashes"][creatureNameImgHash]
    return (creatureName, isBeingAttacked)


# TODO: add unit tests
def getCreatures(screenshot: types.UINT8_VECTOR) -> types.CREATURE_LIST:
    content = getContent(screenshot)
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


def getFilledSlotsCount(content: types.UINT8_VECTOR) -> int:
    content = np.ravel(content[:, 23:24])
    contentOfBooleans = np.where(
        content == config.creatures["namePixelColor"], 1, 0)
    truePixelsIndexes = np.nonzero(contentOfBooleans)[0]
    hasNoFilledSlots = len(truePixelsIndexes) == 0
    if hasNoFilledSlots:
        return 0
    lastIndexOfTruePixelsIndexes = len(truePixelsIndexes) - 1
    lastTrueIndexOfPixelsIndexes = truePixelsIndexes[lastIndexOfTruePixelsIndexes]
    slotsCount = math.ceil(
        lastTrueIndexOfPixelsIndexes / (config.slot["height"] + config.slot["gap"]))
    return slotsCount


def isAttackingSomeCreature(creatures: types.CREATURE_LIST) -> bool:
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature


def isCreatureBeingAttacked(slotImg: types.SLOT_IMG) -> bool:
    attackColor = 76
    highlightedAttackColor = 166
    upperBorderOfCreatureIcon = slotImg[0:1, 0:19].flatten()
    isCreatureBeingAttacked = np.all(np.logical_or(
        upperBorderOfCreatureIcon == attackColor, upperBorderOfCreatureIcon == highlightedAttackColor))
    return isCreatureBeingAttacked


# TODO: add unit tests
def unhighlightName(creatureNameImg: types.UINT8_VECTOR) -> types.UINT8_VECTOR:
    unhighlightedName = np.where(
        creatureNameImg == config.creatures["highlightedNamePixelColor"],
        config.creatures["namePixelColor"],
        creatureNameImg
    )
    return unhighlightedName
