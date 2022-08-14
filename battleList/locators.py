from typing import Union
from . import config
from core.typing import UINT8_NDARRAY
import utils.core
import utils.image


@utils.core.cacheObjectPos
def getContainerBottomBarPos(screenshot: UINT8_NDARRAY) -> Union[None, UINT8_NDARRAY]:
    return utils.core.locate(screenshot, config.container["images"]["bottomBar"])


@utils.core.cacheObjectPos
def getContainerTopBarPos(screenshot: UINT8_NDARRAY) -> Union[None, UINT8_NDARRAY]:
    return utils.core.locate(screenshot, config.container["images"]['topBar'])
