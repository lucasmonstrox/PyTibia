import numpy as np
from typing import Union
from src.shared.typings import GrayImage
from .config import barSize, hpBarAllowedPixelsColors, manaBarAllowedPixelsColors
from .extractors import getHpBar, getManaBar
from .locators import getHpIconPosition, getManaIconPosition


# TODO: add unit tests
# TODO: add perf
def getFilledBarPercentage(bar, size: int=100, allowedPixelsColors=[]) -> int:
    bar = np.where(np.isin(bar, allowedPixelsColors), 0, bar)
    barPercent = np.count_nonzero(bar == 0)
    percent = (barPercent * 100 // size)
    return percent


# TODO: add unit tests
# PERF: [0.052583100000000105, 2.1600000000177033e-05]
def getHpPercentage(screenshot: GrayImage) -> Union[int, None]:
    hpIconPosition = getHpIconPosition(screenshot)
    if hpIconPosition == None:
        return None
    bar = getHpBar(screenshot, hpIconPosition)
    return getFilledBarPercentage(bar, size=barSize,
                                     allowedPixelsColors=hpBarAllowedPixelsColors)


# TODO: add unit tests
# PERF: [0.04806750000000015, 2.3399999999895726e-05]
def getManaPercentage(screenshot: GrayImage) -> Union[int, None]:
    manaIconPosition = getManaIconPosition(screenshot)
    if manaIconPosition == None:
        return None
    bar = getManaBar(screenshot, manaIconPosition)
    percent = getFilledBarPercentage(bar, size=barSize,
                                     allowedPixelsColors=manaBarAllowedPixelsColors)
    return percent
