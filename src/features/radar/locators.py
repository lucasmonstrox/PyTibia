from src.features.radar import config
from src.utils.core import cacheObjectPosition, locate


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@cacheObjectPosition
def getRadarToolsPos(screenshot):
    return locate(screenshot, config.images['tools'])
