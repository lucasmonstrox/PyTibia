import numpy as np
import utils.core
from . import config, extractors, typing


def getCreatures(screenshot):
    content = extractors.getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    hasNoCreatures = filledSlotsCount == 0
    if hasNoCreatures:
        return np.array([], dtype=typing.creatureType)
    beingAttackedCreatures = extractors.getBeingAttackedCreatures(content, filledSlotsCount)
    creaturesNamesImages = extractors.getCreaturesNamesImages(content, filledSlotsCount)
    creatures = [(getCreatureName(creatureNameImage), beingAttackedCreatures[slotIndex])
                           for slotIndex, creatureNameImage in enumerate(creaturesNamesImages)]
    creaturesNp = np.array(creatures, dtype=typing.creatureType)
    return creaturesNp


def getCreatureName(creatureNameImg):
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatureName = config.creatures['nameImgHashes'].get(creatureNameImgHash, 'Unknown')
    return creatureName


def isAttackingSomeCreature(creatures):
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature
