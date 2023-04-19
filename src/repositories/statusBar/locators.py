from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate
from .config import images


# TODO: add unit tests
# PERF: [0.053614899999999466, 1.699999999438262e-06]
@cacheObjectPosition
def getHpIconPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['icons']['hp'])


# TODO: add unit tests
# PERF: [0.05365620000000071, 1.7000000003264404e-06]
@cacheObjectPosition
def getManaIconPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['icons']['mana'])
