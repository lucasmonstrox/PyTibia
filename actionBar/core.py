import easyocr
import numpy as np
import pathlib
from PIL import Image
from actionBar.locators import getSlot1Pos, getSlot2Pos, getSlot3Pos, getSlot4Pos, getSlot5Pos, getSlot6Pos, getSlot7Pos, getSlot8Pos, getSlot9Pos
from actionBar import extractors
from utils.core import locate
from utils.image import loadFromRGBToGray


reader = easyocr.Reader(['en'])
currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
attackCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/attack.png')
exoriCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/exori.png')
exoriGranCooldownImg = loadFromRGBToGray(
    f'{imagesPath}/cooldowns/exoriGran.png')
exoriMasCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/exoriMas.png')
hasteCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/haste.png')
supportCooldownImg = loadFromRGBToGray(f'{imagesPath}/cooldowns/support.png')


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
    basewidth = 24 * 5
    digits = np.where(digits <= 100, 0, digits)
    img = Image.fromarray(digits)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize))
    img = np.array(img)
    res2 = reader.readtext(img, detail=0)
    res2 = int(res2[0])
    return res2


def hasCooldownByImg(screenshot, cooldownImg):
    listOfCooldownsImg = extractors.getCooldownsImg(screenshot)
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