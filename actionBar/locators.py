import pathlib
from utils.core import cacheObjectPos, locate
from utils.image import loadAsGrey, loadFromRGBToGray

currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
leftSideArrowsImg = loadFromRGBToGray(f'{imagesPath}/leftSideArrows.png')
rightSideArrowsImg = loadFromRGBToGray(f'{imagesPath}/rightSideArrowsImg.png')
slotsImgs = {
    "1": loadFromRGBToGray(f'{imagesPath}/slots/1.png'),
    "2": loadFromRGBToGray(f'{imagesPath}/slots/2.png'),
    "3": loadFromRGBToGray(f'{imagesPath}/slots/3.png'),
    "4": loadFromRGBToGray(f'{imagesPath}/slots/4.png'),
    "5": loadFromRGBToGray(f'{imagesPath}/slots/5.png'),
    "6": loadFromRGBToGray(f'{imagesPath}/slots/6.png'),
    "7": loadFromRGBToGray(f'{imagesPath}/slots/7.png'),
    "8": loadFromRGBToGray(f'{imagesPath}/slots/8.png'),
    "9": loadFromRGBToGray(f'{imagesPath}/slots/9.png'),
}


@cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return locate(screenshot, leftSideArrowsImg)


@cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return locate(screenshot, rightSideArrowsImg)


@cacheObjectPos
def getSlot1Pos(screenshot):
    return locate(screenshot, slotsImgs['1'])


@cacheObjectPos
def getSlot2Pos(screenshot):
    return locate(screenshot, slotsImgs['2'])


@cacheObjectPos
def getSlot3Pos(screenshot):
    return locate(screenshot, slotsImgs['3'])


@cacheObjectPos
def getSlot4Pos(screenshot):
    return locate(screenshot, slotsImgs['4'])


@cacheObjectPos
def getSlot5Pos(screenshot):
    return locate(screenshot, slotsImgs['5'])


@cacheObjectPos
def getSlot6Pos(screenshot):
    return locate(screenshot, slotsImgs['6'])


@cacheObjectPos
def getSlot7Pos(screenshot):
    return locate(screenshot, slotsImgs['7'])


@cacheObjectPos
def getSlot8Pos(screenshot):
    return locate(screenshot, slotsImgs['8'])


@cacheObjectPos
def getSlot9Pos(screenshot):
    return locate(screenshot, slotsImgs['9'])
