import utils.core, utils.image, utils.matrix
import numpy as np

f2SlotImg = utils.image.loadAsArray('hud/images/slots/f2.png')
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
def getSlotPos(screenshot):
    return utils.core.locate(screenshot, f2SlotImg)


def getSlotCount(screenshot):
    (x, y, w, _) = getSlotPos(screenshot)
    x1 = x + w
    x0 = x1 - 30
    y0 = y + 22
    y1 = y0 + 8
    digits = screenshot[y0:y1, x0:x1]
    digits = digits[:, 6:30]
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
