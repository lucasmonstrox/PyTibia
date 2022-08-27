import utils.core
import utils.image


leftSideArrowsImg = utils.image.loadAsGrey(
    'actionBar/images/leftSideArrows.png')
rightSideArrowsImg = utils.image.loadAsGrey(
    'actionBar/images/rightSideArrowsImg.png')


@utils.core.cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, leftSideArrowsImg)


@utils.core.cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, rightSideArrowsImg)
