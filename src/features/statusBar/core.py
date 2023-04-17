import numpy as np
import pathlib
from src.utils.core import cacheObjectPos, locate
from src.utils.image import loadAsGrey


currentPath = pathlib.Path(__file__).parent.resolve()
hpIconImage = loadAsGrey(f'{currentPath}/images/heartIcon.png')
manaIconImage = loadAsGrey(f'{currentPath}/images/manaIcon.png')
hpBarAllowedPixelsColors = np.array([79, 118, 121, 110, 62])
hpBarSize = 94

manaBarAllowedPixelsColors = np.array([68, 95, 97, 89, 52])
manaBarSize = 94


def getFilledBarPercentage(bar, size=100, allowedPixelsColors=[]):
    bar = np.where(np.isin(bar, allowedPixelsColors), 0, bar)
    barPercent = np.count_nonzero(bar == 0)
    percent = (barPercent * 100 // size)
    return percent


@cacheObjectPos
def getHeartPos(screenshot):
    return locate(screenshot, hpIconImage)


def getHpPercentage(screenshot):
    heartPos = getHeartPos(screenshot)
    didntGetHpPos = heartPos == None
    if didntGetHpPos:
        return None
    bar = getHealthBar(screenshot, heartPos)
    percent = getFilledBarPercentage(bar, size=hpBarSize,
                                     allowedPixelsColors=hpBarAllowedPixelsColors)
    return percent


def getHealthBar(screenshot, heartPos):
    (left, top, _, _) = heartPos
    y0 = top + 5
    y1 = y0 + 1
    x0 = left + 13
    x1 = x0 + hpBarSize
    bar = screenshot[y0:y1, x0:x1][0]
    return bar


@cacheObjectPos
def getManaPos(screenshot):
    return locate(screenshot, manaIconImage)


def getManaPercentage(screenshot):
    manaPos = getManaPos(screenshot)
    didntGetHpPos = manaPos == None
    if didntGetHpPos:
        return None
    bar = getManaBar(screenshot, manaPos)
    percent = getFilledBarPercentage(bar, size=manaBarSize,
                                     allowedPixelsColors=manaBarAllowedPixelsColors)
    return percent


def getManaBar(screenshot, heartPos):
    (left, top, _, _) = heartPos
    y0 = top + 5
    y1 = y0 + 1
    x0 = left + 14
    x1 = x0 + manaBarSize
    bar = screenshot[y0:y1, x0:x1][0]
    return bar
