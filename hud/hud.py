import cupy as cp
import numpy as np
import cv2
from utils import utils

y = cp.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    480, 506,
    960, 986,
    1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466
])
x = cp.arange(y.size)

allBlack = cp.zeros(y.size, dtype=cp.uint8)
hudWidth = 480


def getCreaturesBars(blackPixels):
    blackPixelsIndexes = cp.nonzero(blackPixels == 0)[0]
    noBlackPixels = blackPixelsIndexes.size == 0
    if noBlackPixels:
        return cp.array([])
    x = cp.broadcast_to(blackPixelsIndexes, (y.size, blackPixelsIndexes.size))
    x = cp.transpose(x)
    z = cp.add(x, y)
    pixelsColorsIndexes = cp.take(blackPixels, z)
    g = (pixelsColorsIndexes == allBlack).all(1)
    possibleCreatures = cp.nonzero(g)[0]
    hasNoCreatures = possibleCreatures.size == 0
    if hasNoCreatures:
        return cp.array([])
    creatures = cp.take(blackPixelsIndexes, possibleCreatures)
    creatures = cp.array(
        list(map(lambda i: [i % hudWidth, i // hudWidth], creatures)))
    return creatures


creaturesNamesHashes = {
    "Cyclops": cp.array(cv2.imread('hud/images/monsters/Cyclops.png', cv2.IMREAD_GRAYSCALE)),
    "Frost Dragon Hatchling": cp.array(cv2.imread('hud/images/monsters/Frost Dragon Hatchling.png', cv2.IMREAD_GRAYSCALE)),
    "Rat": cp.array(cv2.imread('hud/images/monsters/Rat.png', cv2.IMREAD_GRAYSCALE)),
}


def getCreaturesFromBars(hud, creaturesBars, battleListCreatures):
    hasUniqueMonster = len(battleListCreatures) == 1
    if hasUniqueMonster:
        return np.array([makeCreature(battleListCreatures[0], creaturesBars[0])])
    creatures = np.array([])
    for creatureBar in creaturesBars:
        x = creatureBar[0]
        y = creatureBar[1]
        for creatureNameHash in creaturesNamesHashes:
            creatureNameWidth = len(creaturesNamesHashes[creatureNameHash][0])
            creatureNameWidth = max(creatureNameWidth, 27)
            if creatureNameWidth > 27:
                g = creatureNameWidth - 27
                left = (g // 2) + 1
                right = g // 2
                creatureMess = hud[y - 13:y - 13 + 11, x-left:x + 27 + right]
            else:
                creatureMess = hud[y - 13:y - 13 + 11, x:x + creatureNameWidth]
            creatureMess = cp.where(
                creatureMess == 113, 0, creatureMess)
            creatureMess = cp.where(
                creatureMess != 0, 255, creatureMess)
            utils.saveCpImg(
                creatureMess, 'creature-{}.png'.format(creatureNameHash))
            creatureMessFlattened = creatureMess.flatten()
            creatureHashFlattened = creaturesNamesHashes[creatureNameHash].flatten(
            )
            creatureBlackPixelsIndexes = cp.nonzero(
                creatureHashFlattened == 0)[0]
            blackPixels = cp.take(creatureMessFlattened,
                                  creatureBlackPixelsIndexes)
            creatureDidMatch = cp.all(blackPixels == 0)
            if creatureDidMatch:
                creatures = np.append(creatures, creatureNameHash)
    print(creatures)
    return creatures


def makeCreature(creatureBattleList, creatureBar):
    creature = {"creatureBattleList": creatureBattleList,
                "creatureBar": creatureBar}
    return creature
