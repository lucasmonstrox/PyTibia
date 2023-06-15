from numba import njit
from typing import Union
from src.shared.typings import GrayImage
from .config import hpBarAllowedPixelsColors, manaBarAllowedPixelsColors
from .extractors import getHpBar, getManaBar
from .locators import getHpIconPosition, getManaIconPosition


# TODO: add parameters types
# TODO: add unit tests
# TODO: add perf
# TODO: change to numba to increase performance
@njit(cache=True, fastmath=True)
def getFilledBarPercentage(bar, allowedPixelsColors=[]) -> int:
    barPercent = len(bar)
    for i in range(len(bar)):
        if bar[i] not in allowedPixelsColors:
            barPercent -= 1
    return (barPercent * 100 // 94)


# TODO: add unit tests
# PERF: [0.052583100000000105, 2.1600000000177033e-05]
def getHpPercentage(screenshot: GrayImage) -> Union[int, None]:
    hpIconPosition = getHpIconPosition(screenshot)
    if hpIconPosition == None:
        return None
    bar = getHpBar(screenshot, hpIconPosition)
    return getFilledBarPercentage(bar, allowedPixelsColors=hpBarAllowedPixelsColors)


# TODO: add unit tests
# PERF: [0.04806750000000015, 2.3399999999895726e-05]
def getManaPercentage(screenshot: GrayImage) -> Union[int, None]:
    manaIconPosition = getManaIconPosition(screenshot)
    if manaIconPosition == None:
        return None
    bar = getManaBar(screenshot, manaIconPosition)
    return getFilledBarPercentage(bar, allowedPixelsColors=manaBarAllowedPixelsColors)
