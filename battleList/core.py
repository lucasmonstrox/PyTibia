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
    creatures = [(getCreatureName(creatureNameImage), beingAttackedCreatures[slotIndex])
                           for slotIndex, creatureNameImage in enumerate(extractors.getCreaturesNamesImages(content, filledSlotsCount))]
    return np.array(creatures, dtype=typing.creatureType)


def getCreatureName(creatureNameImg):
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatureName = config.creatures['nameImgHashes'].get(creatureNameImgHash, 'Unknown')
    return creatureName


def isAttackingSomeCreature(creatures):
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature
