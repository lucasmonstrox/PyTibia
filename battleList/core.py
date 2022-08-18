import numpy as np
from . import config, extractors
from battleList.typing import creatureType
import utils.core


def getCreatures(screenshot):
    content = extractors.getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    creatures = np.array([], dtype=creatureType)
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    hasNoFilledSlots = filledSlotsCount == 0
    if hasNoFilledSlots:
        return creatures
    for slotIndex in np.arange(filledSlotsCount):
        creature = np.array(getCreatureFromSlot(
            content, slotIndex), dtype=creatureType)
        creatures = np.append(creatures, [creature])
    return creatures


# TODO: add unit tests
# TODO: everything(upper border of creature icon, creature name) can be resolved using parallel code
def getCreatureFromSlot(content, slotIndex):
    slotImg = extractors.getCreatureSlotImg(content, slotIndex)
    isBeingAttacked = isCreatureBeingAttacked(slotImg)
    creatureNameImg = extractors.getCreatureNameImg(slotImg)
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    unknownCreature = not creatureNameImgHash in config.creatures["nameImgHashes"]
    if unknownCreature:
        return ("Unknown", isBeingAttacked)
    creatureName = config.creatures["nameImgHashes"][creatureNameImgHash]
    return (creatureName, isBeingAttacked)


def isAttackingSomeCreature(creatures):
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature


def isCreatureBeingAttacked(slotImg):
    attackColor = 76
    highlightedAttackColor = 166
    upperBorderOfCreatureIcon = extractors.getUpperBorderOfCreatureIcon(
        slotImg)
    isCreatureBeingAttacked = np.all(np.logical_or(
        upperBorderOfCreatureIcon == attackColor, upperBorderOfCreatureIcon == highlightedAttackColor))
    return isCreatureBeingAttacked
