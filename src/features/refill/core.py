import pyautogui
from time import sleep
from src.utils.core import cacheObjectPosition, locate, getScreenshot, press
from src.utils.image import crop
from src.utils.mouse import leftClick, mouseMove
from .config import images, npcTradeBarImage, npcTradeOkImage


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@cacheObjectPosition
def getTradeTopPos(screenshot):
    return locate(screenshot, npcTradeBarImage)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@cacheObjectPosition
def getTradeBottomPos(screenshot):
    (x, y, _, _) = getTradeTopPos(screenshot)
    croppedImage = crop(
        screenshot, x, y, 174, len(screenshot) - y)
    (_, botY, _, _) = locate(croppedImage, npcTradeOkImage)
    return x, y + botY + 26, 174, 2


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def findItem(screenshot, itemName):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx + 160, by - 75)
    sleep(0.2)
    leftClick(bx + 16, by - 75)
    sleep(0.2)
    pyautogui.typewrite(itemName)
    sleep(2)
    screenshotAfterFind = getScreenshot()
    itemImg = images[itemName]
    itemPos = locate(screenshotAfterFind, itemImg)
    # TODO: improve it, click should be done in a handle coordinate inside the box
    x = itemPos[0] + 10
    y = itemPos[1] + 10
    leftClick(x, y)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def setAmount(screenshot, amount):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx + 115, by - 42)
    sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(0.2)
    press('backspace')
    pyautogui.typewrite(str(amount))


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def confirmBuyItem(screenshot):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx + 150, by - 18)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def clearSearchBox(screenshot):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    x = bx + 115 + 45
    y = by - 42 - 35
    mouseMove(x, y)
    leftClick(x, y)
    mouseMove(x, y + 20)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def buyItems(screenshot, itemsAndQuantities):
    screenshot = getScreenshot()
    for itemAndQuantity in itemsAndQuantities:
        buyItem(screenshot, itemAndQuantity)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def buyItem(screenshot, itemAndQuantity):
    (itemName, quantity) = itemAndQuantity
    findItem(screenshot, itemName)
    sleep(1)
    setAmount(screenshot, quantity)
    sleep(1)
    confirmBuyItem(screenshot)
    sleep(1)
    clearSearchBox(screenshot)
    sleep(1)
