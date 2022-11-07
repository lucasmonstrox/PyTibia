from easyocr import Reader
import numpy as np
from PIL import Image
from .config import images
from .extractors import getCooldownsImg
from .locators import getSlot1Pos, getSlot2Pos, getSlot3Pos, getSlot4Pos, getSlot5Pos, getSlot6Pos, getSlot7Pos, getSlot8Pos, getSlot9Pos
from utils.core import locate


reader = Reader(['en'])


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
    return hasCooldownByImg(screenshot, images['attackCooldown'])


def hasExoriCooldown(screenshot):
    return hasCooldownByImg(screenshot, images['exoriCooldown'])


def hasExoriGranCooldown(screenshot):
    return hasCooldownByImg(screenshot, images['exoriGranCooldown'])


def hasExoriMasCooldown(screenshot):
    return hasCooldownByImg(screenshot, images['exoriMasCooldown'])


def hasHasteCooldown(screenshot):
    return hasCooldownByImg(screenshot, images['hasteCooldown'])


def hasSupportCooldown(screenshot):
    return hasCooldownByImg(screenshot, images['supportCooldown'])
