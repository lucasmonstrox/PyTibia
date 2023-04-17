import pathlib
import pyautogui
from time import sleep
from src.features.chat.core import sendMessage
from src.utils.core import cacheObjectPos, getScreenshot, locate, press
from src.utils.image import crop, loadAsGrey
from src.utils.mouse import leftClick


currentPath = pathlib.Path(__file__).parent.resolve()
npcTradeBarImg = loadAsGrey(f'{currentPath}/images/npcTradeBar.png')
npcTradeOkImg = loadAsGrey(f'{currentPath}/images/npcTradeOk.png')


@cacheObjectPos
def getTradeTopPos(screenshot):
    return locate(screenshot, npcTradeBarImg)


@cacheObjectPos
def getTradeBottomPos(screenshot):
    (x, y, w, h) = getTradeTopPos(screenshot)
    (botX, botY, width, height) = locate(crop(
        screenshot, x, y, 174, len(screenshot) - y), npcTradeOkImg)
    return x, y + botY + 26, 174, 2


def findItem(screenshot, itemName):
    (tx, ty, _, _) = getTradeTopPos(screenshot)
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx+160, by-75)
    sleep(0.2)
    leftClick(bx + 16, by - 75)
    sleep(0.2)
    pyautogui.typewrite(itemName)
    sleep(0.2)
    leftClick(tx + 90, ty + 75)
    sleep(0.2)


def setAmount(screenshot, amount):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx + 115, by - 42)
    sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(0.2)
    press('backspace')
    pyautogui.typewrite(str(amount))


def buyItem(screenshot):
    (bx, by, _, _) = getTradeBottomPos(screenshot)
    leftClick(bx + 150, by - 18)


def startTrade(screenshot):
    sendMessage(screenshot, 'hi')
    sleep(0.2)
    sendMessage(screenshot, 'trade')
    sleep(0.2)


def buyItems(screenshot, itemAndQuantity):
    startTrade(screenshot)
    screenshot = getScreenshot()
    for item in itemAndQuantity:
        (itemName, amount) = item
        findItem(screenshot, itemName)
        sleep(0.2)
        setAmount(screenshot, amount)
        sleep(0.2)
        buyItem(screenshot)
        sleep(0.2)
