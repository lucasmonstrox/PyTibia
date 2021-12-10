import cupy as cp
import cv2
import math
import numpy as np
from utils import utils
import xxhash


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


butterflyImg = np.array(cv2.imread(
    'battleList/images/monsters/butterfly.png', cv2.IMREAD_GRAYSCALE))
centipedeImg = np.array(cv2.imread(
    'battleList/images/monsters/centipede.png', cv2.IMREAD_GRAYSCALE))
crocodileImg = np.array(cv2.imread(
    'battleList/images/monsters/crocodile.png', cv2.IMREAD_GRAYSCALE))
elephantImg = np.array(cv2.imread(
    'battleList/images/monsters/elephant.png', cv2.IMREAD_GRAYSCALE))
flamingoImg = np.array(cv2.imread(
    'battleList/images/monsters/flamingo.png', cv2.IMREAD_GRAYSCALE))
hunterImg = np.array(cv2.imread(
    'battleList/images/monsters/hunter.png', cv2.IMREAD_GRAYSCALE))
lizardSentinelImg = np.array(cv2.imread(
    'battleList/images/monsters/lizardSentinel.png', cv2.IMREAD_GRAYSCALE))
lizardTemplarImg = np.array(cv2.imread(
    'battleList/images/monsters/lizardTemplar.png', cv2.IMREAD_GRAYSCALE))
poisonSpiderImg = np.array(cv2.imread(
    'battleList/images/monsters/poisonSpider.png', cv2.IMREAD_GRAYSCALE))
sandcrawlerImg = np.array(cv2.imread(
    'battleList/images/monsters/sandcrawler.png', cv2.IMREAD_GRAYSCALE))
snakeImg = np.array(cv2.imread(
    'battleList/images/monsters/snake.png', cv2.IMREAD_GRAYSCALE))
spitNettleImg = np.array(cv2.imread(
    'battleList/images/monsters/spitNettle.png', cv2.IMREAD_GRAYSCALE))
waspImg = np.array(cv2.imread(
    'battleList/images/monsters/wasp.png', cv2.IMREAD_GRAYSCALE))

creaturesHashes = {
    getHash(butterflyImg): {"name": "Butterfly", "type": "Monster"},
    getHash(centipedeImg): {"name": "Centipede", "type": "Monster"},
    getHash(crocodileImg): {"name": "Crocodile", "type": "Monster"},
    getHash(elephantImg): {"name": "Elephant", "type": "Monster"},
    getHash(flamingoImg): {"name": "Flamingo", "type": "Monster"},
    getHash(hunterImg): {"name": "Hunter", "type": "Monster"},
    getHash(lizardSentinelImg): {"name": "Lizard Sentinel", "type": "Monster"},
    getHash(lizardTemplarImg): {"name": "Lizard Templar", "type": "Monster"},
    getHash(poisonSpiderImg): {"name": "Poison Spider", "type": "Monster"},
    getHash(sandcrawlerImg): {"name": "Sandcrawler", "type": "Monster"},
    getHash(snakeImg): {"name": "Snake", "type": "Monster"},
    getHash(spitNettleImg): {"name": "Spit Nettle", "type": "Monster"},
    getHash(waspImg): {"name": "Wasp", "type": "Monster"},
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
    creatureNameImg = slotImg[:15, 22:22 + 132]
    flattenedCreatureNameImg = creatureNameImg.flatten()
    isEmpty = np.any(flattenedCreatureNameImg == 192)
    if isEmpty:
        return None
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
    battleListContentFlattened = battleListContent[:, 78:79].flatten()
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


@utils.cacheObjectPos
def getNextEndOfContainer(img):
    return utils.locate(img, endOfContainerImg)


@utils.cacheObjectPos
def getPos(img):
    return utils.locate(img, battleListImg)


def replaceHighlightedName(nameImg):
    return np.where(
        nameImg == battleList["creatures"]["highlightedNameColor"],
        battleList["creatures"]["nameColor"],
        nameImg
    )
