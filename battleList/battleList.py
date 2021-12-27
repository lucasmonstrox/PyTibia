
import math
import numpy as np
import pyautogui
from utils import utils
from wiki.creatures import creatures

config = {
    "container": {
        "topImg": utils.loadImgAsArray('battleList/images/battleList.png'),
        "bottomImg": utils.loadImgAsArray('battleList/images/endOfContainer.png'),
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
    creatureImg = utils.loadImgAsArray(
        'battleList/images/monsters/{}.png'.format(creatureName))
    creatureHash = utils.hashit(creatureImg)
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


@utils.cacheObjectPos
def getContainerBottom(img):
    return utils.locate(img, config["container"]["bottomImg"])


@utils.cacheObjectPos
def getContainerTop(img):
    return utils.locate(img, config["container"]["topImg"])


def getContent(screenshot):
    (contentLeft, contentTop, _, contentHeight) = getContainerTop(screenshot)
    startingY = contentTop + contentHeight
    endingX = contentLeft + config["container"]["width"]
    content = screenshot[startingY:, contentLeft:endingX]
    endOfContainer = getContainerBottom(content)
    content = content[:endOfContainer[1] - 11, :]
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


def getCreatureFromSlot(content, slot):
    slotImg = getCreatureSlotImg(content, slot)
    upperCreatureBorder = slotImg[0:1, 0:19].flatten()
    isCreatureBeingAttacked = np.all(np.logical_or(
        upperCreatureBorder == 76, upperCreatureBorder == 166))
    # TODO: apply it once when parsing content
    slotImg = utils.graysToBlack(slotImg)
    creatureNameImg = getCreatureNameImg(slotImg)
    creatureNameImg = np.ravel(creatureNameImg)
    creatureHash = utils.hashit(creatureNameImg)
    unknownCreature = not creatureHash in config["creatures"]["hashes"]
    creatureName = "Unknown" if unknownCreature else config[
        "creatures"]["hashes"][creatureHash]["name"]
    creature = {
        "name": creatureName,
        "hash": creatureHash,
        "isBeingAttacked": isCreatureBeingAttacked
    }
    return creature


def getCreatures(screenshot):
    content = getContent(screenshot)
    contentIsTooSmall = content.shape[0] < config["slot"]["height"]
    if contentIsTooSmall:
        # TODO: throw custom exception
        raise None
    content = replaceHighlightedName(content)
    filledSlots = getFilledSlots(content)
    creatures = np.array([getCreatureFromSlot(content, creature)
                         for creature in np.arange(filledSlots)])
    isAttackingAnyCreature = False
    for creature in creatures:
        if creature["isBeingAttacked"] == True:
            isAttackingAnyCreature = True
            break
    return {"creatures": creatures, "isAttackingAnyCreature": isAttackingAnyCreature}


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


def replaceHighlightedName(creatureNameImg):
    return np.where(
        creatureNameImg == config["creatures"]["highlightedNamePixelColor"],
        config["creatures"]["namePixelColor"],
        creatureNameImg
    )
