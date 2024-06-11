import math
from numba import njit
import numpy as np
import pathlib
from scipy.spatial import distance
import tcod
from typing import List, Tuple, Union
from src.repositories.radar.config import walkableFloorsSqms
from src.repositories.radar.core import isCoordinateWalkable
from src.shared.typings import Coordinate, GrayImage, Slot, SlotWidth, XYCoordinate
from src.utils.core import hashit
from src.utils.coordinate import getPixelFromCoordinate
from src.utils.image import loadFromRGBToGray
from src.utils.matrix import hasMatrixInsideOther
from src.wiki.creatures import creatures as wikiCreatures
from .typings import Creature, CreatureList


currentPath = pathlib.Path(__file__).parent.resolve()
resolutions = {
    720: {
        'gameWindowHeight': 352,
        'gameWindowWidth': 480,
        'slotWidth': 32,
    },
    1080: {
        'gameWindowHeight': 704,
        'gameWindowWidth': 960,
        'slotWidth': 64,
    },
}
creaturesNamesHashes = {}
for creature in wikiCreatures:
    creaturesNamesHashes[creature] = loadFromRGBToGray(
        f'{currentPath}/images/monsters/{creature}.png')


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getClosestCreature(gameWindowCreatures, coordinate: Coordinate):
    if len(gameWindowCreatures) == 0:
        return None
    if len(gameWindowCreatures) == 1:
        return gameWindowCreatures[0]
    gameWindowWalkableFloorsSqms = getGameWindowWalkableFloorsSqms(
        walkableFloorsSqms[coordinate[2]], coordinate)
    graph = tcod.path.SimpleGraph(
        cost=gameWindowWalkableFloorsSqms, cardinal=1, diagonal=0)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root((5, 7))
    closestCreatureSlot = None
    closestCreatureIndex = 0
    for creatureIndex, gameWindowCreature in enumerate(gameWindowCreatures):
        creatureSlot = (
            gameWindowCreature['slot'][1], gameWindowCreature['slot'][0])
        pf.resolve(creatureSlot)
        if closestCreatureSlot is None:
            closestCreatureSlot = creatureSlot
            continue
        if pf.distance[creatureSlot[0], creatureSlot[1]] < pf.distance[closestCreatureSlot[0], closestCreatureSlot[1]]:
            closestCreatureSlot = creatureSlot
            closestCreatureIndex = creatureIndex
    return gameWindowCreatures[closestCreatureIndex]


# TODO: add unit tests
# TODO: add perf
@njit(fastmath=True)
def getCreaturesBars(gameWindowImage: GrayImage) -> List[tuple[int, int]]:
    bars = []
    width = gameWindowImage.shape[1] - 27
    height = gameWindowImage.shape[0] - 3
    creatureIndex = 0
    for y in range(height):
        x = -1
        while x < width:
            x += 1
            if gameWindowImage[y, x + 26] != 0:
                x += 26
                continue
            bothBordersAreBlack = True
            for l in range(25):
                key = x + 25 - l
                if gameWindowImage[y, key] != 0 or gameWindowImage[y + 3, key] != 0:
                    bothBordersAreBlack = False
                    x = key
                    break
            if bothBordersAreBlack == False:
                continue
            if (
                gameWindowImage[y + 1, x] != 0 or
                gameWindowImage[y + 2, x] != 0 or
                gameWindowImage[y + 1, x + 26] != 0 or
                gameWindowImage[y + 2, x + 26] != 0
            ):
                continue
            bars.append((x, y))
            creatureIndex += 1
            x += 26
    return bars


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
# TODO: add name missAlignment for each creature, it avoid possible 3 calculations
# TODO: maximum creatures allowed should be equal battle list size
# TODO: Find a way to avoid 3 calculation times when comparing names since some words have a wrong location
# TODO: Whenever the last species is left, avoid loops and resolve species immediately for remaining creatures bars
def getCreatures(battleListCreatures, direction, gameWindowCoordinate: XYCoordinate, gameWindowImage: GrayImage, coordinate: Coordinate, beingAttackedCreatureCategory: str = None, walkedPixelsInSqm: int = 0):
    if len(battleListCreatures) == 0:
        return []
    creaturesBars = getCreaturesBars(gameWindowImage)
    if len(creaturesBars) == 0:
        return []
    creatures = []
    gameWindowWidth = len(gameWindowImage[1])
    x = (len(gameWindowImage[1]) / 2) - 1
    y = (len(gameWindowImage[0]) / 2) - 1
    slotWidth = len(gameWindowImage[1]) // 15
    sqrt = np.array([
        math.sqrt(((creatureBar[0] - x) ** 2) + ((creatureBar[1] - y) ** 2)) for creatureBar in creaturesBars], dtype=np.float64)
    creaturesBarsSortedIndexes = np.argsort(sqrt)
    discoverTarget = beingAttackedCreatureCategory is not None
    nonCreaturesForCurrentBar = {}
    for creatureBarSortedIndex in creaturesBarsSortedIndexes:
        for battleListIndex in range(len(battleListCreatures)):
            creatureName = battleListCreatures[battleListIndex]['name']
            if creatureName == 'Unknown':
                creature = makeCreature(creatureName, 'player', creaturesBars[creatureBarSortedIndex], direction, gameWindowCoordinate, gameWindowImage,
                                        coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature['isBeingAttacked']:
                    discoverTarget = False
                creatures.append(creature)
                break
            if nonCreaturesForCurrentBar.get(creatureName, None) is not None:
                continue
            creatureNameImg = creaturesNamesHashes.get(creatureName)
            (creatureBarX,
             creatureBarY) = creaturesBars[creatureBarSortedIndex]
            creatureBarY0 = creatureBarY - 13
            creatureBarY1 = creatureBarY0 + 11
            creatureNameImgHalfWidth = math.floor(creatureNameImg.shape[1] / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBarX > leftDiff else leftDiff - creatureBarX
            gapInnerLeft = 0 if creatureNameImg.shape[1] > 27 else math.ceil(
                (27 - creatureNameImg.shape[1]) / 2)
            rightDiff = max(
                creatureNameImg.shape[1] - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if gameWindowWidth > (
                creatureBarX + 27 + rightDiff) else creatureBarX + 27 + rightDiff - gameWindowWidth
            gapInnerRight = 0 if creatureNameImg.shape[1] > 27 else math.floor(
                (27 - creatureNameImg.shape[1]) / 2)
            gg = 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            startingX = max(0, creatureBarX - creatureNameImgHalfWidth + gg)
            endingX = min(gameWindowWidth, creatureBarX +
                          creatureNameImgHalfWidth + gg)
            creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                      startingX:endingX]
            if creatureNameImg.shape[1] != creatureWithDirtNameImg.shape[1]:
                creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                          startingX:endingX + 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg, creatureNameImg):
                creature = makeCreature(creatureName, 'monster', creaturesBars[creatureBarSortedIndex], direction, gameWindowCoordinate, gameWindowImage,
                                        coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature['isBeingAttacked']:
                    discoverTarget = False
                creatures.append(creature)
                break
            creatureNameImg2 = creaturesNamesHashes.get(creatureName)
            creatureWithDirtNameImg2 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX + 1:endingX + 1]
            if creatureNameImg2.shape[1] != creatureWithDirtNameImg2.shape[1]:
                creatureNameImg2 = creatureNameImg2[:,
                                                    0:creatureNameImg2.shape[1] - 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg2, creatureNameImg2):
                creature = makeCreature(creatureName, 'monster', creaturesBars[creatureBarSortedIndex], direction, gameWindowCoordinate, gameWindowImage,
                                        coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature['isBeingAttacked']:
                    discoverTarget = False
                creatures.append(creature)
                break
            creatureWithDirtNameImg3 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX:endingX - 1]
            creatureNameImg3 = creaturesNamesHashes.get(creatureName)
            creatureNameImg3 = creatureNameImg3[:, 1:creatureNameImg3.shape[1]]
            if creatureWithDirtNameImg3.shape[1] != creatureNameImg3.shape[1]:
                creatureNameImg3 = creatureNameImg3[:,
                                                    0:creatureNameImg3.shape[1] - 1]
            if hasMatrixInsideOther(creatureWithDirtNameImg3, creatureNameImg3):
                creature = makeCreature(creatureName, 'monster', creaturesBars[creatureBarSortedIndex], direction, gameWindowCoordinate, gameWindowImage,
                                        coordinate, slotWidth, discoverTarget=discoverTarget, beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=walkedPixelsInSqm)
                if creature['isBeingAttacked']:
                    discoverTarget = False
                creatures.append(creature)
                break
            nonCreaturesForCurrentBar[creatureName] = True
        nonCreaturesForCurrentBar.clear()
    return creatures


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getCreaturesByType(gameWindowCreatures: CreatureList, creatureType):
    return [gameWindowCreature for gameWindowCreature in gameWindowCreatures if gameWindowCreature['type'] == creatureType]


# TODO: add unit tests
# TODO: add perf
# TODO: improve performance
def getDifferentCreaturesBySlots(previousGameWindowCreatures: CreatureList, currentGameWindowCreatures: CreatureList, slots: List[Slot]) -> CreatureList:
    previousGameWindowCreaturesBySlots = np.array(
        [], dtype=Creature)
    currentGameWindowCreaturesBySlots = np.array(
        [], dtype=Creature)
    differentCreatures = np.array([], dtype=Creature)
    for previousGameWindowCreature in previousGameWindowCreatures:
        if np.isin(previousGameWindowCreature['slot'], slots).all():
            previousGameWindowCreaturesBySlots = np.append(
                previousGameWindowCreaturesBySlots, [previousGameWindowCreature])
    for currentGameWindowCreature in currentGameWindowCreatures:
        if np.isin(currentGameWindowCreature['slot'], slots).all():
            currentGameWindowCreaturesBySlots = np.append(
                currentGameWindowCreaturesBySlots, [currentGameWindowCreature])
    for previousGameWindowCreature in previousGameWindowCreaturesBySlots:
        creatureDoesNotExists = True
        for currentGameWindowCreature in currentGameWindowCreatures:
            previousGameWindowCreatureHash = hashit(
                previousGameWindowCreature)
            currentGameWindowCreatureHash = hashit(
                currentGameWindowCreature)
            if previousGameWindowCreatureHash == currentGameWindowCreatureHash:
                creatureDoesNotExists = False
                break
        if creatureDoesNotExists:
            differentCreatures = np.append(
                differentCreatures, [previousGameWindowCreature])
    return differentCreatures


# TODO: add unit tests
# TODO: add perf
def getGameWindowWalkableFloorsSqms(walkableFloorsSqms: np.ndarray, coordinate: Coordinate) -> np.ndarray:
    (xOfPixelCoordinate, yOfPixelCoordinate) = getPixelFromCoordinate(
        coordinate)
    return walkableFloorsSqms[yOfPixelCoordinate - 5:yOfPixelCoordinate + 6, xOfPixelCoordinate - 7:xOfPixelCoordinate + 8]


# TODO: add unit tests
# TODO: add perf
# TODO: if something is already compared, avoid it. Check if it is faster
# TODO: add types
def getNearestCreaturesCount(creatures) -> int:
    nearestCreaturesCount = 0
    for creature in creatures:
        if (creature['slot'][0] == 6 and creature['slot'][1] == 4) or (creature['slot'][0] == 7 and creature['slot'][1] == 4) or (creature['slot'][0] == 8 and creature['slot'][1] == 4) or (creature['slot'][0] == 6 and creature['slot'][1] == 5) or (creature['slot'][0] == 8 and creature['slot'][1] == 5) or (creature['slot'][0] == 6 and creature['slot'][1] == 6) or (creature['slot'][0] == 7 and creature['slot'][1] == 6) or (creature['slot'][0] == 8 and creature['slot'][1] == 6):
            nearestCreaturesCount += 1
    return nearestCreaturesCount


# TODO: add unit tests
# TODO: add perf
# TODO: add types
def getTargetCreature(gameWindowCreatures):
    if len(gameWindowCreatures) == 0:
        return None
    for gameWindowCreature in gameWindowCreatures:
        if gameWindowCreature['isBeingAttacked']:
            return gameWindowCreature


# TODO: add unit tests
# TODO: add perf
def hasTargetToCreatureBySlot(gameWindowCreatures: CreatureList, slot: Slot, coordinate: Coordinate) -> bool:
    if len(gameWindowCreatures) == 0:
        return False
    gameWindowWalkableFloorsSqms = getGameWindowWalkableFloorsSqms(
        walkableFloorsSqms[coordinate[2]], coordinate)
    slots = np.array([creature['slot'] for creature in gameWindowCreatures])
    creaturesSlots = slots[:, [1, 0]]
    gameWindowWalkableFloorsSqms[creaturesSlots[:,
                                                0], creaturesSlots[:, 1]] = 0
    gameWindowWalkableFloorsSqms[slot[1], slot[0]] = 1
    x = coordinate[0] + slot[0] - coordinate[0]
    y = coordinate[1] + slot[1] - coordinate[1]
    return len(tcod.path.AStar(gameWindowWalkableFloorsSqms, 0).get_path(5, 7, y, x)) > 0


# TODO: add unit tests
# TODO: add perf
def hasTargetToCreature(gameWindowCreatures: CreatureList, gameWindowCreature: Creature, coordinate: Coordinate) -> bool:
    return hasTargetToCreatureBySlot(
        gameWindowCreatures, gameWindowCreature['slot'], coordinate)


# TODO: add unit tests
# TODO: add perf
# TODO: is possible to do at same time since everything is 64 pixels or per type(horizontal, vertical) of bar
@njit(cache=True, fastmath=True)
def isCreatureBeingAttacked(gameWindowImage: GrayImage, borderX: int, yOfCreatureBar: int, slotWidth: int) -> bool:
    pixelsCount = 0
    borderedCreatureImg = gameWindowImage[yOfCreatureBar + 5:yOfCreatureBar +
                                          5 + slotWidth, borderX:borderX + slotWidth]
    borderGap = 4 if slotWidth == 64 else 2
    yOfBorder = slotWidth - borderGap
    topBorder = borderedCreatureImg[0:borderGap, :].flatten()
    bottomBorder = borderedCreatureImg[yOfBorder:, :].flatten()
    for i in range(len(topBorder)):
        if topBorder[i] == 76 or topBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
        if bottomBorder[i] == 76 or bottomBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
    leftBorder = borderedCreatureImg[borderGap:yOfBorder,
                                     0:borderGap].flatten()
    rightBorder = borderedCreatureImg[borderGap:yOfBorder, yOfBorder:].flatten(
    )
    for i in range(len(leftBorder)):
        if leftBorder[i] == 76 or leftBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
        if rightBorder[i] == 76 or rightBorder[i] == 166:
            pixelsCount += 1
            if pixelsCount > 50:
                return True
    return pixelsCount > 50


# TODO: add unit tests
# TODO: add perf
def isTrappedByCreatures(gameWindowCreatures: CreatureList, radarCoordinate: Coordinate) -> bool:
    pixelRadarCoordinate = getPixelFromCoordinate(radarCoordinate)
    playerBox = walkableFloorsSqms[radarCoordinate[2], pixelRadarCoordinate[1] -
                                   1: pixelRadarCoordinate[1] + 2, pixelRadarCoordinate[0] - 1: pixelRadarCoordinate[0] + 2]
    for gameWindowCreature in gameWindowCreatures:
        distanceOf = distance.cdist([gameWindowCreature['coordinate']], [
                                    radarCoordinate], 'euclidean').flatten()[0]
        if distanceOf < 1.42:
            x = gameWindowCreature['coordinate'][0] - radarCoordinate[0] + 1
            y = gameWindowCreature['coordinate'][1] - radarCoordinate[1] + 1
            playerBox[y, x] = 0
    if playerBox[0, 0] == 1:
        return False
    if playerBox[0, 1] == 1:
        return False
    if playerBox[0, 2] == 1:
        return False
    if playerBox[1, 0] == 1:
        return False
    if playerBox[1, 2] == 1:
        return False
    if playerBox[2, 0] == 1:
        return False
    if playerBox[2, 1] == 1:
        return False
    if playerBox[2, 2] == 1:
        return False
    return True


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
# TODO: windowCoordinate should be improved for gameWindow edges
# TODO: detect being attacked creature by category
# TODO: since there is only one creature in gameWindow and one in battleList being attacked, avoid computing if creature is being attacked on gameWindow
def makeCreature(creatureName: str, creatureType: str, creatureBar: Tuple[int, int], direction: str, gameWindowCoordinate: XYCoordinate, gameWindowImage: GrayImage, coordinate: Coordinate, slotWidth: SlotWidth, discoverTarget: bool = True, beingAttackedCreatureCategory: Union[str, None] = None, walkedPixelsInSqm: int = 0):
    isBigGameWindow = slotWidth == 64
    gameWindowMisalignment = {'x': 0, 'y': 0}
    if creatureType == 'monster':
        gameWindowMisalignment = wikiCreatures.get(creatureName).get(
            'gameWindowMisalignment', {'x': 0, 'y': 0})
    gameWindowMisalignmentX = gameWindowMisalignment[
        'x'] if isBigGameWindow else gameWindowMisalignment['x'] / 2
    gameWindowMisalignmentY = gameWindowMisalignment[
        'y'] if isBigGameWindow else gameWindowMisalignment['y'] / 2
    distanceBetweenSlotPixelLifeBar = 19 if isBigGameWindow else 3
    xCoordinate = creatureBar[0] - distanceBetweenSlotPixelLifeBar
    # xCoordinate = xCoordinate - walkedPixelsInSqm if direction == 'left' else xCoordinate + walkedPixelsInSqm
    xSlot = max(
        min(round((xCoordinate + gameWindowMisalignmentX) / slotWidth), 14), 0)
    yCoordinate = 0 if creatureBar[1] <= 14 else creatureBar[1] + 5
    ySlot = max(
        min(round((yCoordinate + gameWindowMisalignmentY) / slotWidth), 10), 0)
    borderX = max(creatureBar[0] - distanceBetweenSlotPixelLifeBar, 0)
    isBeingAttacked = False
    if discoverTarget and beingAttackedCreatureCategory is not None and beingAttackedCreatureCategory == creatureName:
        isBeingAttacked = isCreatureBeingAttacked(
            gameWindowImage, borderX, creatureBar[1], slotWidth)
    slot = (xSlot, ySlot)
    coordinate = [coordinate[0] - 7 + xSlot,
                  coordinate[1] - 5 + ySlot, coordinate[2]]
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
                rightCoordinate = [coordinate[0] +
                                   1, coordinate[1], coordinate[2]]
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
                bottomCoordinate = [coordinate[0],
                                    coordinate[1] + 1, coordinate[2]]
                if isCoordinateWalkable(bottomCoordinate):
                    coordinate = bottomCoordinate
                    ySlot = slot[1] + 1
                    ySlot = min(ySlot, 10)
                    ySlot = max(ySlot, 0)
                    slot = (slot[0], ySlot)
    halfOfSlot = (slotWidth / 2)
    xCoordinate = min(max(xCoordinate + halfOfSlot, halfOfSlot),
                      gameWindowImage.shape[1] - halfOfSlot)
    yCoordinate = min(max(yCoordinate + halfOfSlot, halfOfSlot),
                      gameWindowImage.shape[0] - halfOfSlot)
    windowCoordinate = (
        gameWindowCoordinate[0] + xCoordinate, gameWindowCoordinate[1] + yCoordinate)
    gameWindowCoordinate = (
        xCoordinate + gameWindowMisalignmentX, yCoordinate + gameWindowMisalignmentY)
    isUnderRoof = gameWindowImage[creatureBar[1] +
                                  1, creatureBar[0] + 1] == 192
    return {
        'name': creatureName,
        'type': creatureType,
        'isBeingAttacked': isBeingAttacked,
        'slot': slot,
        'coordinate': coordinate,
        'windowCoordinate': windowCoordinate,
        'gameWindowCoordinate': gameWindowCoordinate,
        'isUnderRoof': isUnderRoof
    }
