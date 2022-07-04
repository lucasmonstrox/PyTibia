from utils import utils

leftSideArrowsImg = utils.loadImgAsArray('actionBar/images/leftSideArrows.png')
utils.saveImg(leftSideArrowsImg, 'actionBar/images/leftSideArrows.png')
rightSideArrowsImg = utils.loadImgAsArray('actionBar/images/rightSideArrowsImg.png')
utils.saveImg(rightSideArrowsImg, 'actionBar/images/rightSideArrowsImg.png')


@utils.cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return utils.locate(screenshot, leftSideArrowsImg)


@utils.cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return utils.locate(screenshot, rightSideArrowsImg)


@utils.cacheObjectPos
def getActionBarImg(screenshot):
    leftSideArrowsPos = getLeftSideArrowsPos(screenshot)
    rightSideArrowsPos = getRightSideArrowsPos(screenshot)