import pyautogui
import utils.image
import utils.core
import utils.mouse
from time import sleep
from . import config


@utils.core.cacheObjectPos
def getTradeTopPos(screenshot):
    return utils.core.locate(screenshot, config.npcTradeBarImage)


@utils.core.cacheObjectPos
def getTradeBottomPos(screenshot):
    (x, y, _, _) = getTradeTopPos(screenshot)
    croppedImage = utils.image.crop(
        screenshot, x, y, 174, len(screenshot) - y)
    (_, botY, _, _) = utils.core.locate(croppedImage, config.npcTradeOkImage)
    return x, y + botY + 26, 174, 2


def findItem(screenshot, itemName):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    utils.mouse.leftClick(bx + 160, by - 75)
    sleep(0.2)
    utils.mouse.leftClick(bx + 16, by - 75)
    sleep(0.2)
    pyautogui.typewrite(itemName)
    sleep(2)
    screenshotAfterFind = utils.image.RGBtoGray(utils.core.getScreenshot())
    itemImg = config.potionsImages[itemName]
    itemPos = utils.core.locate(screenshotAfterFind, itemImg)
    # TODO: improve it, click should be done in a handle coordinate inside the box
    x = itemPos[0] + 10
    y = itemPos[1] + 10
    utils.mouse.leftClick(x, y)


def setAmount(screenshot, amount):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    utils.mouse.leftClick(bx + 115, by - 42)
    sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(0.2)
    utils.core.press('backspace')
    pyautogui.typewrite(str(amount))


def confirmBuyItem(screenshot):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    utils.mouse.leftClick(bx + 150, by - 18)


def clearSearchBox(screenshot):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    x = bx + 115 + 45
    y = by - 42 - 35
    utils.mouse.mouseMove(x, y)
    utils.mouse.leftClick(x, y)
    utils.mouse.mouseMove(x, y + 20)


def buyItems(screenshot, itemsAndQuantities):
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    for itemAndQuantity in itemsAndQuantities:
        buyItem(screenshot, itemAndQuantity)


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
