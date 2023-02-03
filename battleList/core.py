from numba import njit, types
from numba.extending import overload, register_jitable
from numba.core.errors import TypingError
import numpy as np
from . import config, extractors
from battleList.typing import creatureType
import utils.core
import utils.image


@overload(np.all)
def np_all(x, axis=None):

    # ndarray.all with axis arguments for 2D arrays.

    @register_jitable
    def _np_all_axis0(arr):
        out = np.logical_and(arr[0], arr[1])
        for v in iter(arr[2:]):
            for idx, v_2 in enumerate(v):
                out[idx] = np.logical_and(v_2, out[idx])
        return out

    @register_jitable
    def _np_all_flat(x):
        out = x.all()
        return out

    @register_jitable
    def _np_all_axis1(arr):
        out = np.logical_and(arr[:, 0], arr[:, 1])
        for idx, v in enumerate(arr[:, 2:]):
            for v_2 in iter(v):
                out[idx] = np.logical_and(v_2, out[idx])
        return out

    if isinstance(axis, types.Optional):
        axis = axis.type

    if not isinstance(axis, (types.Integer, types.NoneType)):
        raise TypingError("'axis' must be 0, 1, or None")

    if not isinstance(x, types.Array):
        raise TypingError("Only accepts NumPy ndarray")

    if not (1 <= x.ndim <= 2):
        raise TypingError("Only supports 1D or 2D NumPy ndarrays")

    if isinstance(axis, types.NoneType):

        def _np_all_impl(x, axis=None):
            return _np_all_flat(x)

        return _np_all_impl

    elif x.ndim == 1:

        def _np_all_impl(x, axis=None):
            return _np_all_flat(x)

        return _np_all_impl

    elif x.ndim == 2:

        def _np_all_impl(x, axis=None):
            if axis == 0:
                return _np_all_axis0(x)
            else:
                return _np_all_axis1(x)

        return _np_all_impl

    else:

        def _np_all_impl(x, axis=None):
            return _np_all_flat(x)

        return _np_all_impl


def getCreatures(screenshot, content):
    # content = extractors.getContent(screenshot)
    # cannotGetContent = content is None
    # if cannotGetContent:
    #     return None
    filledSlotsCount = extractors.getFilledSlotsCount(content)
    beingAttackedCreatures = getBeingAttackedCreatures(content, filledSlotsCount)
    creaturesNames = getCreaturesNames(content, filledSlotsCount)
    creaturesWithoutType = np.column_stack((creaturesNames, beingAttackedCreatures))
    creatures = np.array(creaturesWithoutType)
    return creatures

contentSize = 156
gapBetweenSlots = 22
cenas = gapBetweenSlots * contentSize
topBorderSizeOfCreatureIcon = 20
xArray = np.arange(topBorderSizeOfCreatureIcon)


def getCreaturesNames(content, filledSlotsCount):
    # TODO: parallelize
    creaturesNames = [utils.core.hashit(np.ones((156, 20))) for i in range(filledSlotsCount)]
    return np.array(creaturesNames)


@njit(cache=True, fastmath=True)
def getBeingAttackedCreatures(content, filledSlotsCount):
    coordinatesOfTopBordersOfCreaturesIcons = np.broadcast_to(
        xArray, (filledSlotsCount, topBorderSizeOfCreatureIcon))
    yArray = np.arange(filledSlotsCount)
    zArray = np.broadcast_to(yArray, (topBorderSizeOfCreatureIcon, filledSlotsCount))
    yArray2 = zArray.T * cenas
    indices = coordinatesOfTopBordersOfCreaturesIcons + yArray2
    fa = np.take(content, indices)
    fe = np.logical_or(fa == 76, fa == 166)
    beingAttackedCreatures = np.all(fe, axis=1)
    return beingAttackedCreatures


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
