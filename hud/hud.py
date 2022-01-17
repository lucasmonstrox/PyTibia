import numpy as np
import pyautogui
from utils import utils
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

lifeBarBlackPixelsMapper = np.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    480, 506,
    960, 986,
    1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466
])
x = np.arange(lifeBarBlackPixelsMapper.size)
lifeBarFlattenedImg = np.zeros(lifeBarBlackPixelsMapper.size)
hudWidth = 480
creaturesNamesHashes = {
    "Centipede": utils.loadImgAsArray('hud/images/monsters/Centipede.png'),
    "Cobra": utils.loadImgAsArray('hud/images/monsters/Cobra.png'),
    "Crocodile": utils.loadImgAsArray('hud/images/monsters/Crocodile.png'),
    "Cyclops": utils.loadImgAsArray('hud/images/monsters/Cyclops.png'),
    "Frost Dragon Hatchling": utils.loadImgAsArray('hud/images/monsters/Frost Dragon Hatchling.png'),
    "Rat": utils.loadImgAsArray('hud/images/monsters/Rat.png'),
    "Lizard Sentinel": utils.loadImgAsArray('hud/images/monsters/Lizard Sentinel.png'),
    "Lizard Snakecharmer": utils.loadImgAsArray('hud/images/monsters/Lizard Snakecharmer.png'),
    "Lizard Templar": utils.loadImgAsArray('hud/images/monsters/Lizard Templar.png'),
    "Spit Nettle": utils.loadImgAsArray('hud/images/monsters/Spit Nettle.png'),
}
leftHud = utils.loadImgAsArray('hud/images/leftHud.png')
rightHud = utils.loadImgAsArray('hud/images/rightHud.png')


def moveToSlot(slot, hudPos):
    (hudPosX, hudPosY, hudWidth, hudHeight) = hudPos
    (slotX, slotY) = slot
    slotHeight = hudHeight // 11
    slotWidth = hudWidth // 15
    slotXCoordinate = hudPosX + (slotX * slotWidth)
    slotYCoordinate = hudPosY + (slotY * slotHeight)
    pyautogui.moveTo(slotXCoordinate, slotYCoordinate, duration=0.1)


def clickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.click()


def rightClickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.rightClick()


def getCreaturesBars(hudImg):
    blackPixelsIndexes = np.nonzero(hudImg == 0)[0]
    maxBlackPixelIndex = 168960 - 1468
    allowedBlackPixelsIndexes = np.nonzero(
        blackPixelsIndexes < maxBlackPixelIndex)[0]
    blackPixelsIndexes = np.take(blackPixelsIndexes, allowedBlackPixelsIndexes)
    noBlackPixels = blackPixelsIndexes.size == 0
    if noBlackPixels:
        return np.array([])
    x = np.broadcast_to(
        blackPixelsIndexes, (lifeBarBlackPixelsMapper.size, blackPixelsIndexes.size))
    x = np.transpose(x)
    z = np.add(x, lifeBarBlackPixelsMapper)
    pixelsColorsIndexes = np.take(hudImg, z)
    g = (pixelsColorsIndexes == lifeBarFlattenedImg).all(1)
    possibleCreatures = np.nonzero(g)[0]
    hasNoCreatures = possibleCreatures.size == 0
    if hasNoCreatures:
        return np.array([])
    creatures = np.take(blackPixelsIndexes, possibleCreatures)
    creatures = np.array(
        list(map(lambda i: [i % hudWidth, i // hudWidth], creatures)))
    return creatures


def getSlotFromCoordinate(currentCoordinate, coordinate):
    diffX = coordinate[0] - currentCoordinate[0]
    diffXAbs = abs(diffX)
    if diffXAbs > 7:
        # TODO: throw an exception
        print('diffXAbs > 7')
        return None
    diffY = coordinate[1] - currentCoordinate[1]
    diffYAbs = abs(diffY)
    if diffYAbs > 5:
        # TODO: throw an exception
        print('diffYAbs > 5')
        return None
    hudCoordinateX = 7 + diffX
    hudCoordinateY = 5 + diffY
    return (hudCoordinateX, hudCoordinateY)


def makeCreature(creatureName, coordinate):
    (x, y) = coordinate
    xCoordinate = x - 4 + 16
    yCoordinate = y + 6 + 16
    xSlot = xCoordinate // 32
    ySlot = yCoordinate // 32
    return {
        "name": creatureName,
        "isBeingAttacked": False,
        "windowCoordinate": (xCoordinate, yCoordinate),
        "slot": (xSlot, ySlot)
    }


def getClosestCreatures(creatures, coordinate, walkableSqms):
    (x, y) = utils.getPixelFromCoordinate(coordinate)
    hudWalkableSqms = walkableSqms[y-5:y+6, x-7:x+8]
    hudWalkableSqmsCreatures = np.zeros((11, 15))
    for creature in creatures:
        hudWalkableSqmsCreatures[creature["slot"][1], creature["slot"][0]] = 1
    adjacencyMatrix = utils.getAdjacencyMatrix(hudWalkableSqms)
    sqmsGraph = csr_matrix(adjacencyMatrix)
    sqmsGraphWeights = dijkstra(sqmsGraph, directed=True, indices=82, unweighted=False)
    creaturesIndexes = np.nonzero(hudWalkableSqmsCreatures.flatten() == 1)[0]
    creaturesWeights = np.take(sqmsGraphWeights, creaturesIndexes)
    i = 0
    shortestDistance = 999999
    shortestCreatureIndex = None
    for creatureWeight in creaturesWeights:
        creatureIndex = creaturesIndexes[i]
        creatureWeight = creaturesWeights[i]
        i += 1
        if creatureWeight == np.inf:
            continue
        if creatureWeight < shortestDistance:
            shortestDistance = creatureWeight
            shortestCreatureIndex = creatureIndex
    return shortestCreatureIndex


def getCreatures(hud, creaturesBars, battleListCreatures):
    # TODO: clean names once
    creatures = np.array([], dtype=object)
    hasNoBattleListCreatures = len(battleListCreatures["creatures"]) == 0
    if hasNoBattleListCreatures:
        return creatures
    hasUniqueMonster = len(battleListCreatures["creatures"]) == 1
    if hasUniqueMonster:
        (x, y) = creaturesBars[0]
        return np.append(creatures, makeCreature(battleListCreatures["creatures"][0]["name"], creaturesBars[0]))
    possibleMonsters = {}
    for battleListCreature in battleListCreatures["creatures"]:
        alreadyInPossibleMonsters = battleListCreature["name"] in possibleMonsters
        if alreadyInPossibleMonsters:
            continue
        possibleMonsters[battleListCreature["name"]] = creaturesNamesHashes[battleListCreature["name"]]
    for creatureBar in creaturesBars:
        (x, y) = creatureBar
        creatureMess = hud[y - 13: y - 13 + 11, x: x + 27]
        creatureMess = np.where(creatureMess == 29, 0, creatureMess)
        creatureMess = np.where(creatureMess == 91, 0, creatureMess)
        creatureMess = np.where(creatureMess == 113, 0, creatureMess)
        creatureMess = np.where(creatureMess == 152, 0, creatureMess)
        creatureMess = np.where(creatureMess == 170, 0, creatureMess)
        creatureMess = np.where(creatureMess != 0, 255, creatureMess)
        creatureMessFlattened = creatureMess.flatten()
        for creatureName in possibleMonsters:
            creatureHashFlattened = creaturesNamesHashes[creatureName].flatten(
            )
            creatureBlackPixelsIndexes = np.nonzero(
                creatureHashFlattened == 0)[0]
            blackPixels = np.take(creatureMessFlattened,
                                  creatureBlackPixelsIndexes)
            creatureDidMatch = np.all(blackPixels == 0)
            if creatureDidMatch:
                creatures = np.append(creatures, makeCreature(creatureName, creatureBar))
    return creatures


def getCreatures_perf(hud, creaturesBars, battleListCreatures):
    hashImgWidth = 27
    battleListMonstersCount = battleListCreatures.size
    # obtaining a flattened contigous mess array of each creatures bars in 3d array
    # creaturesBarsHashes = np.array([hud[creature[1] - 13:creature[1] - 13 + 11,
    #                                creature[0]: creature[0] + hashImgWidth] for creature in creaturesBars])
    creaturesBarsHashes = np.array(
        list(map(lambda creature: np.ravel(hud[creature[1] - 13:creature[1] - 13 + 11,
                                               creature[0]: creature[0] + hashImgWidth]), creaturesBars)))
    # converting each pixel with color 113(color inside letters) to black
    creaturesBarsHashes = np.where(
        creaturesBarsHashes == 113, 0, creaturesBarsHashes)
    # converting each black pixel to 1
    creaturesBarsHashes = np.where(creaturesBarsHashes == 0, 1, 0)
    # obtaining a flattened contigous clean array of each creature in battle list
    battleListMonstersHashes = np.array(
        list(map(lambda creature: np.ravel(creaturesNamesHashes[creature["name"]]), battleListCreatures)))
    # battleListMonstersHashes = np.array(
    # [np.ravel(creaturesNamesHashes[creature["name"]]) for creature in battleListCreatures])
    # converting white pixels to 1
    battleListMonstersHashes = np.where(battleListMonstersHashes == 255, 1, 0)
    left = np.repeat(creaturesBarsHashes, battleListMonstersCount, axis=0)
    left = np.array(np.vsplit(left, battleListMonstersCount))
    right = np.broadcast_to(battleListMonstersHashes,
                            (creaturesBarsHashes.shape[0],
                             battleListMonstersCount,
                             battleListMonstersHashes.shape[1]))
    z = np.add(left, right)
    z = np.all(z == 1, axis=2)
    z = np.where(z, 1, 0)
    z = z - 1
    z = z.flatten()
    creatures = np.take(battleListCreatures, z)
    return creatures


@utils.cacheObjectPos
def getLeftSidebarArrows(screenshot):
    return utils.locate(screenshot, leftHud)


@utils.cacheObjectPos
def getRightSidebarArrows(screenshot):
    return utils.locate(screenshot, rightHud)


def getCoordinates(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    rightSidebarArrows = getRightSidebarArrows(screenshot)
    (hudWidth, hudHeight) = (480, 352)
    hudCenter = (
        (rightSidebarArrows[0] - leftSidebarArrows[0]) // 2) + leftSidebarArrows[0]
    hudLeftPos = hudCenter - (hudWidth // 2) - 1
    hud = screenshot[leftSidebarArrows[1] + 5: leftSidebarArrows[1] +
                     5 + hudHeight, hudLeftPos:hudLeftPos + 1]
    hud = np.where(np.logical_and(hud >= 18, hud <= 30), 1, 0)
    isHudDetected = np.all(hud == 1)
    if isHudDetected:
        x = hudLeftPos + 1
        y = leftSidebarArrows[1] + 5
        bbox = (x, y, 480, 352)
        return bbox


def getImgByCoordinates(screenshot, coordinates):
    return screenshot[coordinates[1]:coordinates[1] +
                      352, coordinates[0]:coordinates[0] + 480]
