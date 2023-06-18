import math
from typing import Union
import src.repositories.actionBar.extractors as actionBarExtractors
import src.repositories.actionBar.locators as actionBarLocators
from src.shared.typings import GrayImage
import src.utils.core as coreUtils
from .config import images


# TODO: add unit tests
# PERF: [0.04209370000000012, 9.999999999621423e-06]
def getSlotCount(screenshot: GrayImage, slot: int) -> Union[int, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    x0 = leftSideArrowsPos[0] + leftSideArrowsPos[2] + \
        (slot * 2) + ((slot - 1) * 34)
    slotImage = screenshot[leftSideArrowsPos[1]
        :leftSideArrowsPos[1] + 34, x0:x0 + 34]
    digits = slotImage[24:32, 3:33]
    count = 0
    for i in range(5):
        x = (6 * (5 - i) - 3)
        number = images['digits'].get(
            coreUtils.hashit(digits[2:6, x:x + 1]), None)
        if number is None:
            break
        count += number * math.pow(10, i)
    return int(count)


# PERF: [0.08509680000000008, 0.00037780000000031677]
def hasCooldownByImage(screenshot: GrayImage, cooldownImage: GrayImage) -> Union[bool, None]:
    listOfCooldownsImage = actionBarExtractors.getCooldownsImage(screenshot)
    if listOfCooldownsImage is None:
        return None
    cooldownImagePosition = coreUtils.locate(
        listOfCooldownsImage, cooldownImage)
    if cooldownImagePosition is None:
        return False
    return listOfCooldownsImage[20:21, cooldownImagePosition[0]:cooldownImagePosition[0] + cooldownImagePosition[2]][0][0] == 255


# TODO: add unit tests
# PERF: [0.08509680000000008, 0.00037780000000031677]
def hasCooldownByName(screenshot: GrayImage, name: str) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns'][name])


# TODO: improve performance
# PERF: [0.08509680000000008, 0.00037780000000031677]
def hasAttackCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['attack'])


# TODO: improve performance
# PERF: [0.08131169999999965, 0.00037539999999980367]
def hasExoriCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori'])


# TODO: improve performance
# PERF: [0.08513510000000002, 0.00037559999999992044]
def hasExoriGranCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori gran'])


# TODO: improve performance
# PERF: [0.08332179999999978, 0.000373600000000085]
def hasExoriMasCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori mas'])


# TODO: improve performance
# TODO: add unit tests
# PERF: [0.08801449999999988, 0.000378400000000223]
def hasExuraGranIcoCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura gran'])


# TODO: improve performance
# PERF: [0.08647640000000001,  0.0003741999999999912]
def hasExoriMinCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori min'])


# TODO: improve performance
# PERF: [0.08596130000000013, 0.00038250000000017437]
def hasHealingCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['healing'])


# TODO: improve performance
# PERF: [0.08592040000000001, 0.0003776000000002]
def hasSupportCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['support'])


# TODO: improve performance
# TODO: add unit tests
# PERF: [0.08165200000000006, 0.0003780999999998258]
def hasUturaCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura'])


# TODO: improve performance
# TODO: add unit tests
# PERF: [0.0844541999999997, 0.0003747000000000611]
def hasUturaGranCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura gran'])


# PERF: [0.03996639999999996, 4.199999999787707e-06]
def slotIsEquipped(screenshot: GrayImage, slot: int) -> Union[bool, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    x0 = leftSideArrowsPos[0] + leftSideArrowsPos[2] + \
        (slot * 2) + ((slot - 1) * 34)
    slotImage = screenshot[leftSideArrowsPos[1]                           :leftSideArrowsPos[1] + 34, x0:x0 + 34]
    return slotImage[0, 0] == 41


# PERF: [0.04092479999999998, 4.300000000068138e-06]
def slotIsAvailable(screenshot: GrayImage, slot: int) -> Union[bool, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    x0 = leftSideArrowsPos[0] + leftSideArrowsPos[2] + \
        (slot * 2) + ((slot - 1) * 34)
    slotImage = screenshot[leftSideArrowsPos[1]                           :leftSideArrowsPos[1] + 34, x0:x0 + 34]
    return not (slotImage[1, 2] == 54 and slotImage[1, 4] == 54 and slotImage[1, 6] == 54 and slotImage[1, 8] == 54 and slotImage[1, 10] == 54)
