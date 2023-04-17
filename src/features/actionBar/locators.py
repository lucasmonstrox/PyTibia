from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPos, locate
from .config import images


# PERF: [0.062264100000000155, 2.8000000007466497e-06]
@cacheObjectPos
def getLeftArrowsPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['arrows']['left'])


# PERF: [0.05522599999999933, 1.8999999991109462e-06]
@cacheObjectPos
def getRightArrowsPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['arrows']['right'])
