import utils.core, utils.image

leftSideArrowsImg = utils.image.loadAsArray('actionBar/images/leftSideArrows.png')
rightSideArrowsImg = utils.image.loadAsArray('actionBar/images/rightSideArrowsImg.png')


@utils.core.cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, leftSideArrowsImg)


@utils.core.cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, rightSideArrowsImg)
