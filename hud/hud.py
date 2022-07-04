import math
import numpy as np
import pyautogui
from utils import utils
from wiki import creatures
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
creaturesNamesHashes = {}
for monster in creatures.creatures:
    creaturesNamesHashes[monster] = utils.loadImgAsArray('hud/images/monsters/{}.png'.format(monster))
leftHud = utils.loadImgAsArray('hud/images/leftHud.png')
rightHud = utils.loadImgAsArray('hud/images/rightHud.png')

hudSize = (480, 352)


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


# TODO: group pixels by 27 black pixels, it means a possible life bar
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
    hasNoCreaturesBars = possibleCreatures.size == 0
    if hasNoCreaturesBars:
        return np.array([])
    creaturesBars = np.take(blackPixelsIndexes, possibleCreatures)
    creaturesBars = np.array(
        list(map(lambda i: [i % hudWidth, i // hudWidth], creaturesBars)))
    return creaturesBars


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


def makeCreature(creatureName, coordinate, hudCoordinates):
    (hudCoordinateX, hudCoordinateY, _, _) = hudCoordinates
    (x, y) = coordinate
    extraY = 0 if y <= 27 else 15
    xCoordinate = x - 3 + extraY
    yCoordinate = y + 5 + extraY
    xSlot = round(xCoordinate / 32)
    xSlot = 14 if xSlot > 14 else xSlot
    ySlot = 0 if y <= 27 else round(yCoordinate / 32)
    ySlot = 10 if ySlot > 10 else ySlot
    healthPercentage = 100
    isBeingAttacked = False
    slot = (xSlot, ySlot)
    windowCoordinate = (hudCoordinateX + xCoordinate, hudCoordinateY + yCoordinate)
    return (creatureName, healthPercentage, isBeingAttacked, slot, windowCoordinate)


def getClosestCreature(creatures, coordinate, walkableFloorsSqms):
    (x, y) = utils.getPixelFromCoordinate(coordinate)
    hudwalkableFloorsSqms = walkableFloorsSqms[y-5:y+6, x-7:x+8]
    hudwalkableFloorsSqmsCreatures = np.zeros((11, 15))
    creaturesDict = {}
    for creature in creatures:
        hudwalkableFloorsSqmsCreatures[creature['slot'][1], creature['slot'][0]] = 1
        creaturesDict[(creature['slot'][0], creature['slot'][1])] = creature
    adjacencyMatrix = utils.getAdjacencyMatrix(hudwalkableFloorsSqms)
    sqmsGraph = csr_matrix(adjacencyMatrix)
    sqmsGraphWeights = dijkstra(sqmsGraph, directed=True, indices=82, unweighted=False)
    creaturesIndexes = np.nonzero(hudwalkableFloorsSqmsCreatures.flatten() == 1)[0]
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
    if shortestCreatureIndex is None:
        return None
    creatureSlot = (shortestCreatureIndex % 15, shortestCreatureIndex // 15)
    return creaturesDict[creatureSlot]


creatureType = np.dtype([
    ('name', np.str_, 64),
    ('healthPercentage', np.uint8),
    ('isBeingAttacked', np.bool_),
    ('slot', np.uint8, (2,)),
    ('windowCoordinate', np.uint32, (2,))
])


def cleanCreatureName(creatureName):
    creatureName = np.where(creatureName == 29, 0, creatureName)
    creatureName = np.where(creatureName == 91, 0, creatureName)
    creatureName = np.where(creatureName == 113, 0, creatureName)
    creatureName = np.where(creatureName == 152, 0, creatureName)
    creatureName = np.where(creatureName == 170, 0, creatureName)
    creatureName = np.where(creatureName == 192, 0, creatureName)
    creatureName = np.where(creatureName != 0, 255, creatureName)
    return creatureName


# TODO: after each loop, remove bar when creatureDidMatch
# TODO: use matrix calculations instead of for loops
def getCreatures(screenshot, battleListCreatures):
    hudCoordinates = getCoordinates(screenshot)
    hudImg = getImgByCoordinates(screenshot, hudCoordinates)
    creaturesBars = getCreaturesBars(hudImg.flatten())
    creatures = np.array([], dtype=creatureType)
    hasNoCreaturesBars = len(creaturesBars) == 0
    if hasNoCreaturesBars:
        return creatures
    hasNoBattleListCreatures = len(battleListCreatures) == 0
    if hasNoBattleListCreatures:
        return creatures
    possibleCreatures = {}
    for battleListCreature in battleListCreatures:
        if battleListCreature['name'] != 'Unknown':
            possibleCreatures[battleListCreature['name']] = creaturesNamesHashes[battleListCreature['name']]
    for creatureName in possibleCreatures:
        _, creatureNameWidth  = possibleCreatures[creatureName].shape
        for creatureBar in creaturesBars:
            (creatureBarStartingX, creatureBarStartingY) = creatureBar
            creatureNameImgHalfWidth = math.floor(creatureNameWidth / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBarStartingX > leftDiff else leftDiff - creatureBarStartingX
            gapInnerLeft = 0 if creatureNameWidth > 27  else math.ceil((27 - creatureNameWidth) / 2)
            rightDiff = max(creatureNameWidth - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if hudSize[0] > (creatureBarStartingX + 27 + rightDiff) else creatureBarStartingX + 27 + rightDiff - hudSize[0]  
            gapInnerRight = 0 if creatureNameWidth > 27 else math.floor((27 - creatureNameWidth) / 2)
            startingX = creatureBarStartingX - creatureNameImgHalfWidth + 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            endingX = creatureBarStartingX + creatureNameImgHalfWidth + 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            creatureMess = hudImg[creatureBarStartingY - 13: creatureBarStartingY - 13 + 11, startingX:endingX]
            if creatureMess.shape[1] < creaturesNamesHashes[creatureName].shape[1]:
                creatureMess = hudImg[creatureBarStartingY - 13: creatureBarStartingY - 13 + 11, startingX:endingX+1]
            creatureMess = cleanCreatureName(creatureMess)
            creatureDidMatch = utils.hasMatrixInsideOther(creatureMess, creaturesNamesHashes[creatureName])
            if creatureDidMatch:
                creature = makeCreature(creatureName, creatureBar, hudCoordinates)
                creaturesToAppend = np.array([creature], dtype=creatureType)
                creatures = np.append(creatures, creaturesToAppend)
                continue
            creatureMess2 = hudImg[creatureBarStartingY - 13: creatureBarStartingY - 13 + 11, startingX+1:endingX+1]
            creatureNameHash = creaturesNamesHashes[creatureName].copy()
            if creatureMess2.shape[1] < creatureNameHash.shape[1]:
                creatureNameHash = creatureNameHash[:, 0:creatureNameHash.shape[1] - 1]
            creatureMess2 = cleanCreatureName(creatureMess2)
            creatureDidMatch = utils.hasMatrixInsideOther(creatureMess2, creatureNameHash)
            if creatureDidMatch:
                creature = makeCreature(creatureName, creatureBar, hudCoordinates)
                creaturesToAppend = np.array([creature], dtype=creatureType)
                creatures = np.append(creatures, creaturesToAppend)
                continue
            creatureMess3 = hudImg[creatureBarStartingY - 13: creatureBarStartingY - 13 + 11, startingX:endingX-1]
            creatureMess3 = cleanCreatureName(creatureMess3)
            creatureNameHash2 = creaturesNamesHashes[creatureName].copy()
            creatureNameHash2 = creatureNameHash2[:, 1:creatureNameHash2.shape[1]]
            if creatureMess3.shape[1] != creatureNameHash2.shape:
                continue
            creatureDidMatch = utils.hasMatrixInsideOther(creatureMess3, creatureNameHash2)
            if creatureDidMatch:
                creature = makeCreature(creatureName, creatureBar, hudCoordinates)
                creaturesToAppend = np.array([creature], dtype=creatureType)
                creatures = np.append(creatures, creaturesToAppend)
                continue
    return creatures


@utils.cacheObjectPos
def getLeftSidebarArrows(screenshot):
    return utils.locate(screenshot, leftHud)


@utils.cacheObjectPos
def getRightSidebarArrows(screenshot):
    return utils.locate(screenshot, rightHud)


# TODO: cache it
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


def getNearestCreaturesCount(creatures):
    hudwalkableFloorsSqmsCreatures = np.zeros((11, 15), dtype=np.uint)
    for creature in creatures:
        hudwalkableFloorsSqmsCreatures[creature['slot'][1], creature['slot'][0]] = 1
    mcDonalds = hudwalkableFloorsSqmsCreatures[
        [4, 4, 4, 5, 5, 6, 6, 6],
        [6, 7, 8, 6, 8, 6, 7, 8]
    ]
    nearestCreaturesCount = np.sum(mcDonalds)
    return nearestCreaturesCount