import numpy as np
import pathlib
from actionBar.locators import getSlot1Pos, getSlot2Pos, getSlot3Pos, getSlot4Pos, getSlot5Pos, getSlot6Pos, getSlot7Pos, getSlot8Pos, getSlot9Pos
from actionBar.extractors import getCooldownsImg
from utils.core import locate
from utils.image import loadAsGrey, loadFromRGBToGray
from utils.matrix import hasMatrixInsideOther

currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
attackCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/attack.png')
exoriCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/exori.png')
exoriGranCooldownImg = loadFromRGBToGray(
    f'{imagesPath}/cooldowns/exoriGran.png')
exoriMasCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/exoriMas.png')
hasteCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/haste.png')
supportCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/support.png')
numbersAsArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbersAsImg = [
    loadAsGrey(f'{imagesPath}/slotDigits/0.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/1.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/2.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/3.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/4.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/5.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/6.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/7.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/8.png'),
    loadAsGrey(f'{imagesPath}/slotDigits/9.png'),
]


# TODO: add unit tests
def getNumberFromDigitSlot(digitIndex, digits):
    digitWidth = 6
    x0 = digitIndex * digitWidth
    x1 = x0 + digitWidth
    digitImg = digits[:, x0:x1]
    result = np.array([hasMatrixInsideOther(digitImg, numberAsImg)
                      for numberAsImg in numbersAsImg])
    digit = np.nonzero(result == True)
    cannotGetNumber = len(digit[0]) == 0
    if cannotGetNumber:
        return None
    number = digit[0][0]
    return number


# TODO: add unit tests
def getSlotCount(screenshot, key):
    slotPosFunc = {
        '1': getSlot1Pos,
        '2': getSlot2Pos,
        '3': getSlot3Pos,
        '4': getSlot4Pos,
        '5': getSlot5Pos,
        '6': getSlot6Pos,
        '7': getSlot7Pos,
        '8': getSlot8Pos,
        '9': getSlot9Pos,
    }
    (x, y, w, _) = slotPosFunc[key](screenshot)
    x1 = x + w
    x0 = x1 - 30
    y0 = y + 22
    y1 = y0 + 8
    digits = screenshot[y0:y1, x0:x1]
    digits = digits[:, 6:30]
    digits = np.where(digits <= 30, 0, digits)
    digits = np.where(digits != 0, 255, digits)
    numberOfDigits = 4
    digits = np.array([getNumberFromDigitSlot(digitIndex, digits)
                      for digitIndex in np.arange(numberOfDigits)])
    digits = digits[digits != None]
    hasNoCount = len(digits) == 0
    if hasNoCount:
        return 0
    digits = digits[::-1]
    numberOfDigits = len(digits)
    sequentialVector = np.arange(numberOfDigits)
    vectorOf10 = np.full(numberOfDigits, 10)
    result = np.power(vectorOf10, sequentialVector)
    number = np.sum(digits * result)
    return number


def hasCooldownByImg(screenshot, cooldownImg):
    listOfCooldownsImg = getCooldownsImg(screenshot)
    cannotGetListOfCooldownsImg = listOfCooldownsImg is None
    if cannotGetListOfCooldownsImg:
        return None
    cooldownImgPos = locate(listOfCooldownsImg, cooldownImg)
    cannotGetCooldownImgPos = cooldownImgPos is None
    if cannotGetCooldownImgPos:
        return False
    (x, _, width, _) = cooldownImgPos
    percentBar = listOfCooldownsImg[20:21, x:x + width]
    firstPixel = percentBar[0][0]
    whitePixelColor = 255
    hasCooldown = firstPixel == whitePixelColor
    return hasCooldown


def hasAttackCooldown(screenshot):
    return hasCooldownByImg(screenshot, attackCooldownImg)


def hasExoriCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriCooldownImg)


def hasExoriGranCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriGranCooldownImg)


def hasExoriMasCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriMasCooldownImg)


def hasHasteCooldown(screenshot):
    return hasCooldownByImg(screenshot, hasteCooldownImg)


def hasSupportCooldown(screenshot):
    return hasCooldownByImg(screenshot, supportCooldownImg)
