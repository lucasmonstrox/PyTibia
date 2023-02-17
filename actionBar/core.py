from easyocr import Reader
import numpy as np
from PIL import Image
from .config import images
from .extractors import getCooldownsImage
from .locators import getLeftArrowsPos
from utils.core import locate


reader = Reader(['en'])


def getSlotCount(screenshot, slot):
    leftSideArrowsPos = getLeftArrowsPos(screenshot)
    cannotGetLeftSideArrowsPos = leftSideArrowsPos is None
    if cannotGetLeftSideArrowsPos:
        return None
    (xOfLeftSideArrowsPos, yOfLeftSideArrowsPos, widthOfLeftSideArrowsPos, _) = leftSideArrowsPos
    pageSlot = (slot - 1)
    slotSize = 34
    slotGap = 2
    x0 = xOfLeftSideArrowsPos + widthOfLeftSideArrowsPos + (slot * slotGap) + (pageSlot * slotSize)
    y0 = yOfLeftSideArrowsPos
    slotImg = screenshot[y0:y0 + 34, x0:x0 + 34]
    digits = slotImg[24:32, 3:33]
    basewidth = 24 * 5
    digits = np.where(digits <= 100, 0, digits)
    img = Image.fromarray(digits)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize))
    img = np.array(img)
    textAsArray = reader.readtext(img, detail=0)
    cannotGetCount = len(textAsArray) == 0
    if cannotGetCount:
        return None
    count = int(textAsArray[0])
    return count


def hasCooldownByImg(screenshot, cooldownImg):
    listOfCooldownsImg = getCooldownsImage(screenshot)
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
