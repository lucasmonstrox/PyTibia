from ahocorapy.keywordtree import KeywordTree
from hud.core import getLeftSidebarArrows
import pathlib
import utils.core
import utils.image
import utils.mouse


currentPath = pathlib.Path(__file__).parent.resolve()
chatMenuImg = utils.image.loadAsGrey(f'{currentPath}/images/chatMenu.png')
chatOnImg = utils.image.loadAsGrey(f'{currentPath}/images/chatOn.png')
chatOnImgTemp = utils.image.loadAsGrey(f'{currentPath}/images/chatOnTemp.png')
chatOffImg = utils.image.loadAsGrey(f'{currentPath}/images/chatOff.png')
chatOffImg = utils.image.loadAsGrey(f'{currentPath}/images/chatOff.png')
lootOfTextImg = utils.image.loadAsGrey(f'{currentPath}/images/lootOfText.png')
nothingTextImg = utils.image.loadAsGrey(f'{currentPath}/images/nothingText.png')

chatTabs = [
    ('loot', (utils.image.loadAsGrey(f'{currentPath}/images/loot.png'), utils.image.loadAsGrey(f'{currentPath}/images/selectedLootTab.png'))),
    ('npcs', (utils.image.loadAsGrey(f'{currentPath}/images/NPCs.png'), utils.image.loadAsGrey(f'{currentPath}/images/selectedNPCsTab.png'))),
    ('localChat', (utils.image.loadAsGrey(f'{currentPath}/images/localChat.png'),
     utils.image.loadAsGrey(f'{currentPath}/images/selectedLocalChatTab.png')))]

chatTabs = dict(chatTabs)

oldListOfLootCheck = []


def readMessagesFromActiveChatTab(screenshot):
    (x, y, width, height) = getChatMessagesContainerPos(screenshot)
    chatMessagesContainer = utils.image.crop(screenshot, x, y, width, height)
    chatMessagesContainer = utils.image.convertGraysToBlack(
        chatMessagesContainer)
    messages = utils.image.toString(chatMessagesContainer, "6").splitlines()
    messages = list(filter(None, messages))
    return messages


def hasNewLoot(screenshot):
    global oldListOfLootCheck
    lootLines = getLootLines(screenshot)
    if len(lootLines) == 0:
        return False
    listOfLootCheck = []
    start = 5
    if len(lootLines) - 5 <= 0:
        start = len(lootLines)
    for i in range(len(lootLines) - start, len(lootLines)):
        listOfLootCheck.append(utils.core.hashit(
            utils.image.convertGraysToBlack(lootLines[i][0])))
    if len(listOfLootCheck) != 0 and len(oldListOfLootCheck) == 0:
        oldListOfLootCheck = listOfLootCheck
        return True
    for newLootLine in listOfLootCheck:
        if newLootLine not in oldListOfLootCheck:
            oldListOfLootCheck = listOfLootCheck
            return True
    oldListOfLootCheck = listOfLootCheck
    return False


def getLootLines(screenshot):
    (x, y, w, h) = getChatMessagesContainerPos(screenshot)
    messages = screenshot[y: y + h, x: x + w]
    lootLines = utils.core.locateMultiple(lootOfTextImg, messages)
    linesWithLoot = []
    for line in lootLines:
        line = x, line[1] + y, w, line[3]
        lineImg = screenshot[line[1]:line[1] +
                             line[3], line[0]:line[0] + line[2]]
        nothingFound = utils.core.locate(nothingTextImg, lineImg)
        if nothingFound is None:
            linesWithLoot.append((lineImg, line))
    return linesWithLoot


def searchInActiveChatTab(activeChatText, patterns):
    kwtree = KeywordTree(case_insensitive=True)
    for i in range(len(patterns)):
        kwtree.add(patterns[i])
    kwtree.finalize()

    processedChatText = []
    for i in range(len(activeChatText)):
        results = kwtree.search_all(activeChatText[i])
        if len(patterns) == len(list(results)):
            processedChatText.append(activeChatText[i])
    return processedChatText


@utils.core.cacheObjectPos
def getChatMenuPos(screenshot):
    return utils.core.locate(screenshot, chatMenuImg)


@utils.core.cacheObjectPos
def getChatOffPos(screenshot):
    return utils.core.locate(screenshot, chatOffImg, confidence=0.985)


def getChatStatus(screenshot):
    chatOffPos = getChatOffPos(screenshot)
    if chatOffPos:
        return chatOffPos, False
    chatOnPos = utils.core.locate(screenshot, chatOnImgTemp, confidence=0.9)
    return chatOnPos, True


def enableChatOn(screenshot):
    (_, chatIsOn) = getChatStatus(screenshot)
    chatIsNotOn = chatIsOn is False
    if chatIsNotOn:
        utils.core.press('enter')


def enableChatOff(screenshot):
    (_, chatIsOn) = getChatStatus(screenshot)
    if chatIsOn:
        utils.core.press('enter')


@utils.core.cacheObjectPos
def getChatsTabsContainer(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenuPos = getChatMenuPos(screenshot)
    return leftSidebarArrows[0] + 10, chatMenuPos[1], chatMenuPos[0] - (leftSidebarArrows[0] + 10), 20


@utils.core.cacheObjectPos
def getChatMessagesContainerPos(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenuPos(screenshot)
    chatStatus = getChatStatus(screenshot)
    return leftSidebarArrows[0], chatMenu[1] + 18, chatStatus[0][0] + 40, (chatStatus[0][1] - 6) - (chatMenu[1] + 13)


@utils.core.cacheObjectPos
def getLootTabPos(screenshot):
    return utils.core.locate(screenshot, chatTabs['loot'][0])


@utils.core.cacheObjectPos
def getNPCsTabPos(screenshot):
    return utils.core.locate(screenshot, chatTabs['npcs'][0])


@utils.core.cacheObjectPos
def getLocalChatTabPos(screenshot):
    return utils.core.locate(screenshot, chatTabs['localChat'][0])


def isTabSelected(screenshot, tabName):
    isSelected = utils.core.locate(screenshot, chatTabs[tabName][1]) is not None
    return isSelected


def selectLootTab(screenshot):
    (x, y, _, _) = getLootTabPos(screenshot)
    utils.mouse.leftClick(x, y)


def selectNPCsTab(screenshot):
    (x, y, _, _) = getNPCsTabPos(screenshot)
    utils.mouse.leftClick(x, y)


def selectLocalChatTab(screenshot):
    (x, y, _, _) = getLocalChatTabPos(screenshot)
    utils.mouse.leftClick(x, y)


def sendMessage(screenshot, phrase):
    enableChatOn(screenshot)
    utils.core.typeKeyboard(phrase)
