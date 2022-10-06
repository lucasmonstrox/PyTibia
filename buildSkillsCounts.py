import numpy as np
import utils.core
import utils.image


numbersHashes = {}

for number in range(1000):
    numberAsString = "{:03d}".format(number)
    digit = numberAsString[2]
    digitAsImg = utils.image.loadFromRGBToGray(f'skills/images/{digit}.png')
    numberAsImg = np.zeros((8, 22), dtype=np.uint8)
    numberAsImg[:, 22-6:22] = digitAsImg
    hasDecimalDigit = number >= 10
    if hasDecimalDigit:
        decimalDigit = numberAsString[1]
        decimalDigitAsImg = utils.image.loadFromRGBToGray(
            f'skills/images/{decimalDigit}.png')
        numberAsImg[:, 22-14:22-14+6] = decimalDigitAsImg
    hasHundredDigit = number >= 100
    if hasHundredDigit:
        hundredDigit = numberAsString[0]
        hundredDigitAsImg = utils.image.loadFromRGBToGray(
            f'skills/images/{hundredDigit}.png')
        numberAsImg[:, 0:6] = hundredDigitAsImg
    numberAsImg = np.array(numberAsImg, dtype=np.uint8)
    hashKey = utils.core.hashit(numberAsImg)
    numbersHashes[hashKey] = number
