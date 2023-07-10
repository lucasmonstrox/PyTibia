from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate
from .config import images


# PERF: [0.05150189999999988, 2.000000000279556e-06]
@cacheObjectPosition
def getBattleListIconPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['icons']['battleList'])


# PERF: [0.05364349999999973, 1.8999999991109462e-06]
@cacheObjectPosition
def getContainerBottomBarPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['containers']['bottomBar'])
