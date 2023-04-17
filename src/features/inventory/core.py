import pathlib
import pyautogui
import time
from src.utils.core import getScreenshot, locate, randomCoord
from src.utils.image import crop, load, loadAsGrey, loadFromRGBToGray
from src.utils.mouse import mouseDrag, rightClick


currentPath = pathlib.Path(__file__).parent.resolve()

backpacksImages = {
    'beach backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/beachBackpack.png'),
    'brocade backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/brocadeBackpack.png'),
    'fur backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/furBackpack.png'),
}

backpacksBarsImages = {
    'beach backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/beachBackpackBar.png'),
    'brocade backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/brocadeBackpackBar.png'),
    'fur backpack': loadFromRGBToGray(f'{currentPath}/images/backpacks/furBackpackBar.png'),
}

backpackBarImg = loadAsGrey(
    f'{currentPath}/images/backpackBar.png')
jewelledBackpackBarImg = loadAsGrey(
    f'{currentPath}/images/jewelledBackpackBar.png')
blueBackpackBarImg = loadAsGrey(
    f'{currentPath}/images/blueBackpackBar.png')
orangeBackpackBarImg = loadAsGrey(
    f'{currentPath}/images/orangeBackpackBar.png')
backpackBottomImg = loadAsGrey(
    f'{currentPath}/images/backpackBottom.png')
mainBackpackImg = loadAsGrey(
    f'{currentPath}/images/mainBackpack.png')
lockerBarImg = loadAsGrey(f'{currentPath}/images/lockerBar.png')
depotBarImg = loadAsGrey(f'{currentPath}/images/depotBar.png')
depotImage = loadAsGrey(f'{currentPath}/images/depot.png')
emptySlotImage = loadAsGrey(f'{currentPath}/images/emptySlot.png')
stashImage = loadFromRGBToGray(f'{currentPath}/images/stash.png')
depotChest1Image = loadAsGrey(f'{currentPath}/images/items/depot-chest-1.png')
depotChest2Image = loadAsGrey(f'{currentPath}/images/items/depot-chest-2.png')
depotChest3Image = loadAsGrey(f'{currentPath}/images/items/depot-chest-3.png')
depotChest4Image = loadAsGrey(f'{currentPath}/images/items/depot-chest-4.png')

jewelledBpItems = [
    'great-health-potion',
    'great-mana-potion',
    'great-spirit-potion',
    'health-potion',
    'mana-potion',
    'strong-health-potion',
    'strong-mana-potion',
    'ultimate-health-potion',
    'ultimate-mana-potion',
    'ultimate-spirit-potion'
]

itemsImgs = [
    ('great-health-potion',
     load(f'{currentPath}/images/items/great-health-potion.png')),
    ('great-mana-potion',
     load(f'{currentPath}/images/items/great-mana-potion.png')),
    ('great-spirit-potion',
     load(f'{currentPath}/images/items/great-spirit-potion.png')),
    ('health-potion',
     load(f'{currentPath}/images/items/health-potion.png')),
    ('mana-potion',
     load(f'{currentPath}/images/items/mana-potion.png')),
    ('strong-health-potion',
     load(f'{currentPath}/images/items/strong-health-potion.png')),
    ('strong-mana-potion',
     load(f'{currentPath}/images/items/strong-mana-potion.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-1.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-2.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-3.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-4.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-5.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-6.png')),
    ('ultimate-health-potion',
     load(f'{currentPath}/images/items/ultimate-health-potion-7.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-1.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-2.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-3.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-4.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-5.png')),
    ('ultimate-mana-potion',
     load(f'{currentPath}/images/items/ultimate-mana-potion-6.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-1.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-2.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-3.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-4.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-5.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-6.png')),
    ('ultimate-spirit-potion',
     load(f'{currentPath}/images/items/ultimate-spirit-potion-7.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-1.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-2.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-3.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-4.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-5.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-6.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-7.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-8.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-9.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-10.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-11.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-12.png')),
    ('supreme-health-potion',
     load(f'{currentPath}/images/items/supreme-health-potion-13.png')),
    ('brown-backpack',
     load(f'{currentPath}/images/items/brown-backpack.png')),
    ('blue-backpack',
     load(f'{currentPath}/images/items/blue-backpack.png')),
    ('orange-backpack',
     load(f'{currentPath}/images/items/orange-backpack.png')),
    ('jewelled-backpack',
     load(f'{currentPath}/images/items/jewelled-backpack.png')),
    ('shopping-bag',
     load(f'{currentPath}/images/items/shopping-bag.png')),
    ('depot-chest-1',
     load(f'{currentPath}/images/items/depot-chest-1.png')),
    ('depot-chest-2',
     load(f'{currentPath}/images/items/depot-chest-2.png')),
    ('depot-chest-3',
     load(f'{currentPath}/images/items/depot-chest-3.png')),
    ('depot-chest-4',
     load(f'{currentPath}/images/items/depot-chest-4.png')),
    ('depot-chest-5',
     load(f'{currentPath}/images/items/depot-chest-5.png')),
    ('depot-chest-6',
     load(f'{currentPath}/images/items/depot-chest-6.png')),
    ('depot-chest-7',
     load(f'{currentPath}/images/items/depot-chest-7.png')),
    ('depot-chest-8',
     load(f'{currentPath}/images/items/depot-chest-8.png')),
    ('depot-chest-9',
     load(f'{currentPath}/images/items/depot-chest-9.png')),
    ('depot-chest-10',
     load(f'{currentPath}/images/items/depot-chest-10.png')),
    ('depot-chest-11',
     load(f'{currentPath}/images/items/depot-chest-11.png')),
    ('depot-chest-12',
     load(f'{currentPath}/images/items/depot-chest-12.png')),
    ('depot-chest-13',
     load(f'{currentPath}/images/items/depot-chest-13.png')),
    ('depot-chest-14',
     load(f'{currentPath}/images/items/depot-chest-14.png')),
    ('depot-chest-15',
     load(f'{currentPath}/images/items/depot-chest-15.png')),
    ('depot-chest-16',
     load(f'{currentPath}/images/items/depot-chest-16.png')),
    ('depot-chest-17',
     load(f'{currentPath}/images/items/depot-chest-17.png')),
    ('depot-chest-18',
     load(f'{currentPath}/images/items/depot-chest-18.png')),
    ('empty', load(f'{currentPath}/images/items/empty.png')),
]


def isBackpackOpen(screenshot, name):
    backpackBarImg = backpacksBarsImages[name]
    backpackBarPos = locate(screenshot, backpackBarImg)
    isOpen = backpackBarPos is not None
    return isOpen


def isLockerOpen(screenshot):
    lockerPosition = locate(screenshot, lockerBarImg)
    return lockerPosition is not None


def openBackpack(screenshot, name):
    backpackImg = backpacksImages[name]
    backpackPos = locate(screenshot, backpackImg, confidence=0.8)
    if backpackPos is None:
        return
    (x, y, _, __) = backpackPos
    backpackX = x + 5
    backpackY = y + 5
    pyautogui.rightClick(backpackX, backpackY)


def getWindowTopPos(screenshot, img):
    return locate(screenshot, img)


def getWindowBottomPos(screenshot, topPos):
    (x, y, w, h) = topPos
    (botX, botY, width, height) = locate(
        crop(screenshot, x, y, 160, 250), backpackBottomImg)
    return x, y + botY, 172, 1


def adjustAndGetWindowPos(window, img, squares):
    screenshot = getScreenshot()
    (x0, y0, w0, h0) = getWindowTopPos(screenshot, img)
    (x1, y1, w1, h1) = getWindowBottomPos(screenshot, (x0, y0, w0, h0))

    incompleteLine = 0
    if (squares % 4) != 0:
        incompleteLine = 1
    maxWindowSize = 14 + (36 * ((squares // 4) + incompleteLine)) + 12
    if (y1 - y0) < maxWindowSize:
        mouseDrag(x0 + 70, y1, x0 + 70, y1 +
                              (maxWindowSize - (y1 - y0)))
        screenshot = getScreenshot()
        (x1, y1, w1, h1) = getWindowBottomPos(screenshot, (x0, y0, w0, h0))
        return x0, y0, w0, y1 - y0
    return x0, y0, w0, y1 - y0


def isWindowOpen(screenshot, windowBar):
    backpackPos = locate(screenshot, windowBar)
    if backpackPos is None:
        return False
    return True


def openMainBackpack(window, squares):
    screenshot = getScreenshot()
    (x, y, w, h) = locate(screenshot, mainBackpackImg)
    if isWindowOpen(screenshot, backpackBarImg) is False:
        (xBp, yBp) = randomCoord(x + 3, y + 18, w - 3, h - 25)
        rightClick(xBp, yBp)
        time.sleep(1)
    backpackPos = adjustAndGetWindowPos(window, backpackBarImg, squares)
    backpackMap = mapWindowSquares(window, backpackPos, squares)
    return backpackPos, backpackMap


def mapWindowSquares(window, windowPos, squares):
    screenshot = getScreenshot(window)
    (x, y, w, h) = windowPos
    containerMap = []
    (borX, borY) = (11, 20)
    incompleteLine = 0
    if (squares % 4) != 0:
        incompleteLine = 1
    for i in range((squares // 4) + incompleteLine):
        for j in range(4):
            squarePos = (x + borX + 32 * j + 5 * j, y + borY + 32 * i + 5 * i)
            itemName = 'unknown'
            for k in range(len(itemsImgs)):
                (listH, listW, listC) = itemsImgs[k][1].shape
                itemFound = locate(
                    crop(
                        screenshot, squarePos[0] + 2, squarePos[1] + 1, 32 - 4, listH - 1), itemsImgs[k][1],
                    0.95)
                if itemFound is not None:
                    itemName = itemsImgs[k][0]
                    break
            if len(containerMap) < squares:
                containerMap.append((itemName, squarePos[0], squarePos[1]))

    return containerMap


def openDepot(window):
    screenshot = getScreenshot()
    (x, y, w, h) = locate(screenshot, lockerBarImg)
    (xLck, yLck) = randomCoord(x + 11, y + 20, 28, 28)
    rightClick(xLck, yLck)
    time.sleep(1)
    DepotPos = adjustAndGetWindowPos(window, depotBarImg, 18)
    DepotMap = mapWindowSquares(window, DepotPos, 18)
    return DepotPos, DepotMap


def closeWindow(windowPos):
    (x, y, w, h) = windowPos
    clickCoord = randomCoord(x + 162, y + 4, 10, 10)
    pyautogui.click(clickCoord[0], clickCoord[1])


def moveItem(fromContainerMap, toContainerMap, slotIndex):
    if toContainerMap[len(toContainerMap)-1][0] != 'empty':
        return None

    fromPos = randomCoord(
        fromContainerMap[slotIndex][1], fromContainerMap[slotIndex][2], 28, 28)
    toPos = randomCoord(
        toContainerMap[0][1], toContainerMap[0][2], 28, 28)
    mouseDrag(fromPos[0], fromPos[1], toPos[0], toPos[1])

    for i in reversed(range(1, len(toContainerMap))):
        toContainerMap[i] = (toContainerMap[i - 1][0],
                             toContainerMap[i][1], toContainerMap[i][2])
    toContainerMap[0] = (fromContainerMap[slotIndex][0],
                         toContainerMap[0][1], toContainerMap[0][2])

    for i in range(slotIndex, len(fromContainerMap) - 1):
        fromContainerMap[i] = (fromContainerMap[i + 1][0],
                               fromContainerMap[i][1], fromContainerMap[i][2])
    fromContainerMap[len(fromContainerMap)-1] = ('empty', fromContainerMap[len(
        fromContainerMap)-1][1], fromContainerMap[len(fromContainerMap)-1][2])

    return fromContainerMap, toContainerMap
