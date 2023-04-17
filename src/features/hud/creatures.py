import math
from numba import njit
import numpy as np
import pathlib
import tcod
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from src.features.radar.config import walkableFloorsSqms
from src.features.radar.core import isCoordinateWalkable
from src.utils.core import getPixelFromCoordinate, hashitHex
from src.utils.image import loadAsGrey
from src.utils.matrix import getAdjacencyMatrix, hasMatrixInsideOther
from src.wiki.creatures import creatures as wikiCreatures
from .typings import creatureType


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
    creaturesNamesHashes[creature] = loadAsGrey(
        f'{currentPath}/images/monsters/{creature}.png')


# TODO: improve performance
def getClosestCreature(hudCreatures, coordinate):
    if len(hudCreatures) == 0:
        return None
    hudWalkableFloorsSqms = getHudWalkableFloorsSqms(
        walkableFloorsSqms[coordinate[2]], coordinate)
    adjacencyMatrix = getAdjacencyMatrix(hudWalkableFloorsSqms)
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
    for j in range(imgHeight - 3):
        i = -1
        while(i < (imgWidth - 27)):
            i += 1
            if hudImg[j, i + 26] == 0:
                if hudImg[j, i] == 0:
                    upperBorderIsBlack = True
                    bottomBorderIsBlack = True
                    # detecting upper/bottom black borders
                    for l in range(25):
                        if hudImg[j, i + 25 - l] != 0:
                            upperBorderIsBlack = False
                            i += 25 - l
                            break
                        if hudImg[j + 3, i + 25 - l] != 0:
                            bottomBorderIsBlack = False
                            i += 25 - l
                            break
                    if upperBorderIsBlack == False or bottomBorderIsBlack == False:
                        continue
                    # detecting left/right bars
                    if hudImg[j + 1, i] != 0 or hudImg[j + 2, i] != 0 or hudImg[j + 1, i + 26] != 0 or hudImg[j + 2, i + 26] != 0:
                        continue
                    yield (i, j)
                    i += 26
            else:
                i += 26


# TODO: add name missAlignment for each creature, it avoid possible 3 calculations
# TODO: maximum creatures allowed should be equal battle list size
# TODO: Find a way to avoid 3 calculation times when comparing names since some words have a wrong location
# TODO: Whenever the last species is left, avoid loops and resolve species immediately for remaining creatures bars
def getCreatures(battleListCreatures, direction, hudCoordinate, hudImg, coordinate, beingAttackedCreatureCategory=None, walkedPixelsInSqm=0):
    if len(battleListCreatures) == 0:
        return np.array([], dtype=creatureType)
    creaturesBars = [creatureBar for creatureBar in getCreaturesBars(hudImg)]
    if len(creaturesBars) == 0:
        return np.array([], dtype=creatureType)
    creatures = []
    # creatures = [None] * len(creaturesBars)
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
    discoverTarget = beingAttackedCreatureCategory is not None
    battleListStartIndex = 0
    for creatureBarSortedIndex in creaturesBarsSortedIndexes:
        nonCreaturesForCurrentBar = {}
        for battleListIndex in range(battleListStartIndex, len(battleListCreatures)):
            if battleListCreatures[battleListIndex]['name'] == 'Unknown':
                creature = makeCreature(battleListCreatures[battleListIndex]['name'], 'player', creaturesBars[creatureBarSortedIndex], direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListStartIndex += 1
                break
            if nonCreaturesForCurrentBar.get(battleListCreatures[battleListIndex]['name'], None) is not None:
                continue
            creatureNameImg = creaturesNamesHashes.get(battleListCreatures[battleListIndex]['name'])
            (creatureBarX, creatureBarY) = creaturesBars[creatureBarSortedIndex]
            creatureBarY0 = creatureBarY - 13
            creatureBarY1 = creatureBarY0 + 11
            creatureNameImgHalfWidth = math.floor(creatureNameImg.shape[1] / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBarX > leftDiff else leftDiff - creatureBarX
            gapInnerLeft = 0 if creatureNameImg.shape[1] > 27 else math.ceil((27 - creatureNameImg.shape[1]) / 2)
            rightDiff = max(creatureNameImg.shape[1] - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if hudWidth > (creatureBarX + 27 + rightDiff) else creatureBarX + 27 + rightDiff - hudWidth
            gapInnerRight = 0 if creatureNameImg.shape[1] > 27 else math.floor((27 - creatureNameImg.shape[1]) / 2)
            gg = 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            startingX = max(0, creatureBarX - creatureNameImgHalfWidth + gg)
            endingX = min(hudWidth, creatureBarX + creatureNameImgHalfWidth + gg)
            creatureWithDirtNameImg = hudImg[creatureBarY0:creatureBarY1, startingX:endingX]
            if creatureNameImg.shape[1] != creatureWithDirtNameImg.shape[1]:
                creatureWithDirtNameImg = hudImg[creatureBarY0:creatureBarY1, startingX:endingX + 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg, creatureNameImg):
                creature = makeCreature(battleListCreatures[battleListIndex]['name'], 'monster', creaturesBars[creatureBarSortedIndex], direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListStartIndex += 1
                break
            creatureNameImg2 = creaturesNamesHashes.get(battleListCreatures[battleListIndex]['name'])
            creatureWithDirtNameImg2 = hudImg[creatureBarY0:creatureBarY1, startingX + 1:endingX + 1]
            if creatureNameImg2.shape[1] != creatureWithDirtNameImg2.shape[1]:
                creatureNameImg2 = creatureNameImg2[:, 0:creatureNameImg2.shape[1] - 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg2, creatureNameImg2):
                creature = makeCreature(battleListCreatures[battleListIndex]['name'], 'monster', creaturesBars[creatureBarSortedIndex], direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature[2]:
                    discoverTarget = False
                creatures.append(creature)
                battleListStartIndex += 1
                break
            creatureWithDirtNameImg3 = hudImg[creatureBarY0:creatureBarY1, startingX:endingX - 1]
            creatureNameImg3 = creaturesNamesHashes.get(battleListCreatures[battleListIndex]['name'])
            creatureNameImg3 = creatureNameImg3[:, 1:creatureNameImg3.shape[1]]
            if creatureWithDirtNameImg3.shape[1] != creatureNameImg3.shape[1]:
                creatureNameImg3 = creatureNameImg3[:, 0:creatureNameImg3.shape[1] - 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg3, creatureNameImg3):
                creature = makeCreature(battleListCreatures[battleListIndex]['name'], 'monster', creaturesBars[creatureBarSortedIndex], direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature[2]:
                    discoverTarget = False
                # creatures[creaturesIndex] = creature
                # creaturesIndex += 1
                creatures.append(creature)
                battleListStartIndex += 1
                break
            nonCreaturesForCurrentBar[battleListCreatures[battleListIndex]['name']] = True
    return np.array(creatures, dtype=creatureType)


# TODO: change to for loop with numba
def getCreaturesByType(hudCreatures, creatureType):
    return hudCreatures[hudCreatures['type'] == creatureType]


def getCreaturesGraph(hudCreatures, coordinate):
    floorLevel = hudCreatures[0]['coordinate'][2]
    walkableFloorsSqms = walkableFloorsSqms[floorLevel]
    hudWalkableFloorsSqms = getHudWalkableFloorsSqms(
        walkableFloorsSqms, coordinate)
    adjacencyMatrix = getAdjacencyMatrix(hudWalkableFloorsSqms)
    graph = csr_matrix(adjacencyMatrix)
    playerHudIndex = 82
    graphWeights = dijkstra(graph, directed=True, indices=playerHudIndex, unweighted=False)
    graphWeights = graphWeights.reshape(11, 15)
    availableCreatures = [hudCreature for hudCreature in hudCreatures if graphWeights[hudCreature['slot'][1], hudCreature['slot'][0]] != np.inf]
    return np.array(availableCreatures, dtype=creatureType)


# TODO: improve performance
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
            previousHudCreatureHash = hashitHex(
                previousHudCreature)
            currentHudCreatureHash = hashitHex(
                currentHudCreature)
            if previousHudCreatureHash == currentHudCreatureHash:
                creatureDoesNotExists = False
                break
        if creatureDoesNotExists:
            differentCreatures = np.append(
                differentCreatures, [previousHudCreature])
    return differentCreatures


def getHudWalkableFloorsSqms(walkableFloorsSqms, coordinate):
    (xOfPixelCoordinate, yOfPixelCoordinate) = getPixelFromCoordinate(
        coordinate)
    return walkableFloorsSqms[yOfPixelCoordinate -
                                               5:yOfPixelCoordinate+6, xOfPixelCoordinate-7:xOfPixelCoordinate+8].copy()


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
    if len(hudCreatures) == 0:
        return None
    for hudCreature in hudCreatures:
        if hudCreature['isBeingAttacked']:
            return hudCreature


def hasTargetToCreatureBySlot(hudCreatures, slot, coordinate):
    if len(hudCreatures) == 0:
        return False
    xOfCoordinate, yOfCoordinate, floorLevel = coordinate
    hudWalkableFloorsSqms = getHudWalkableFloorsSqms(
        walkableFloorsSqms[floorLevel], coordinate)
    creaturesSlots = hudCreatures['slot'][:, [1, 0]]
    hudWalkableFloorsSqms[creaturesSlots[:, 0], creaturesSlots[:, 1]] = 0
    hudWalkableFloorsSqms[slot[1], slot[0]] = 1
    pf = tcod.path.AStar(hudWalkableFloorsSqms, 0)
    xOfGoalCoordinate = coordinate[0] + slot[0] - 7
    yOfGoalCoordinate = coordinate[1] + slot[1] - 5
    x = xOfGoalCoordinate - xOfCoordinate + 7
    y = yOfGoalCoordinate - yOfCoordinate + 5
    paths = pf.get_path(5, 7, y, x)
    walkpoints = [[xOfCoordinate + x - 7,
                   yOfCoordinate + y - 5, floorLevel] for y, x in paths]
    return len(walkpoints) > 0


def hasTargetToCreature(hudCreatures, hudCreature, coordinate):
    hasTarget = hasTargetToCreatureBySlot(
        hudCreatures, hudCreature['slot'], coordinate)
    return hasTarget


# TODO: is possible to do at same time since everything is 64 pixels or per type(horizontal, vertical) of bar
@njit(cache=True, fastmath=True)
def isCreatureBeingAttacked(hudImg, borderX, yOfCreatureBar, slotWidth):
    pixelsCount = 0
    borderedCreatureImg = hudImg[yOfCreatureBar + 5:yOfCreatureBar +
                                    5 + slotWidth, borderX:borderX + slotWidth]
    borderGap = 4 if slotWidth == 64 else 2
    yOfBorder = slotWidth - borderGap
    topBorder = borderedCreatureImg[0:borderGap, :].flatten()
    for i in range(len(topBorder)):
        if topBorder[i] == 76 or topBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
    leftBorder = borderedCreatureImg[borderGap:yOfBorder, 0:borderGap].flatten()
    for i in range(len(leftBorder)):
        if leftBorder[i] == 76 or leftBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
    rightBorder = borderedCreatureImg[borderGap:yOfBorder, yOfBorder:].flatten()
    for i in range(len(rightBorder)):
        if rightBorder[i] == 76 or rightBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
    bottomBorder = borderedCreatureImg[yOfBorder:, :].flatten()
    for i in range(len(bottomBorder)):
        if bottomBorder[i] == 76 or bottomBorder[i] == 166:
            pixelsCount += 1
    return pixelsCount > 50


# TODO: windowCoordinate should be improved for hud edges
# TODO: detect being attacked creature by category
# TODO: since there is only one creature in hud and one in battleList being attacked, avoid computing if creature is being attacked on hud
def makeCreature(creatureName, creatureType, creatureBar, direction, hudCoordinate, hudImg, coordinate, slotWidth, discoverTarget=True, beingAttackedCreatureCategory=None, walkedPixelsInSqm=0):
    isBigHud = slotWidth == 64
    hudMisalignment = {'x': 0, 'y': 0}
    if creatureType == 'monster':
        hudMisalignment = wikiCreatures.get(creatureName).get('hudMisalignment', {'x': 0, 'y': 0})
    hudMisalignmentX = hudMisalignment['x'] if isBigHud else hudMisalignment['x'] / 2
    hudMisalignmentY = hudMisalignment['y'] if isBigHud else hudMisalignment['y'] / 2
    distanceBetweenSlotPixelLifeBar = 19 if isBigHud else 3
    xCoordinate = creatureBar[0] - distanceBetweenSlotPixelLifeBar
    # xCoordinate = xCoordinate - walkedPixelsInSqm if direction == 'left' else xCoordinate + walkedPixelsInSqm
    xSlot = max(min(round((xCoordinate + hudMisalignmentX) / slotWidth), 14), 0)
    yCoordinate = 0 if creatureBar[1] <= 14 else creatureBar[1] + 5
    ySlot = max(min(round((yCoordinate + hudMisalignmentY) / slotWidth), 10), 0)
    borderX = max(creatureBar[0] - distanceBetweenSlotPixelLifeBar, 0)
    isBeingAttacked = False
    if discoverTarget and beingAttackedCreatureCategory is not None and beingAttackedCreatureCategory == creatureName:
        isBeingAttacked = isCreatureBeingAttacked(hudImg, borderX, creatureBar[1], slotWidth)
    slot = (xSlot, ySlot)
    coordinate = [coordinate[0] - 7 + xSlot, coordinate[1] - 5 + ySlot, coordinate[2]]
    if not isCoordinateWalkable(coordinate):
        if direction == 'left' or direction == 'right':
            leftCoordinate = [coordinate[0] - 1, coordinate[1], coordinate[2]]
            if isCoordinateWalkable(leftCoordinate):
                coordinate = leftCoordinate
                xSlot = slot[0] - 1
                xSlot = min(xSlot, 14)
                xSlot = max(xSlot, 0)
                slot = (xSlot, slot[1])
            else:
                rightCoordinate = [coordinate[0] + 1, coordinate[1], coordinate[2]]
                if isCoordinateWalkable(rightCoordinate):
                    coordinate = rightCoordinate
                    xSlot = slot[0] + 1
                    xSlot = min(xSlot, 14)
                    xSlot = max(xSlot, 0)
                    slot = (xSlot, slot[1])
        if direction == 'top' or direction == 'bottom':
            topCoordinate = [coordinate[0], coordinate[1] - 1, coordinate[2]]
            if isCoordinateWalkable(topCoordinate):
                coordinate = topCoordinate
                ySlot = slot[1] - 1
                ySlot = min(ySlot, 10)
                ySlot = max(ySlot, 0)
                slot = (slot[0], ySlot)
            else:
                bottomCoordinate = [coordinate[0], coordinate[1] + 1, coordinate[2]]
                if isCoordinateWalkable(bottomCoordinate):
                    coordinate = bottomCoordinate
                    ySlot = slot[1] + 1
                    ySlot = min(ySlot, 10)
                    ySlot = max(ySlot, 0)
                    slot = (slot[0], ySlot)
    halfOfSlot = (slotWidth / 2)
    xCoordinate = min(max(xCoordinate + halfOfSlot, halfOfSlot), hudImg.shape[1] - halfOfSlot)
    yCoordinate = min(max(yCoordinate + halfOfSlot, halfOfSlot), hudImg.shape[0] - halfOfSlot)
    windowCoordinate = (hudCoordinate[0] + xCoordinate, hudCoordinate[1] + yCoordinate)
    hudCoordinate = (xCoordinate + hudMisalignmentX, yCoordinate + hudMisalignmentY)
    return (creatureName, creatureType, isBeingAttacked, slot, coordinate, windowCoordinate , hudCoordinate)
