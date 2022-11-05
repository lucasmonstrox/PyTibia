import numpy as np
import pathlib
import utils.core
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()
minutesOrHoursHashes = {}
numbersHashes = {}

for number in range(1000):
    numberAsString = "{:03d}".format(number)
    digit = numberAsString[2]
    digitAsImg = utils.image.loadFromRGBToGray(
        f'{currentPath}/images/{digit}.png')
    numberAsImg = np.zeros((8, 22), dtype=np.uint8)
    numberAsImg[:, 22-6:22] = digitAsImg
    hasDecimalDigit = number >= 10
    if hasDecimalDigit:
        decimalDigit = numberAsString[1]
        decimalDigitAsImg = utils.image.loadFromRGBToGray(
            f'{currentPath}/images/{decimalDigit}.png')
        numberAsImg[:, 22-14:22-14+6] = decimalDigitAsImg
    hasHundredDigit = number >= 100
    if hasHundredDigit:
        hundredDigit = numberAsString[0]
        hundredDigitAsImg = utils.image.loadFromRGBToGray(
            f'{currentPath}/images/{hundredDigit}.png')
        numberAsImg[:, 0:6] = hundredDigitAsImg
    numberAsImg = np.array(numberAsImg, dtype=np.uint8)
    hashKey = utils.core.hashit(numberAsImg)
    numbersHashes[hashKey] = number


for number in range(60):
    numberAsString = "{:02d}".format(number)
    firstDigit = numberAsString[1]
    secondDigit = numberAsString[0]
    firstDigitAsImg = utils.image.loadFromRGBToGray(
        f'{currentPath}/images/{firstDigit}.png')
    secondDigitAsImg = utils.image.loadFromRGBToGray(
        f'{currentPath}/images/{secondDigit}.png')
    dateAsImg = np.zeros((8, 14), dtype=np.uint8)
    dateAsImg[:, 14-6:14] = firstDigitAsImg
    dateAsImg[:, 0:6] = secondDigitAsImg
    dateAsImg = np.array(dateAsImg, dtype=np.uint8)
    hashKey = utils.core.hashit(dateAsImg)
    minutesOrHoursHashes[hashKey] = number
