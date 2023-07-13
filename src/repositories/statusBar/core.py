from numba import njit
from typing import Union
from src.shared.typings import GrayImage
from .config import hpBarAllowedPixelsColors, manaBarAllowedPixelsColors
from .extractors import getHpBar, getManaBar
from .locators import getHpIconPosition, getManaIconPosition


# TODO: add parameters types
# TODO: add unit tests
# TODO: add perf
@njit(cache=True, fastmath=True)
def getFilledBarPercentage(bar, allowedPixelsColors=[]) -> int:
    barPercent = len(bar)
    for i in range(len(bar)):
        if bar[i] not in allowedPixelsColors:
            barPercent -= 1
    return (barPercent * 100 // 94)


# TODO: add unit tests
# PERF: [0.34756980000000004, 2.9999999999752447e-06]
def getHpPercentage(screenshot: GrayImage) -> Union[int, None]:
    hpIconPosition = getHpIconPosition(screenshot)
    if hpIconPosition is None:
        return None
    bar = getHpBar(screenshot, hpIconPosition)
    return getFilledBarPercentage(bar, allowedPixelsColors=hpBarAllowedPixelsColors)


# TODO: add unit tests
# PERF: [0.32003090000000034, 3.200000000092018e-06]
def getManaPercentage(screenshot: GrayImage) -> Union[int, None]:
    manaIconPosition = getManaIconPosition(screenshot)
    if manaIconPosition is None:
        return None
    bar = getManaBar(screenshot, manaIconPosition)
    return getFilledBarPercentage(bar, allowedPixelsColors=manaBarAllowedPixelsColors)
