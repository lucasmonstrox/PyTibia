import utils.core
import utils.image
from . import config


@utils.core.cacheObjectPos
def getContainerBottomBarPos(screenshot):
    return utils.core.locate(screenshot, config.container['images']['bottomBar'])


@utils.core.cacheObjectPos
def getContainerTopBarPos(screenshot):
    return utils.core.locate(screenshot, config.container['images']['topBar'])
