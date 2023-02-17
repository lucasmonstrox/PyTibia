from pathlib import Path
from utils.core import cacheObjectPos, locate
from utils.image import loadFromRGBToGray


currentPath = Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
leftSideArrowsImg = loadFromRGBToGray(f'{imagesPath}/leftSideArrows.png')
rightSideArrowsImg = loadFromRGBToGray(f'{imagesPath}/rightSideArrowsImg.png')


@cacheObjectPos
def getLeftArrowsPos(screenshot):
    return locate(screenshot, leftSideArrowsImg)


@cacheObjectPos
def getRightArrowsPos(screenshot):
    return locate(screenshot, rightSideArrowsImg)
