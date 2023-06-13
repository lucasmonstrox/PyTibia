import math
from typing import Union
import src.repositories.actionBar.extractors as actionBarExtractors
import src.repositories.actionBar.locators as actionBarLocators
from src.shared.typings import GrayImage
import src.utils.core as coreUtils
from .config import images


# TODO: add unit tests
def getSlotCount(screenshot: GrayImage, slot: int) -> Union[int, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    (xOfLeftSideArrowsPos, yOfLeftSideArrowsPos, widthOfLeftSideArrowsPos, _) = leftSideArrowsPos
    x0 = xOfLeftSideArrowsPos + widthOfLeftSideArrowsPos + (slot * 2) + ((slot - 1) * 34)
    y0 = yOfLeftSideArrowsPos
    slotImage = screenshot[y0:y0 + 34, x0:x0 + 34]
    digits = slotImage[24:32, 3:33]
    count = 0
    for i in range(5):
        x = (6 * (5 - i) - 3)
        numberImage = digits[2:6, x:x + 1]
        numberHash = coreUtils.hashit(numberImage)
        number = images['digits'].get(numberHash, None)
        if number is None:
            break
        count += number * math.pow(10, i)
    return int(count)


def hasCooldownByImage(screenshot: GrayImage, cooldownImage: GrayImage) -> Union[bool, None]:
    listOfCooldownsImage = actionBarExtractors.getCooldownsImage(screenshot)
    if listOfCooldownsImage is None:
        return None
    cooldownImagePosition = coreUtils.locate(listOfCooldownsImage, cooldownImage)
    if cooldownImagePosition is None:
        return False
    percentBar = listOfCooldownsImage[20:21, cooldownImagePosition[0]:cooldownImagePosition[0] + cooldownImagePosition[2]]
    return percentBar[0][0] == 255


# TODO: add unit tests
def hasCooldownByName(screenshot: GrayImage, name: str) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns'][name])


def hasAttackCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['attack'])


def hasExoriCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori'])


def hasExoriGranCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori gran'])


def hasExoriMasCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori mas'])


# TODO: add unit tests
def hasExuraGranIcoCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura gran'])


def hasExoriMinCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['exori min'])


def hasHealingCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['healing'])


def hasSupportCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['support'])


# TODO: add unit tests
def hasUturaCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura'])


# TODO: add unit tests
def hasUturaGranCooldown(screenshot: GrayImage) -> Union[bool, None]:
    return hasCooldownByImage(screenshot, images['cooldowns']['utura gran'])


def slotIsEquipped(screenshot: GrayImage, slot: int) -> Union[bool, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    (xOfLeftSideArrowsPos, yOfLeftSideArrowsPos, widthOfLeftSideArrowsPos, _) = leftSideArrowsPos
    x0 = xOfLeftSideArrowsPos + widthOfLeftSideArrowsPos + (slot * 2) + ((slot - 1) * 34)
    y0 = yOfLeftSideArrowsPos
    slotImage = screenshot[y0:y0 + 34, x0:x0 + 34]
    return slotImage[0, 0] == 41


def slotIsAvailable(screenshot: GrayImage, slot: int) -> Union[bool, None]:
    leftSideArrowsPos = actionBarLocators.getLeftArrowsPosition(screenshot)
    if leftSideArrowsPos is None:
        return None
    x0 = leftSideArrowsPos[0] + leftSideArrowsPos[2] + (slot * 2) + ((slot - 1) * 34)
    slotImage = screenshot[leftSideArrowsPos[1]:leftSideArrowsPos[1] + 34, x0:x0 + 34]
    return not (slotImage[1, 2] == 54 and slotImage[1, 4] == 54 and slotImage[1, 6] == 54 and slotImage[1, 8] == 54 and slotImage[1, 10] == 54)
