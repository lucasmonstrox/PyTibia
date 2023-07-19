from time import time
import numpy as np
from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import hashit
from src.utils.image import convertGraysToBlack
from .config import minutesOrHoursHashes, numbersHashes
from .locators import getSkillsIconPosition


# TODO: add unit tests
# PERF: [0.04747469999999998, 2.9300000000009874e-05]
def getCapacity(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = skillsIconPosition[0] + 5, skillsIconPosition[1] + \
        131, skillsIconPosition[2], skillsIconPosition[3]
    return getValuesCount(screenshot, position)


# TODO: add unit tests
# TODO: add perf
def getFood(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = skillsIconPosition[0] + 5, skillsIconPosition[1] + \
        159, skillsIconPosition[2], skillsIconPosition[3]
    return getMinutesCount(screenshot, position)


# TODO: add unit tests
# PERF: [0.04967209999999955, 3.1599999999798456e-05]
def getHp(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = skillsIconPosition[0] + 5, skillsIconPosition[1] + \
        89, skillsIconPosition[2], skillsIconPosition[3]
    return getValuesCount(screenshot, position)


# TODO: add unit tests
# PERF: [0.05254219999999998, 2.970000000068751e-05]
def getMana(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = skillsIconPosition[0] + 5, skillsIconPosition[1] + \
        103, skillsIconPosition[2], skillsIconPosition[3]
    return getValuesCount(screenshot, position)


# TODO: add unit tests
# PERF: [0.04700700000000024, 3.0399999999985994e-05]
def getSpeed(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = skillsIconPosition[0] + 5, skillsIconPosition[1] + \
        145, skillsIconPosition[2], skillsIconPosition[3]
    return getValuesCount(screenshot, position)


# TODO: add unit tests
# PERF: [0.047493200000000346, 2.0000000000131024e-05]
def getStamina(screenshot: GrayImage) -> Union[int, None]:
    skillsIconPosition = getSkillsIconPosition(screenshot)
    if skillsIconPosition is None:
        return None
    position = (skillsIconPosition[0] + 5), (skillsIconPosition[1] +
                                             173), skillsIconPosition[2], skillsIconPosition[3]
    return getMinutesCount(screenshot, position)


# TODO: add unit tests
# TODO: add perf
def getMinutesCount(screenshot: GrayImage, position: BBox) -> int:
    minutesCountsImage = convertGraysToBlack(
        screenshot[position[1]:position[1] + 8, position[0] + 130:position[0] + 144])
    minutesCountsHashKey = hashit(minutesCountsImage)
    minutesCount = 0
    if minutesCountsHashKey in minutesOrHoursHashes:
        minutesCount = minutesOrHoursHashes[minutesCountsHashKey]
    hoursCountsImage = convertGraysToBlack(
        screenshot[position[1]:position[1] + 8, position[0] + 110:position[0] + 124])
    hoursCountsHashKey = hashit(hoursCountsImage)
    hoursCount = 0
    if hoursCountsHashKey in minutesOrHoursHashes:
        hoursCount = minutesOrHoursHashes[hoursCountsHashKey]
    return (hoursCount * 60) + minutesCount


# TODO: add unit tests
# TODO: add perf
def getValuesCount(screenshot: GrayImage, position: BBox) -> int:
    capacityHundredsCountsImage = convertGraysToBlack(
        screenshot[position[1]:position[1] + 8, position[0] + 144 - 22:position[0] + 144])
    capacityHundredsCountsImage = np.where(
        np.logical_or(capacityHundredsCountsImage == 126, capacityHundredsCountsImage == 192), 192, 0)
    capacityHundredsCountsImage = np.array(
        capacityHundredsCountsImage, dtype=np.uint8)
    capacityHundredsCountsHashKey = hashit(capacityHundredsCountsImage)
    capacityHundredsCount = 0
    if capacityHundredsCountsHashKey in numbersHashes:
        capacityHundredsCount = numbersHashes[capacityHundredsCountsHashKey]
    capacityThousandsCountsImage = convertGraysToBlack(
        screenshot[position[1]:position[1] + 8, position[0] + 116 - 22:position[0] + 116])
    capacityThousandsCountsImage = np.where(
        np.logical_or(capacityThousandsCountsImage == 126, capacityThousandsCountsImage == 192), 192, 0)
    capacityThousandsCountsImage = np.array(
        capacityThousandsCountsImage, dtype=np.uint8)
    capacityThousandsCountsHashKey = hashit(
        capacityThousandsCountsImage)
    capacityThousandsCount = 0
    if capacityThousandsCountsHashKey in numbersHashes:
        capacityThousandsCount = numbersHashes[capacityThousandsCountsHashKey] * 1000
    return capacityThousandsCount + capacityHundredsCount
