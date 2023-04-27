import pathlib
from typing import Tuple, Union
from src.shared.typings import BBox, GrayImage
from src.repositories.gameWindow.core import getLeftArrowPosition
from src.utils.core import cacheObjectPosition, hashit, locate, locateMultiple, press, typeKeyboard
from src.utils.image import cacheChain, convertGraysToBlack, loadFromRGBToGray, save
from .config import hashes, images


currentPath = pathlib.Path(__file__).parent.resolve()
chatMenuImg = loadFromRGBToGray(f'{currentPath}/images/chatMenu.png')
chatOnImg = loadFromRGBToGray(f'{currentPath}/images/chatOn.png')
chatOnImgTemp = loadFromRGBToGray(f'{currentPath}/images/chatOnTemp.png')
chatOffImg = loadFromRGBToGray(f'{currentPath}/images/chatOff.png')
chatOffImg = loadFromRGBToGray(f'{currentPath}/images/chatOff.png')
lootOfTextImg = loadFromRGBToGray(f'{currentPath}/images/lootOfText.png')
nothingTextImg = loadFromRGBToGray(f'{currentPath}/images/nothingText.png')
oldListOfLootCheck = []


# TODO: add unit tests
# TODO: add perf
# TODO: add tests
def getTabs(screenshot):
    shouldFindTabs = True
    tabIndex = 0
    tabs = {}
    leftSidebarArrowsPosition = getLeftArrowPosition(screenshot)
    chatMenuPosition = getChatMenuPosition(screenshot)
    x, y, width, height = leftSidebarArrowsPosition[0] + 18, chatMenuPosition[1], chatMenuPosition[0] - (leftSidebarArrowsPosition[0] + 18), 20
    chatsTabsContainerImage = screenshot[y:y + height, x:x + width]
    while shouldFindTabs:
        xOfTab = tabIndex * 96
        firstPixel = chatsTabsContainerImage[0, xOfTab]
        if firstPixel != 114 and firstPixel != 125:
            shouldFindTabs = False
            continue
        isTabSelected = firstPixel == 114
        tabImage = chatsTabsContainerImage[2:16, xOfTab + 2:xOfTab + 2 + 92]
        tabImageHash = hashit(tabImage)
        tabName = hashes['tabs'].get(tabImageHash, 'Unknown')
        if tabName != 'Unknown':
            tabs.setdefault(tabName, {'isSelected': isTabSelected, 'position': (x + xOfTab, y, 92, 14)})
        tabIndex += 1
    return tabs


# TODO: add unit tests
# TODO: add perf
def hasNewLoot(screenshot: GrayImage) -> bool:
    global oldListOfLootCheck
    lootLines = getLootLines(screenshot)
    if len(lootLines) == 0:
        return False
    listOfLootCheck = []
    start = 5
    if len(lootLines) - 5 <= 0:
        start = len(lootLines)
    for i in range(len(lootLines) - start, len(lootLines)):
        listOfLootCheck.append(hashit(
            convertGraysToBlack(lootLines[i][0])))
    if len(listOfLootCheck) != 0 and len(oldListOfLootCheck) == 0:
        oldListOfLootCheck = listOfLootCheck
        return True
    for newLootLine in listOfLootCheck:
        if newLootLine not in oldListOfLootCheck:
            oldListOfLootCheck = listOfLootCheck
            return True
    oldListOfLootCheck = listOfLootCheck
    return False


# TODO: add unit tests
# TODO: add perf
def getLootLines(screenshot: GrayImage) -> GrayImage:
    (x, y, w, h) = getChatMessagesContainerPosition(screenshot)
    messages = screenshot[y: y + h, x: x + w]
    lootLines = locateMultiple(lootOfTextImg, messages)
    linesWithLoot = []
    for line in lootLines:
        line = x, line[1] + y, w, line[3]
        lineImg = screenshot[line[1]:line[1] +
                             line[3], line[0]:line[0] + line[2]]
        nothingFound = locate(nothingTextImg, lineImg)
        if nothingFound is None:
            linesWithLoot.append((lineImg, line))
    return linesWithLoot


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getChatMenuPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, chatMenuImg)


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getChatOffPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, chatOffImg, confidence=0.985)


# TODO: add unit tests
# TODO: add perf
def getChatStatus(screenshot: GrayImage) -> Tuple[BBox, bool]:
    chatOffPos = getChatOffPosition(screenshot)
    if chatOffPos:
        return chatOffPos, False
    chatOnPos = locate(screenshot, chatOnImgTemp, confidence=0.9)
    return chatOnPos, True


# TODO: add unit tests
# TODO: add perf
def enableChatOn(screenshot: GrayImage):
    (_, chatIsOn) = getChatStatus(screenshot)
    chatIsNotOn = chatIsOn is False
    if chatIsNotOn:
        press('enter')


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getChatMessagesContainerPosition(screenshot: GrayImage) -> BBox:
    leftSidebarArrows = getLeftArrowPosition(screenshot)
    chatMenu = getChatMenuPosition(screenshot)
    chatStatus = getChatStatus(screenshot)
    return leftSidebarArrows[0] + 5, chatMenu[1] + 18, chatStatus[0][0] + 40, (chatStatus[0][1] - 6) - (chatMenu[1] + 13)


@cacheChain([
    images['tabs']['loot']['selectedLoot'],
    images['tabs']['loot']['unselectedLoot'],
    images['tabs']['loot']['unselectedLootWithNewestMessage'],
    images['tabs']['loot']['unselectedLootWithUnreadMessage'],
])
def getLootTabPosition(_: GrayImage) -> Tuple[BBox, int]:
    pass


# TODO: add unit tests
# TODO: add perf
def sendMessage(screenshot: GrayImage, phrase: str):
    enableChatOn(screenshot)
    typeKeyboard(phrase)
