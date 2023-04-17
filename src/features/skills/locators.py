import pathlib
from src.utils.core import cacheObjectPos, locate
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
xpBoostImage = loadFromRGBToGray(f'{currentPath}/images/xpBoostButton.png')


@cacheObjectPos
def getXpBoostPosition(screenshot):
    return locate(screenshot, xpBoostImage)
