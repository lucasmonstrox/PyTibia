from radar import config
import utils.core


@utils.core.cacheObjectPos
def getRadarToolsPos(screenshot):
    return utils.core.locate(screenshot, config.images['tools'])
