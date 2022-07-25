
import math
import numpy as np
import pyautogui
import utils.core, utils.image
from wiki.creatures import creatures

config = {
    "container": {
        "topImg": utils.image.loadAsArray('battleList/images/battleList.png'),
        "bottomImg": utils.image.loadAsArray('battleList/images/endOfContainer.png'),
        "width": 156
    },
    "creatures": {
        "namePixelColor": 192,
        "highlightedNamePixelColor": 247,
        "hashes": {}
    },
    "slot": {
        "height": 20,
        "gap": 2
    },
}


for creatureName in creatures:
    creatureImg = utils.image.loadAsArray(
        'battleList/images/monsters/{}.png'.format(creatureName))
    creatureHash = utils.core.hashit(creatureImg)
    config["creatures"]["hashes"][creatureHash] = {
        "name": creatureName,
        "hash": creatureHash,
        "info": creatures[creatureName]
    }


def attackSlot(screenshot, slot):
    pos = getContainerTop(screenshot)
    x = pos[0] + 20
    y = pos[1] + 13 + (slot * 22) + 22 // 2
    pyautogui.click(x, y)


@utils.core.cacheObjectPos
def getContainerBottom(img):
    return utils.core.locate(img, config["container"]["bottomImg"])


@utils.core.cacheObjectPos
def getContainerTop(img):
    return utils.core.locate(img, config["container"]["topImg"])


def getContent(screenshot):
    containerTop = getContainerTop(screenshot)
    cannotGetContainerTop = containerTop is None
    if cannotGetContainerTop:
        return None
    (contentLeft, contentTop, _, contentHeight) = containerTop
    startingY = contentTop + contentHeight
    endingX = contentLeft + config["container"]["width"]
    content = screenshot[startingY:, contentLeft:endingX]
    containerBottom = getContainerBottom(content)
    content = content[:containerBottom[1] - 11, :]
    return content


def getCreatureNameImg(slotImg):
    # TODO: improve clean code
    return slotImg[3:11 + 3, 23:23 + 131]


def getCreatureSlotImg(content, slot):
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config["slot"]["height"] + config["slot"]["gap"])
    finishingY = startingY + config["slot"]["height"]
    slotImg = content[startingY:finishingY, :]
    return slotImg


# TODO: get creature life
def getCreatureFromSlot(content, slot):
    slotImg = getCreatureSlotImg(content, slot)
    upperCreatureBorder = slotImg[0:1, 0:19].flatten()
    isBeingAttacked = np.all(np.logical_or(
        upperCreatureBorder == 76, upperCreatureBorder == 166))
    # TODO: apply it once when parsing content
    slotImg = utils.image.convertGraysToBlack(slotImg)
    creatureNameImg = getCreatureNameImg(slotImg)
    creatureNameImg = np.ravel(creatureNameImg)
    creatureHash = utils.core.hashit(creatureNameImg)
    unknownCreature = not creatureHash in config["creatures"]["hashes"]
    creatureName = "Unknown" if unknownCreature else config[
        "creatures"]["hashes"][creatureHash]["name"]
    return (creatureName, isBeingAttacked, 100)


def getCreatures(screenshot):
    content = getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    contentIsTooSmall = content.shape[0] < config["slot"]["height"]
    if contentIsTooSmall:
        raise None
    content = unhighlightName(content)
    filledSlots = getFilledSlots(content)
    creatureType = np.dtype([('name', np.str_, 64), ('isBeingAttacked', np.bool_), ('life', np.int8)])
    creatures = np.array([getCreatureFromSlot(content, creature)
                         for creature in np.arange(filledSlots)], dtype=creatureType)
    return creatures


def getFilledSlots(content):
    content = np.ravel(content[:, 23:24])
    possibleCreatureNames = np.nonzero(
        np.where(
            content == config["creatures"]["namePixelColor"],
            True,
            False
        )
    )[0]
    hasNoFilledSlots = len(possibleCreatureNames) == 0
    if hasNoFilledSlots:
        return 0
    lastCreatureIndex = possibleCreatureNames[len(possibleCreatureNames) - 1]
    filledSlots = math.ceil(
        lastCreatureIndex / (config["slot"]["height"] + config["slot"]["gap"]))
    return filledSlots


def isAttackingCreature(creatures):
    return np.any(creatures['isBeingAttacked'] == True)


def unhighlightName(creatureNameImg):
    return np.where(
        creatureNameImg == config["creatures"]["highlightedNamePixelColor"],
        config["creatures"]["namePixelColor"],
        creatureNameImg
    )
