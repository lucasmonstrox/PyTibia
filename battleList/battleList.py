
import cv2
import math
import numpy as np
from utils import utils
import xxhash
from wiki.creatures import creatures

config = {
    "container": {
        "width": 156
    },
    "creatures": {
        "nameColor": 192,
        "highlightedNameColor": 247
    },
    "slot": {
        "height": 20,
        "gap": 2
    },
}

creaturesHashes = {}


def getHash(creatureNameImg):
    creatureNameImg = np.ascontiguousarray(creatureNameImg)
    hashCode = xxhash.xxh64(creatureNameImg).intdigest()
    return hashCode


for creature in creatures:
    creatureImg = np.array(
        cv2.imread(
            'battleList/images/monsters/{}.png'.format(creature),
            cv2.IMREAD_GRAYSCALE
        )
    )
    creatureHash = getHash(creatureImg)
    creaturesHashes[creatureHash] = {
        "name": creature,
        "hash": creatureHash,
        "info": creatures[creature]
    }


class BattleListIsTooSmallError():
    """Raised when battle list is too small"""
    pass


battleListImg = np.array(cv2.cvtColor(cv2.imread(
    'battleList/images/battleList.png'), cv2.COLOR_RGB2GRAY))
endOfContainerImg = np.array(cv2.cvtColor(cv2.imread(
    'battleList/images/endOfContainer.png'), cv2.COLOR_RGB2GRAY))


def getCreatureSlotImg(content, slot):
    isFirstSlot = slot == 0
    startingY = 0 if isFirstSlot else slot * \
        (config["slot"]["height"] + config["slot"]["gap"])
    finishingY = startingY + config["slot"]["height"]
    slotImg = content[startingY:finishingY, :]
    return slotImg


def getCreatureNameImg(slotImg):
    # TODO: improve clean code
    return slotImg[3:11 + 3, 23:23 + 131]


def getCreatureFromSlot(content, slot):
    slotImg = getCreatureSlotImg(content, slot)
    creatureNameImg = getCreatureNameImg(slotImg)
    creatureNameImg = np.ravel(creatureNameImg)
    isEmpty = not np.any(creatureNameImg == config["creatures"]["nameColor"])
    if isEmpty:
        return None
    creatureHash = getHash(creatureNameImg)
    unknownCreature = not creatureHash in creaturesHashes
    creature = {
        "name": "Unknown" if unknownCreature else creaturesHashes[creatureHash]["name"],
        "hash": creatureHash,
        "isBeingAttacked": False
    }
    return creature


def getCreatures(screenshot):
    content = getContent(screenshot)
    contentIsTooSmall = content.shape[0] < config["slot"]["height"]
    if contentIsTooSmall:
        raise BattleListIsTooSmallError
    content = utils.graysToBlack(content)
    content = replaceHighlightedName(content)
    filledSlots = getFilledSlots(content)
    creatures = np.array([getCreatureFromSlot(content, x)
                         for x in np.arange(filledSlots)])
    creatures = creatures[creatures != None]
    return creatures


def getContent(screenshot):
    (contentLeft, contentTop, _, contentHeight) = getPos(screenshot)
    startingY = contentTop + contentHeight
    endingX = contentLeft + config["container"]["width"]
    content = screenshot[startingY:, contentLeft:endingX]
    endOfContainer = getNextEndOfContainer(content)
    content = content[:endOfContainer[1] - 11, :]
    return content


def getFilledSlots(content):
    content = np.ravel(content[:, 23:24])
    possibleCreatureNames = np.nonzero(
        np.where(
            content == config["creatures"]["nameColor"],
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


@utils.cacheObjectPos
def getNextEndOfContainer(img):
    return utils.locate(img, endOfContainerImg)


@utils.cacheObjectPos
def getPos(img):
    return utils.locate(img, battleListImg)


def replaceHighlightedName(creatureNameImg):
    return np.where(
        creatureNameImg == config["creatures"]["highlightedNameColor"],
        config["creatures"]["nameColor"],
        creatureNameImg
    )
