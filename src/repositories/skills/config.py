import numpy as np
import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
iconsImagesPath = f'{imagesPath}/icons'
digitsImagesPath = f'{imagesPath}/digits'
images = {
    'digits': {
        0: loadFromRGBToGray(f'{digitsImagesPath}/0.png'),
        1: loadFromRGBToGray(f'{digitsImagesPath}/1.png'),
        2: loadFromRGBToGray(f'{digitsImagesPath}/2.png'),
        3: loadFromRGBToGray(f'{digitsImagesPath}/3.png'),
        4: loadFromRGBToGray(f'{digitsImagesPath}/4.png'),
        5: loadFromRGBToGray(f'{digitsImagesPath}/5.png'),
        6: loadFromRGBToGray(f'{digitsImagesPath}/6.png'),
        7: loadFromRGBToGray(f'{digitsImagesPath}/7.png'),
        8: loadFromRGBToGray(f'{digitsImagesPath}/8.png'),
        9: loadFromRGBToGray(f'{digitsImagesPath}/9.png'),
    },
    'icons': {
        'skills': loadFromRGBToGray(f'{iconsImagesPath}/skills.png')
    },
}
minutesOrHoursHashes = {}
numbersHashes = {}

# TODO: make loader function
for number in range(1000):
    numberAsString = "{:03d}".format(number)
    digit = int(numberAsString[2])
    digitImage = images['digits'][digit]
    numberAsImg = np.zeros((8, 22), dtype=np.uint8)
    numberAsImg[:, 22 - 6:22] = digitImage
    hasDecimalDigit = number >= 10
    if hasDecimalDigit:
        decimalDigit = int(numberAsString[1])
        decimalDigitImage = images['digits'][decimalDigit]
        numberAsImg[:, 22 - 14:22 - 14 + 6] = decimalDigitImage
    hasHundredDigit = number >= 100
    if hasHundredDigit:
        hundredDigit = int(numberAsString[0])
        hundredDigitAsImg = images['digits'][hundredDigit]
        numberAsImg[:, 0:6] = hundredDigitAsImg
    numberAsImg = np.array(numberAsImg, dtype=np.uint8)
    hashKey = hashit(numberAsImg)
    numbersHashes[hashKey] = number

# TODO: make loader function
for number in range(60):
    numberAsString = "{:02d}".format(number)
    firstDigit = int(numberAsString[1])
    secondDigit = int(numberAsString[0])
    firstDigitImage = images['digits'][firstDigit]
    secondDigitImage = images['digits'][secondDigit]
    dateAsImg = np.zeros((8, 14), dtype=np.uint8)
    dateAsImg[:, 14 - 6:14] = firstDigitImage
    dateAsImg[:, 0:6] = secondDigitImage
    dateAsImg = np.array(dateAsImg, dtype=np.uint8)
    hashKey = hashit(dateAsImg)
    minutesOrHoursHashes[hashKey] = number
