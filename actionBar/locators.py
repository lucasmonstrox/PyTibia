import utils.core
import utils.image


leftSideArrowsImg = utils.image.loadFromRGBToGray(
    'actionBar/images/leftSideArrows.png')
rightSideArrowsImg = utils.image.loadFromRGBToGray(
    'actionBar/images/rightSideArrowsImg.png')


@utils.core.cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, leftSideArrowsImg)


@utils.core.cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, rightSideArrowsImg)
