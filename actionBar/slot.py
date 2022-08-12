import utils.core, utils.image, utils.matrix
import numpy as np

slotImgs = {
    "f1": utils.image.loadAsArray('hud/images/slots/f1.png'),
    "f2": utils.image.loadAsArray('hud/images/slots/f2.png'),
    "f3": utils.image.loadAsArray('hud/images/slots/f3.png'),
    "f4": utils.image.loadAsArray('hud/images/slots/f4.png'),
    "f5": utils.image.loadAsArray('hud/images/slots/f5.png'),
    "f6": utils.image.loadAsArray('hud/images/slots/f6.png'),
    "f7": utils.image.loadAsArray('hud/images/slots/f7.png'),
    "f8": utils.image.loadAsArray('hud/images/slots/f8.png'),
    "f9": utils.image.loadAsArray('hud/images/slots/f9.png'),
    "f10": utils.image.loadAsArray('hud/images/slots/f10.png'),
    "f11": utils.image.loadAsArray('hud/images/slots/f11.png'),
    "f12": utils.image.loadAsArray('hud/images/slots/f12.png'),
}

numbersAsArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbersAsImg = [
    utils.image.loadAsArray('actionBar/images/slotDigits/0.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/1.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/2.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/3.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/4.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/5.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/6.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/7.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/8.png'),
    utils.image.loadAsArray('actionBar/images/slotDigits/9.png'),
]


def calculateDigit(digitTuple):
    (digitIndex, digit) = digitTuple
    return (10 ** digitIndex) * digit


def getNumberFromDigitSlot(digitIndex, digits):
    digitWidth = 6
    x0 = digitIndex * digitWidth
    x1 = x0 + digitWidth
    digitImg = digits[:, x0:x1]
    result = np.array([utils.matrix.hasMatrixInsideOther(digitImg, numberAsImg) for numberAsImg in numbersAsImg])
    digit = np.nonzero(result == True)
    cannotGetNumber = len(digit[0]) == 0
    if cannotGetNumber:
        return None
    number = digit[0][0]
    return number


@utils.core.cacheObjectPos
def getSlot1Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f1'])


@utils.core.cacheObjectPos
def getSlot2Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f2'])


@utils.core.cacheObjectPos
def getSlot3Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f3'])


@utils.core.cacheObjectPos
def getSlot4Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f4'])


@utils.core.cacheObjectPos
def getSlot5Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f5'])


@utils.core.cacheObjectPos
def getSlot6Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f6'])


@utils.core.cacheObjectPos
def getSlot7Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f7'])


@utils.core.cacheObjectPos
def getSlot8Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f8'])


@utils.core.cacheObjectPos
def getSlot9Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f9'])


@utils.core.cacheObjectPos
def getSlot10Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f10'])


@utils.core.cacheObjectPos
def getSlot11Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f11'])


@utils.core.cacheObjectPos
def getSlot12Pos(screenshot):
    return utils.core.locate(screenshot, slotImgs['f12'])


def getSlotCount(screenshot, key):

    if key == 'f1': (x, y, w, _) = getSlot1Pos(screenshot)
    if key == 'f2': (x, y, w, _) = getSlot2Pos(screenshot)
    if key == 'f3': (x, y, w, _) = getSlot3Pos(screenshot)
    if key == 'f4': (x, y, w, _) = getSlot4Pos(screenshot)
    if key == 'f5': (x, y, w, _) = getSlot5Pos(screenshot)
    if key == 'f6': (x, y, w, _) = getSlot6Pos(screenshot)
    if key == 'f7': (x, y, w, _) = getSlot7Pos(screenshot)
    if key == 'f8': (x, y, w, _) = getSlot8Pos(screenshot)
    if key == 'f9': (x, y, w, _) = getSlot9Pos(screenshot)
    if key == 'f10': (x, y, w, _) = getSlot10Pos(screenshot)
    if key == 'f11': (x, y, w, _) = getSlot11Pos(screenshot)
    if key == 'f12': (x, y, w, _) = getSlot12Pos(screenshot)

    x1 = x + w
    x0 = x1 - 30
    y0 = y + 22
    y1 = y0 + 8
    digits = screenshot[y0:y1, x0:x1]
    digits = digits[:, 6:30]
    digits = np.where(digits <= 30, 0, digits)
    digits = np.where(digits != 0, 255, digits)
    numberOfDigits = 4
    digits = np.array([getNumberFromDigitSlot(digitIndex, digits) for digitIndex in np.arange(numberOfDigits)])
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
