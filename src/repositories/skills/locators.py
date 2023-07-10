from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate
from .config import images


# TODO: add unit tests
# PERF: [0.05445730000000015, 1.9100000000271677e-05]
@cacheObjectPosition
def getSkillsIconPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['icons']['skills'])
