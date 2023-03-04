import numpy as np
import utils.core
from . import config, extractors, typing


def getCreatures(screenshot):
    content = extractors.getContent(screenshot)
    if content is None:
        return None
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    if filledSlotsCount == 0:
        return np.array([], dtype=typing.creatureType)
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in extractors.getBeingAttackedCreatures(content, filledSlotsCount)]
    creatures = [(getCreatureName(creatureNameImage), beingAttackedCreatures[slotIndex], slotIndex)
                           for slotIndex, creatureNameImage in enumerate(extractors.getCreaturesNamesImages(content, filledSlotsCount))]
    return np.array(creatures, dtype=typing.creatureType)


def getIconsRegionByCreatureIndex(content, creatureIndex):
    y = (creatureIndex * 22)
    return content[y + 2:y + 13, -38:-2]


def getCreatureName(creatureNameImg):
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatureName = config.creatures['nameImgHashes'].get(creatureNameImgHash, 'Unknown')
    return creatureName


def hasSkull(screenshot, creatures):
    content = extractors.getContent(screenshot)
    if content is None:
        return None
    for creature in creatures:
        if creature['name'] != 'Unknown':
            continue
        creatureIconsImage = getIconsRegionByCreatureIndex(content, creature['index'])
        if utils.core.locate(creatureIconsImage, config.skulls['images']['black']):
            return True
        if utils.core.locate(creatureIconsImage, config.skulls['images']['orange']):
            return True
        if utils.core.locate(creatureIconsImage, config.skulls['images']['red']):
            return True
        if utils.core.locate(creatureIconsImage, config.skulls['images']['white']):
            return True
        if utils.core.locate(creatureIconsImage, config.skulls['images']['yellow']):
            return True
    return False


def isAttackingSomeCreature(creatures):
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature
