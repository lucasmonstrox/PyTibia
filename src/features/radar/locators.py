from src.features.radar import config
from src.utils.core import cacheObjectPos, locate


@cacheObjectPos
def getRadarToolsPos(screenshot):
    return locate(screenshot, config.images['tools'])
