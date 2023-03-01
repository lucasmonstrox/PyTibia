import math
from numba import njit
import numpy as np
import pathlib
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import radar.config
import radar.core
import utils.core
import utils.image
import utils.matrix
from wiki.creatures import creatures as wikiCreatures
from .typing import creatureType


currentPath = pathlib.Path(__file__).parent.resolve()
resolutions = {
    720: {
        'hudHeight': 352,
        'hudWidth': 480,
        'slotWidth': 32,
    },
    1080: {
        'hudHeight': 704,
        'hudWidth': 960,
        'slotWidth': 64,
    },
}
creaturesNamesHashes = {}
for creature in wikiCreatures:
    creaturesNamesHashes[creature] = utils.image.loadAsGrey(
        f'{currentPath}/images/monsters/{creature}.png')


def getClosestCreature(hudCreatures, coordinate):
    hasNoCreatures = len(hudCreatures) == 0
    if hasNoCreatures:
        return None
    floorLevel = coordinate[2]
    walkableFloorsSqms = radar.config.walkableFloorsSqms[floorLevel]
    hudWalkableFloorsSqms = getHudWalkableFloorsSqms(
        walkableFloorsSqms, coordinate)
    adjacencyMatrix = utils.matrix.getAdjacencyMatrix(hudWalkableFloorsSqms)
    sqmsGraph = csr_matrix(adjacencyMatrix)
    playerHudIndex = 82
    sqmsGraphWeights = dijkstra(
        sqmsGraph, directed=True, indices=playerHudIndex, unweighted=False)
    creaturesSlots = hudCreatures['slot'][:, [1, 0]]
    hudWalkableFloorsSqmsCreatures = np.zeros((11, 15))
    hudWalkableFloorsSqmsCreatures[creaturesSlots[:,
                                                  0], creaturesSlots[:, 1]] = 1
    creaturesIndexes = np.nonzero(
        hudWalkableFloorsSqmsCreatures.flatten() == 1)[0]
    creaturesGraphWeights = np.take(sqmsGraphWeights, creaturesIndexes)
    nonTargetCreaturesIndexes = np.where(creaturesGraphWeights == np.inf)[0]
    creaturesIndexes = np.delete(creaturesIndexes, nonTargetCreaturesIndexes)
    creaturesGraphWeights = np.delete(
        creaturesGraphWeights, nonTargetCreaturesIndexes)
    hasOnlyNonTargetCreatures = len(creaturesGraphWeights) == 0
    if hasOnlyNonTargetCreatures:
        return None
    creaturesDistances = np.where(
        creaturesGraphWeights == np.amin(creaturesGraphWeights))[0]
    closestCreatureHudIndex = creaturesIndexes[np.random.choice(
        creaturesDistances)]
    creatureSlot = [closestCreatureHudIndex %
                    15, closestCreatureHudIndex // 15]
    closestCreatureIndex = np.where(
        (hudCreatures['slot'] == creatureSlot).all(axis=1))[0][0]
    closestCreature = hudCreatures[closestCreatureIndex]
    return closestCreature


@njit(cache=True, fastmath=True)
def getCreaturesBars(hudImg):
    imgHeight, imgWidth = hudImg.shape
    bars = []
    for j in range(imgHeight - 3):
        i = -1
        while(i < (imgWidth - 27)):
            i += 1
            if hudImg[j, i] & 0xFF == 0:
                upperBorderIsBlack = True
                for value in hudImg[j, i: i + 27]:
                    if value & 0xFF != 0:
                        upperBorderIsBlack = False
                        break
                if upperBorderIsBlack == False:
                    continue
                leftBorderIsBlack = True
                for value in hudImg[j: j + 4, i]:
                    if value & 0xFF != 0:
                        leftBorderIsBlack = False
                        break
                if leftBorderIsBlack == False:
                    continue
                rightBorderIsBlack = True
                for value in hudImg[j: j + 4, i + 26]:
                    if value & 0xFF != 0:
                        rightBorderIsBlack = False
                        break
                if rightBorderIsBlack == False:
                    continue
                bottomBorderIsBlack = True
                for value in hudImg[j + 3, i: i + 26]:
                    if value & 0xFF != 0:
                        bottomBorderIsBlack = False
                        break
                if bottomBorderIsBlack:
                    bars.append((i, j))
    return bars


# TODO: if last category is remaining, avoid calculating, return it immediatelly
# TODO: add name missAlignment for each creature, it avoid possible 3 calculations
# TODO: maximum creatures allowed should be equal battle list size
def getCreatures(battleListCreatures, direction, hudCoordinate, hudImg, coordinate):
    """
    TODO:
    - Find a way to avoid 3 calculation times when comparing names since some words have a wrong location
    - Whenever the last species is left, avoid loops and resolve species immediately for remaining creatures bars
    """
    creatures = []
    battleListCreaturesCount = len(battleListCreatures)
    hasNoBattleListCreatures = battleListCreaturesCount == 0
    if hasNoBattleListCreatures:
        return creatures
    creaturesBars = getCreaturesBars(hudImg)
    hasNoCreaturesBars = len(creaturesBars) == 0
    if hasNoCreaturesBars:
        return creatures
    hudWidth = len(hudImg[1])
    x = (len(hudImg[1]) / 2) - 1
    y = (len(hudImg[0]) / 2) - 1
    slotWidth = len(hudImg[1]) // 15
    centersBars = np.broadcast_to([x, y], (len(creaturesBars), 2))
    absolute = np.absolute(creaturesBars - centersBars)
    power = np.power(absolute, 2)
    sum = np.sum(power, axis=1)
    sqrt = np.sqrt(sum)
    creaturesBarsSortedIndexes = np.argsort(sqrt)
    discoverTarget = np.any(battleListCreatures['isBeingAttacked'] == True)
    for creatureBarSortedIndex in creaturesBarsSortedIndexes:
        creatureBar = creaturesBars[creatureBarSortedIndex]
        nonCreaturesForCurrentBar = {}
        battleListCreaturesCount = len(battleListCreatures)
        for battleListIndex in range(battleListCreaturesCount):
            battleListCreature = battleListCreatures[battleListIndex]
            creatureName = battleListCreature['name']
            isUnknownCreature = creatureName == 'Unknown'
            if isUnknownCreature:
                creature = makeCreature(creatureName, 'player', creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListCreatures = np.delete(battleListCreatures, battleListIndex)
                continue
            creatureTypeAlreadyTried = creatureName in nonCreaturesForCurrentBar
            if creatureTypeAlreadyTried:
                continue
            creatureNameImg = creaturesNamesHashes.get(creatureName).copy()
            creatureNameWidth = creatureNameImg.shape[1]
            (creatureBarX, creatureBarY) = creatureBar
            creatureBarY0 = creatureBarY - 13
            creatureBarY1 = creatureBarY0 + 11
            creatureNameImgHalfWidth = math.floor(creatureNameWidth / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBarX > leftDiff else leftDiff - creatureBarX
            gapInnerLeft = 0 if creatureNameWidth > 27 else math.ceil((27 - creatureNameWidth) / 2)
            rightDiff = max(creatureNameWidth - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if hudWidth > (creatureBarX + 27 + rightDiff) else creatureBarX + 27 + rightDiff - hudWidth
            gapInnerRight = 0 if creatureNameWidth > 27 else math.floor((27 - creatureNameWidth) / 2)
            gg = 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            startingX = max(0, creatureBarX - creatureNameImgHalfWidth + gg)
            endingX = min(hudWidth, creatureBarX + creatureNameImgHalfWidth + gg)
            creatureWithDirtNameImg = hudImg[creatureBarY0:creatureBarY1, startingX:endingX]
            if creatureNameImg.shape[1] != creatureWithDirtNameImg.shape[1]:
                creatureWithDirtNameImg = hudImg[creatureBarY0:creatureBarY1, startingX:endingX + 1]
            creatureDidMatch = utils.matrix.hasMatrixInsideOther(creatureWithDirtNameImg, creatureNameImg)
            if creatureDidMatch:
                creature = makeCreature(creatureName, 'monster', creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListCreatures = np.delete(battleListCreatures, battleListIndex)
                break
            creatureNameImg2 = creaturesNamesHashes.get(creatureName).copy()
            creatureWithDirtNameImg2 = hudImg[creatureBarY0:creatureBarY1, startingX + 1:endingX + 1]
            if creatureNameImg2.shape[1] != creatureWithDirtNameImg2.shape[1]:
                creatureNameImg2 = creatureNameImg2[:, 0:creatureNameImg2.shape[1] - 1]
            creatureDidMatch = utils.matrix.hasMatrixInsideOther(creatureWithDirtNameImg2, creatureNameImg2)
            if creatureDidMatch:
                creature = makeCreature(creatureName, 'monster', creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListCreatures = np.delete(battleListCreatures, battleListIndex)
                break
            creatureWithDirtNameImg3 = hudImg[creatureBarY0:creatureBarY1, startingX:endingX - 1]
            creatureNameImg3 = creaturesNamesHashes.get(creatureName).copy()
            creatureNameImg3 = creatureNameImg3[:, 1:creatureNameImg3.shape[1]]
            if creatureWithDirtNameImg3.shape[1] != creatureNameImg3.shape[1]:
                creatureNameImg3 = creatureNameImg3[:, 0:creatureNameImg3.shape[1] - 1]
            creatureDidMatch = utils.matrix.hasMatrixInsideOther(creatureWithDirtNameImg3, creatureNameImg3)
            if creatureDidMatch:
                creature = makeCreature(creatureName, 'monster', creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListCreatures = np.delete(battleListCreatures, battleListIndex)
                break
            nonCreaturesForCurrentBar[creatureName] = True
    return np.array(creatures, dtype=creatureType)


def getCreaturesByType(hudCreatures, creatureType):
    return hudCreatures[hudCreatures['type'] == creatureType]


def getDifferentCreaturesBySlots(previousHudCreatures, currentHudCreatures, slots):
    previousHudCreaturesBySlots = np.array(
        [], dtype=creatureType)
    currentHudCreaturesBySlots = np.array(
        [], dtype=creatureType)
    differentCreatures = np.array([], dtype=creatureType)
    for previousHudCreature in previousHudCreatures:
        if np.isin(previousHudCreature['slot'], slots).all():
            previousHudCreaturesBySlots = np.append(
                previousHudCreaturesBySlots, [previousHudCreature])
    for currentHudCreature in currentHudCreatures:
        if np.isin(currentHudCreature['slot'], slots).all():
            currentHudCreaturesBySlots = np.append(
                currentHudCreaturesBySlots, [currentHudCreature])
    for previousHudCreature in previousHudCreaturesBySlots:
        creatureDoesNotExists = True
        for currentHudCreature in currentHudCreatures:
            previousHudCreatureHash = utils.core.hashitHex(
                previousHudCreature)
            currentHudCreatureHash = utils.core.hashitHex(
                currentHudCreature)
            if previousHudCreatureHash == currentHudCreatureHash:
                creatureDoesNotExists = False
                break
        if creatureDoesNotExists:
            differentCreatures = np.append(
                differentCreatures, [previousHudCreature])
    return differentCreatures


def getHudWalkableFloorsSqms(walkableFloorsSqms, coordinate):
    (xOfPixelCoordinate, yOfPixelCoordinate) = utils.core.getPixelFromCoordinate(
        coordinate)
    hudWalkableFloorsSqms = walkableFloorsSqms[yOfPixelCoordinate -
                                               5:yOfPixelCoordinate+6, xOfPixelCoordinate-7:xOfPixelCoordinate+8].copy()
    return hudWalkableFloorsSqms


# TODO: if something is already compared, avoid it. Check if it is faster
@njit(cache=True, fastmath=True)
def getNearestCreaturesCount(creatures):
    nearestCreaturesCount = 0
    for creatureSlot in creatures['slot']:
        if (creatureSlot[0] == 6 and creatureSlot[1] == 4) or (creatureSlot[0] == 7 and creatureSlot[1] == 4) or (creatureSlot[0] == 8 and creatureSlot[1] == 4) or (creatureSlot[0] == 6 and creatureSlot[1] == 5) or (creatureSlot[0] == 8 and creatureSlot[1] == 5) or (creatureSlot[0] == 6 and creatureSlot[1] == 6) or (creatureSlot[0] == 7 and creatureSlot[1] == 6) or (creatureSlot[0] == 8 and creatureSlot[1] == 6):
            nearestCreaturesCount += 1
    return nearestCreaturesCount


@njit(cache=True, fastmath=True)
def getTargetCreature(hudCreatures):
    hasNoHudCreatures = len(hudCreatures) == 0
    if hasNoHudCreatures:
        return None
    for hudCreature in hudCreatures:
        if hudCreature['isBeingAttacked']:
            return hudCreature
    return None


def hasTargetToCreatureBySlot(hudCreatures, slot, coordinate):
    hasNoHudCreatures = len(hudCreatures) == 0
    if hasNoHudCreatures:
        return False
    floorLevel = hudCreatures[0]['coordinate'][2]
    walkableFloorsSqms = radar.config.walkableFloorsSqms[floorLevel]
    hudWalkableFloorsSqms = getHudWalkableFloorsSqms(
        walkableFloorsSqms, coordinate)
    creaturesSlots = hudCreatures['slot'][:, [1, 0]]
    hudWalkableFloorsSqms[creaturesSlots[:, 0], creaturesSlots[:, 1]] = 0
    xOfSlot, yOfSlot = slot
    hudWalkableFloorsSqms[yOfSlot, xOfSlot] = 1
    adjacencyMatrix = utils.matrix.getAdjacencyMatrix(hudWalkableFloorsSqms)
    graph = csr_matrix(adjacencyMatrix)
    playerHudIndex = 82
    graphWeights = dijkstra(graph, directed=True,
                            indices=playerHudIndex, unweighted=False)
    graphWeights = graphWeights.reshape(11, 15)
    creatureGraphValue = graphWeights[yOfSlot, xOfSlot]
    hasTarget = creatureGraphValue != np.inf
    return hasTarget


def hasTargetToCreature(hudCreatures, hudCreature, coordinate):
    hasTarget = hasTargetToCreatureBySlot(
        hudCreatures, hudCreature['slot'], coordinate)
    return hasTarget


@njit(cache=True, fastmath=True)
def isCreatureBeingAttacked(hudImg, borderX, yOfCreatureBar, slotWidth):
    pixelsCount = 0
    borderedCreatureImg = hudImg[yOfCreatureBar + 5:yOfCreatureBar +
                                    5 + slotWidth, borderX:borderX + slotWidth]
    borderGap = 4 if slotWidth == 64 else 2
    yOfBorder = slotWidth - borderGap
    topBorder = borderedCreatureImg[0:borderGap, :].flatten()
    bottomBorder = borderedCreatureImg[yOfBorder:, :].flatten()
    leftBorder = borderedCreatureImg[borderGap:yOfBorder, 0:borderGap].flatten()
    rightBorder = borderedCreatureImg[borderGap:yOfBorder, yOfBorder:].flatten()
    for i in range(len(topBorder)):
        if topBorder[i] == 76 or topBorder[i] == 166:
            pixelsCount += 1
    if pixelsCount > 50:
        return True
    for i in range(len(leftBorder)):
        if leftBorder[i] == 76 or leftBorder[i] == 166:
            pixelsCount += 1
    if pixelsCount > 50:
        return True
    for i in range(len(rightBorder)):
        if rightBorder[i] == 76 or rightBorder[i] == 166:
            pixelsCount += 1
    if pixelsCount > 50:
        return True
    for i in range(len(bottomBorder)):
        if bottomBorder[i] == 76 or bottomBorder[i] == 166:
            pixelsCount += 1
    isBeingAttacked = pixelsCount > 50
    return isBeingAttacked


# TODO: improve clean code
# TODO: windowCoordinate should be improved for hud edges
# TODO: detect being creature by category
# TODO: since there is only one creature in hud and one in battleList being attacked, avoid computing if creature is being attacked on hud
def makeCreature(creatureName, creatureType, creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=True):
    isBigHud = slotWidth == 64
    (hudCoordinateX, hudCoordinateY, _, _) = hudCoordinate
    (xOfCreatureBar, yOfCreatureBar) = creatureBar
    wikiCreature = wikiCreatures.get(creatureName)
    hudMisalignment = wikiCreature.get('hudMisalignment', {'x': 0, 'y': 0})
    hudMisalignmentX = hudMisalignment['x'] if isBigHud else hudMisalignment['x'] / 2
    hudMisalignmentY = hudMisalignment['y'] if isBigHud else hudMisalignment['y'] / 2
    distanceBetweenSlotPixelLifeBar = 19 if isBigHud else 3
    xCoordinate = xOfCreatureBar - distanceBetweenSlotPixelLifeBar
    xSlot = round((xCoordinate + hudMisalignmentX) / slotWidth)
    xSlot = min(xSlot, 14)
    xSlot = max(xSlot, 0)
    yCoordinate = 0 if yOfCreatureBar <= 14 else yOfCreatureBar + 5
    ySlot = round((yCoordinate + hudMisalignmentY) / slotWidth)
    ySlot = min(ySlot, 10)
    ySlot = max(ySlot, 0)
    borderX = max(xOfCreatureBar - distanceBetweenSlotPixelLifeBar, 0)
    isBeingAttacked = False
    if discoverTarget:
        isBeingAttacked = isCreatureBeingAttacked(
            hudImg, borderX, yOfCreatureBar, slotWidth)
    slot = (xSlot, ySlot)
    coordinateX = coordinate[0] - 7 + xSlot
    coordinateY = coordinate[1] - 5 + ySlot
    coordinate = [coordinateX, coordinateY, coordinate[2]]
    currentCreatureCoordinateIsntWalkable = not radar.core.isCoordinateWalkable(
        coordinate)
    if currentCreatureCoordinateIsntWalkable:
        if direction == 'left' or direction == 'right':
            leftCoordinate = [coordinate[0] - 1,
                              coordinate[1], coordinate[2]]
            leftCoordinateIsWalkable = radar.core.isCoordinateWalkable(
                leftCoordinate)
            if leftCoordinateIsWalkable:
                coordinate = leftCoordinate
                xSlot = slot[0] - 1
                xSlot = min(xSlot, 14)
                xSlot = max(xSlot, 0)
                slot = (xSlot, slot[1])
            else:
                rightCoordinate = [coordinate[0] + 1,
                                   coordinate[1], coordinate[2]]
                rightCoordinateIsWalkable = radar.core.isCoordinateWalkable(
                    rightCoordinate)
                if rightCoordinateIsWalkable:
                    coordinate = rightCoordinate
                    xSlot = slot[0] + 1
                    xSlot = min(xSlot, 14)
                    xSlot = max(xSlot, 0)
                    slot = (xSlot, slot[1])
        if direction == 'top' or direction == 'bottom':
            topCoordinate = [coordinate[0],
                             coordinate[1] - 1, coordinate[2]]
            topCoordinateIsWalkable = radar.core.isCoordinateWalkable(
                topCoordinate)
            if topCoordinateIsWalkable:
                coordinate = topCoordinate
                ySlot = slot[1] - 1
                ySlot = min(ySlot, 10)
                ySlot = max(ySlot, 0)
                slot = (slot[0], ySlot)
            else:
                bottomCoordinate = [coordinate[0],
                                    coordinate[1] + 1, coordinate[2]]
                bottomCoordinateIsWalkable = radar.core.isCoordinateWalkable(
                    bottomCoordinate)
                if bottomCoordinateIsWalkable:
                    coordinate = bottomCoordinate
                    ySlot = slot[1] + 1
                    ySlot = min(ySlot, 10)
                    ySlot = max(ySlot, 0)
                    slot = (slot[0], ySlot)
    hudHeight, hudWidth = hudImg.shape
    halfOfSlot = (slotWidth / 2)
    maxHudHeightForAttacking = hudHeight - halfOfSlot
    maxHudWidthForAttacking = hudWidth - halfOfSlot
    xCoordinate = max(xCoordinate + halfOfSlot, halfOfSlot)
    xCoordinate = min(xCoordinate, maxHudWidthForAttacking)
    yCoordinate = max(yCoordinate + halfOfSlot, halfOfSlot)
    yCoordinate = min(yCoordinate, maxHudHeightForAttacking)
    windowCoordinate = (hudCoordinateX + xCoordinate,
                        hudCoordinateY + yCoordinate)
    hudCoordinate = (xCoordinate + hudMisalignmentX, yCoordinate + hudMisalignmentY)
    creature = (creatureName, creatureType, isBeingAttacked, slot,
                coordinate, windowCoordinate , hudCoordinate)
    return creature
