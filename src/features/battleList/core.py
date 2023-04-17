from numba import njit
import numpy as np
from typing import Generator, Union
from src.shared.typings import GrayImage
from src.utils.core import hashit, locate
from .config import creaturesNamesImagesHashes, skulls
from .extractors import getCreaturesNamesImages
from .typings import CreaturesList, Creature


# PERF: [0.13737060000000056, 4.999999987376214e-07]
@njit(cache=True, fastmath=True)
def getBeingAttackedCreatureCategory(creatures: CreaturesList) -> Union[str, None]:
    for creature in creatures:
        if creature['isBeingAttacked']:
            return creature['name']
    return None


# PERF: [1.3400000000274304e-05, 2.9000000001389026e-06]
@njit(cache=True, fastmath=True)
def getBeingAttackedCreatures(content: GrayImage, filledSlotsCount: int) -> Generator[bool, None, None]:
    alreadyCalculatedBeingAttackedCreature = False
    for creatureIndex in range(filledSlotsCount):
        contentIndex = creatureIndex * 22
        if alreadyCalculatedBeingAttackedCreature:
            yield False
        else:
            # detecting through corner pixels
            isBeingAttacked = (content[creatureIndex * 22, 0] == 76 or content[contentIndex, 0] == 166) and (content[contentIndex, 19] == 76 or content[contentIndex, 19] == 166) and (content[contentIndex + 19, 0] == 76 or content[contentIndex + 19, 0] == 166) and (content[contentIndex + 19, 19] == 76 or content[contentIndex + 19, 19] == 166)
            yield isBeingAttacked
            if isBeingAttacked:
                alreadyCalculatedBeingAttackedCreature = True


# PERF: [0.00017040000000001498, 7.330000000038694e-05]
def getCreatures(content: GrayImage) -> CreaturesList:
    filledSlotsCount = getFilledSlotsCount(content)
    if filledSlotsCount == 0:
        return np.array([], dtype=Creature)
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(content, filledSlotsCount)]
    creaturesNames = [creatureName for creatureName in getCreaturesNames(content, filledSlotsCount)]
    return np.array([(creatureName, beingAttackedCreatures[slotIndex])
                           for slotIndex, creatureName in enumerate(creaturesNames)], dtype=Creature)


# PERF: [0.019119499999998624, 4.020000000082291e-05]
def getCreaturesNames(content: GrayImage, filledSlotsCount: int) -> Generator[str, None, None]:
    for creatureNameImage in getCreaturesNamesImages(content, filledSlotsCount):
        yield creaturesNamesImagesHashes.get(hashit(creatureNameImage), 'Unknown')


# PERF: [0.5794668999999999, 3.9999999934536845e-07]
@njit(cache=True, fastmath=True)
def getFilledSlotsCount(content: GrayImage) -> int:
    filledSlotsCount = 0
    for slotIndex in range(len(content) // 22):
        y = 22 * slotIndex
        if content[:, 23][y + 11] == 192 or content[:, 23][y + 11] == 247:
            filledSlotsCount += 1
        elif content[:, 23][y + 10] == 192 or content[:, 23][y + 10] == 247:
            filledSlotsCount += 1
        elif content[:, 23][y + 4] == 192 or content[:, 23][y + 4] == 247:
            filledSlotsCount += 1
        elif content[:, 23][y + 5] == 192 or content[:, 23][y + 5] == 247:
            filledSlotsCount += 1
        else:
            break
    return filledSlotsCount


# PERF: [7.5999999999964984e-06, 7.999999986907369e-07]
def hasSkull(content: GrayImage, creatures: CreaturesList) -> bool:
    for creatureIndex, creature in enumerate(creatures):
        if creature['name'] != 'Unknown':
            continue
        y = (creatureIndex * 22)
        creatureIconsImage = content[y + 2:y + 13, -38:-2]
        if locate(creatureIconsImage, skulls['images']['black']):
            return True
        if locate(creatureIconsImage, skulls['images']['orange']):
            return True
        if locate(creatureIconsImage, skulls['images']['red']):
            return True
        if locate(creatureIconsImage, skulls['images']['white']):
            return True
        if locate(creatureIconsImage, skulls['images']['yellow']):
            return True
    return False


# PERF: [4.499999999296733e-06, 9.999999992515995e-07]
@njit(cache=True, fastmath=True)
def isAttackingSomeCreature(creatures: CreaturesList) -> bool:
    for isBeingAttacked in creatures['isBeingAttacked']:
        if isBeingAttacked:
            return True
    return False
