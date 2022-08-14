import numpy as np
from . import config, extractors
from battleList.typing import creatureType, CREATURE, CREATURE_LIST, SLOT_IMG
from core.typing import UINT8_NDARRAY
import utils.core


def getCreatures(screenshot: UINT8_NDARRAY) -> CREATURE_LIST:
    content = extractors.getContent(screenshot)
    cannotGetContent = content is None
    if cannotGetContent:
        return None
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    creatures = np.array([getCreatureFromSlot(content, slotIndex)
                          for slotIndex in np.arange(filledSlotsCount)], dtype=creatureType)
    return creatures


# TODO: add unit tests
# TODO: everything(upper border of creature icon, creature name) can be resolved using parallel code
def getCreatureFromSlot(content: UINT8_NDARRAY, slotIndex: int) -> CREATURE:
    slotImg = extractors.getCreatureSlotImg(content, slotIndex)
    isBeingAttacked = isCreatureBeingAttacked(slotImg)
    creatureNameImg = extractors.getCreatureNameImg(slotImg)
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    unknownCreature = not creatureNameImgHash in config.creatures["nameImgHashes"]
    if unknownCreature:
        return ("Unknown", isBeingAttacked)
    creatureName = config.creatures["nameImgHashes"][creatureNameImgHash]
    return (creatureName, isBeingAttacked)


def isAttackingSomeCreature(creatures: CREATURE_LIST) -> bool:
    isAttackingSomeCreature = np.any(creatures['isBeingAttacked'] == True)
    return isAttackingSomeCreature


def isCreatureBeingAttacked(slotImg: SLOT_IMG) -> bool:
    attackColor = 76
    highlightedAttackColor = 166
    upperBorderOfCreatureIcon = extractors.getUpperBorderOfCreatureIcon(
        slotImg)
    isCreatureBeingAttacked = np.all(np.logical_or(
        upperBorderOfCreatureIcon == attackColor, upperBorderOfCreatureIcon == highlightedAttackColor))
    return isCreatureBeingAttacked
