from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPos, locate
from .config import container


# PERF: [0.05364349999999973, 1.8999999991109462e-06]
@cacheObjectPos
def getContainerBottomBarPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, container['images']['bottomBar'])


# PERF: [0.05150189999999988, 2.000000000279556e-06]
@cacheObjectPos
def getContainerTopBarPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, container['images']['topBar'])
