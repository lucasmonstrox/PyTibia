
import numpy as np
from . import config, extractors
from battleList.typing import creatureType
import utils.image
import utils.core


def getCreatures(screenshot):
    content = extractors.getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    hasNoCreatures = filledSlotsCount == 0
    if hasNoCreatures:
        return np.array([], dtype=creatureType)
    beingAttackedCreatures = extractors.getBeingAttackedCreatures(content, filledSlotsCount)
    creaturesNamesImages = extractors.getCreaturesNamesImages(content, filledSlotsCount)
    creatures = [(getCreatureName(creatureNameImage), beingAttackedCreatures[slotIndex])
                           for slotIndex, creatureNameImage in enumerate(creaturesNamesImages)]
    creaturesNp = np.array(creatures, dtype=creatureType)
    return creaturesNp


def getCreatureName(creatureNameImg):
    creatureNameImgNp = np.array(creatureNameImg, dtype=np.uint8)
    creatureNameImgHash = utils.core.hashit(creatureNameImgNp)
    creatureName = config.creatures['nameImgHashes'].get(creatureNameImgHash, 'Unknown')
    return creatureName


def isAttackingSomeCreature(creatures):
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature
