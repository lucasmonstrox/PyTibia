from typing import Union
from src.repositories.radar.config import images
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getRadarToolsPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['tools'])
