import pathlib
from typing import Tuple, Union
from src.shared.typings import BBox, GrayImage
# from src.features.gameWindow.core import getLeftSidebarArrows
from src.utils.core import cacheObjectPosition, hashit, locate, locateMultiple, press, typeKeyboard
from src.utils.image import convertGraysToBlack, loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
chatMenuImg = loadFromRGBToGray(f'{currentPath}/images/chatMenu.png')
chatOnImg = loadFromRGBToGray(f'{currentPath}/images/chatOn.png')
chatOnImgTemp = loadFromRGBToGray(f'{currentPath}/images/chatOnTemp.png')
chatOffImg = loadFromRGBToGray(f'{currentPath}/images/chatOff.png')
chatOffImg = loadFromRGBToGray(f'{currentPath}/images/chatOff.png')
lootOfTextImg = loadFromRGBToGray(f'{currentPath}/images/lootOfText.png')
nothingTextImg = loadFromRGBToGray(f'{currentPath}/images/nothingText.png')
chatTabs = [
    ('loot', (loadFromRGBToGray(f'{currentPath}/images/loot.png'), loadFromRGBToGray(f'{currentPath}/images/selectedLootTab.png'))),
    ('npcs', (loadFromRGBToGray(f'{currentPath}/images/NPCs.png'), loadFromRGBToGray(f'{currentPath}/images/selectedNPCsTab.png'))),
    ('localChat', (loadFromRGBToGray(f'{currentPath}/images/localChat.png'),
     loadFromRGBToGray(f'{currentPath}/images/selectedLocalChatTab.png')))]
chatTabs = dict(chatTabs)
oldListOfLootCheck = []


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
# TODO: add typings
def getLootLines(screenshot: GrayImage):
    (x, y, w, h) = getChatMessagesContainerPos(screenshot)
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
def enableChatOff(screenshot: GrayImage):
    (_, chatIsOn) = getChatStatus(screenshot)
    if chatIsOn:
        press('enter')


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getChatsTabsContainer(screenshot: GrayImage) -> Tuple[BBox, int]:
    leftSidebarArrows = None
    # leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenuPos = getChatMenuPosition(screenshot)
    return leftSidebarArrows[0] + 10, chatMenuPos[1], chatMenuPos[0] - (leftSidebarArrows[0] + 10), 20


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@cacheObjectPosition
def getChatMessagesContainerPos(screenshot):
    leftSidebarArrows = None
    # leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenuPosition(screenshot)
    chatStatus = getChatStatus(screenshot)
    return leftSidebarArrows[0], chatMenu[1] + 18, chatStatus[0][0] + 40, (chatStatus[0][1] - 6) - (chatMenu[1] + 13)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def sendMessage(screenshot, phrase):
    enableChatOn(screenshot)
    typeKeyboard(phrase)
