from time import sleep
from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate, getScreenshot
from src.utils.image import crop
from src.utils.keyboard import hotkey, press, write
from src.utils.mouse import leftClick, moveTo
from .config import images, npcTradeBarImage, npcTradeOkImage


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getTradeTopPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, npcTradeBarImage)


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getTradeBottomPos(screenshot: GrayImage) -> Union[BBox, None]:
    tradeTopPos = getTradeTopPosition(screenshot)
    if tradeTopPos is None:
        return None
    (x, y, _, _) = tradeTopPos
    croppedImage = crop(
        screenshot, x, y, 174, len(screenshot) - y)
    (_, botY, _, _) = locate(croppedImage, npcTradeOkImage)
    return x, y + botY + 26, 174, 2


# TODO: add unit tests
# TODO: add perf
def findItem(screenshot: GrayImage, itemName: str):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick((bx + 160, by - 75))
    sleep(0.2)
    leftClick((bx + 16, by - 75))
    sleep(0.2)
    write(itemName)
    sleep(2)
    screenshotAfterFind = getScreenshot()
    itemImg = images[itemName]
    itemPos = locate(screenshotAfterFind, itemImg)
    # TODO: improve it, click should be done in a handle coordinate inside the box
    x = itemPos[0] + 10
    y = itemPos[1] + 10
    leftClick((x, y))


# TODO: add unit tests
# TODO: add perf
def setAmount(screenshot: GrayImage, amount: int):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick((bx + 115, by - 42))
    sleep(0.2)
    hotkey('ctrl', 'a')
    sleep(0.2)
    press('backspace')
    write(str(amount))


# TODO: add unit tests
# TODO: add perf
def confirmBuyItem(screenshot: GrayImage):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick((bx + 150, by - 18))


# TODO: add unit tests
# TODO: add perf
def clearSearchBox(screenshot: GrayImage):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    x = bx + 115 + 45
    y = by - 42 - 35
    moveTo((x, y))
    leftClick((x, y))
    moveTo((x, y + 20))


# TODO: add unit tests
# TODO: add perf
def buyItem(screenshot: GrayImage, itemName: str, itemQuantity: int):
    findItem(screenshot, itemName)
    sleep(1)
    setAmount(screenshot, itemQuantity)
    sleep(1)
    confirmBuyItem(screenshot)
    sleep(1)
    clearSearchBox(screenshot)
    sleep(1)
