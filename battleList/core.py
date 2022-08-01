import math
import numpy as np
from battleList import config, types
import utils.core, utils.image, utils.mouse


def attackSlot(screenshot, slot):
    pos = getContainerTopBarPos(screenshot)
    x = pos[0] + 20
    y = pos[1] + 13 + (slot * 22) + 22 // 2
    utils.mouse.leftClick(x, y)


@utils.core.cacheObjectPos
def getContainerBottomBarPos(img):
    return utils.core.locate(img, config.container["bottomBarImg"])


@utils.core.cacheObjectPos
def getContainerTopBarPos(img):
    return utils.core.locate(img, config.container['topBarImg'])


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


def getCreatureNameImg(slotImg):
    creatureNameImg = slotImg[3:11 + 3, 23:23 + 131]
    creatureNameImg = utils.image.convertGraysToBlack(creatureNameImg)
    return creatureNameImg


def getCreatureSlotImg(content, slot):
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config.slot["height"] + config.slot["gap"])
    finishingY = startingY + config.slot["height"]
    slotImg = content[startingY:finishingY, :]
    return slotImg


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


def getCreatures(screenshot):
    content = getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    contentIsTooSmall = content.shape[0] < config.slot["height"]
    if contentIsTooSmall:
        raise None
    content = unhighlightName(content)
    slotsCount = getSlotsCount(content)
    creatures = np.array([getCreatureFromSlot(content, creature)
                         for creature in np.arange(slotsCount)], dtype=types.creatureType)
    return creatures


def getSlotsCount(content):
    content = np.ravel(content[:, 23:24])
    possibleCreatureNames = np.nonzero(
        np.where(
            content == config.creatures["namePixelColor"],
            True,
            False
        )
    )[0]
    hasNoFilledSlots = len(possibleCreatureNames) == 0
    if hasNoFilledSlots:
        return 0
    lastCreatureIndex = possibleCreatureNames[len(possibleCreatureNames) - 1]
    filledSlots = math.ceil(
        lastCreatureIndex / (config.slot["height"] + config.slot["gap"]))
    return filledSlots


def isCreatureBeingAttacked(slotImg):
    upperCreatureBorder = slotImg[0:1, 0:19].flatten()
    isBeingAttacked = np.all(np.logical_or(
        upperCreatureBorder == 76, upperCreatureBorder == 166))
    return isBeingAttacked


def isAttackingSomeCreature(creatures):
    return np.any(creatures['isBeingAttacked'] == True)


def unhighlightName(creatureNameImg):
    return np.where(
        creatureNameImg == config.creatures["highlightedNamePixelColor"],
        config.creatures["namePixelColor"],
        creatureNameImg
    )
