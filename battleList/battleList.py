
import cv2
import math
import numpy as np
from utils import utils
import xxhash
from wiki.creatures import creatures


battleList = {
    "container": {
        "width": 156
    },
    "creatures": {
        "nameColor": 192,
        "highlightedNameColor": 247
    },
    "slot": {
        "height": 20,
    },
}


def getHash(creatureNameImg):
    creatureNameImg = np.ascontiguousarray(creatureNameImg)
    hashCode = xxhash.xxh64(creatureNameImg).intdigest()
    return hashCode


creaturesHashes = {}

for creature in creatures:
    if creature == 'Butterfly':
        break
    creatureImg = np.array(
        cv2.imread(
            'battleList/images/monsters/{}.png'.format(creature),
            cv2.IMREAD_GRAYSCALE
        )
    )
    creatureHash = xxhash.xxh64(creatureImg).intdigest()
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


def getCreatureBySlot(battleListContent, slot):
    isFirstSlot = slot == 0
    y = 0 if isFirstSlot else slot * 22
    slotImg = battleListContent[y:y + battleList["slot"]["height"], :]
    creatureNameImg = slotImg[3:11+3, 23:23 + 131]
    flattenedCreatureNameImg = creatureNameImg.flatten()
    isEmpty = not np.any(flattenedCreatureNameImg == 192)
    if isEmpty:
        return None
    # utils.saveImg(creatureNameImg, 'creatureNameImg-{}.png'.format(slot))
    creatureHash = getHash(creatureNameImg)
    unknownCreature = not creatureHash in creaturesHashes
    creature = {
        "creature": "Unknown" if unknownCreature else creaturesHashes[creatureHash]["name"],
        "hash": creatureHash,
        "isBeingAttacked": False
    }
    return creature


def getCreatures(battleListContent):
    (battleListContentLeft, battleListContentTop, _,
     battleListContentHeight) = getPos(battleListContent)
    battleListContent = battleListContent[battleListContentTop + battleListContentHeight:,
                                          battleListContentLeft:battleListContentLeft + battleList["container"]["width"]]
    endOfContainer = getNextEndOfContainer(battleListContent)
    battleListContent = battleListContent[:endOfContainer[1] - 11, :]
    battleListContent = utils.graysToBlack(battleListContent)
    battleListContent = replaceHighlightedName(battleListContent)
    battleListIsTooSmall = battleListContent.shape[0] < battleList["slot"]["height"]
    if battleListIsTooSmall:
        raise BattleListIsTooSmallError
    filledSlots = getFilledSlots(battleListContent)
    possibleCreatures = np.array(list(map(lambda x: getCreatureBySlot(
        battleListContent, x), np.arange(filledSlots))))
    creatures = possibleCreatures[possibleCreatures != None]
    return creatures


def getFilledSlots(battleListContent):
    battleListContentFlattened = battleListContent[:, 23:24].flatten()
    possibleCreatureNames = np.nonzero(
        np.where(
            battleListContentFlattened == battleList["creatures"]["nameColor"],
            True,
            False
        )
    )[0]
    hasNoFilledSlots = len(possibleCreatureNames) == 0
    if hasNoFilledSlots:
        return 0
    lastPossibleCreatureIndex = possibleCreatureNames[len(
        possibleCreatureNames) - 1]
    filledSlots = math.ceil(lastPossibleCreatureIndex / 22)
    return filledSlots


@ utils.cacheObjectPos
def getNextEndOfContainer(img):
    return utils.locate(img, endOfContainerImg)


@ utils.cacheObjectPos
def getPos(img):
    return utils.locate(img, battleListImg)


def replaceHighlightedName(nameImg):
    return np.where(
        nameImg == battleList["creatures"]["highlightedNameColor"],
        battleList["creatures"]["nameColor"],
        nameImg
    )
