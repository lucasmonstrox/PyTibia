import pyautogui
from ahocorapy.keywordtree import KeywordTree
from hud.core import getLeftSidebarArrows
import utils.core, utils.image

chatMenuImg = utils.image.loadAsArray('chat/images/chatMenu.png')
chatOnImg = utils.image.loadAsArray('chat/images/chatOn.png')
chatOnImgTemp = utils.image.loadAsArray('chat/images/chatOnTemp.png')
chatOffImg = utils.image.loadAsArray('chat/images/chatOff.png')
chatOffImg = utils.image.loadAsArray('chat/images/chatOff.png')
lootOfTextImg = utils.image.loadAsArray('chat/images/lootOfText.png')
nothingTextImg = utils.image.loadAsArray('chat/images/nothingText.png')

oldListOfLootCheck = []


def readMessagesFromActiveChatTab(screenshot):
    (x, y, width, height) = getChatMessagesContainerPos(screenshot)
    chatMessagesContainer = utils.image.crop(screenshot, x, y, width, height)
    chatMessagesContainer = utils.image.convertGraysToBlack(chatMessagesContainer)
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
        listOfLootCheck.append(utils.core.hashit(utils.image.convertGraysToBlack(lootLines[i][0])))

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
        lineImg = screenshot[line[1]:line[1] + line[3], line[0]:line[0] + line[2]]
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


def getChatsTabs(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenuPos(screenshot)
    return leftSidebarArrows[0] + 10, chatMenu[1], chatMenu[0] - (leftSidebarArrows[0] + 10), 20


def getChatMessagesContainerPos(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenuPos(screenshot)
    chatStatus = getChatStatus(screenshot)
    return leftSidebarArrows[0], chatMenu[1] + 18, chatStatus[0][0] + 40, (chatStatus[0][1] - 6) - (chatMenu[1] + 13)


def getChatsTabText(screenshot):
    chatCoordinates = getChatsTabs(screenshot)
    chatsBar = utils.image.crop(screenshot, chatCoordinates[0], chatCoordinates[1], chatCoordinates[2],
                                chatCoordinates[3])
    chatsBar = utils.image.convertGraysToBlack(chatsBar)
    d = utils.image.toTextData(chatsBar, 'tessedit_char_whitelist=abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n_boxes = len(d['level'])

    return n_boxes, d, chatCoordinates


def getServerLogTabPos(screenshot):
    n_boxes, d, chatCoordinates = getChatsTabText(screenshot)
    for i in range(n_boxes - 1):
        if d['text'][i] == 'Server' and d['text'][i + 1] == 'Log':
            (x, y, width, height) = (d['left'][i], d['top'][i], (d['left'][i + 1] + d['width'][i + 1]) - d['left'][i],
                                     (d['top'][i + 1] + d['height'][i + 1]) - d['top'][i])
            break
    x += chatCoordinates[0]
    y += chatCoordinates[1]
    return x, y, width, height


def getLootTabPos(screenshot):
    n_boxes, d, chatCoordinates = getChatsTabText(screenshot)
    for i in range(n_boxes - 1):
        if 'Loot' in d['text'][i]:
            (x, y, width, height) = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
            break
    x += chatCoordinates[0]
    y += chatCoordinates[1]
    return x, y, width, height


def selectServerLogTab(screenshot):
    clickCoord = getServerLogTabPos(screenshot)
    clickCoord = utils.core.randomCoord(clickCoord[0], clickCoord[1], clickCoord[2], clickCoord[3])
    pyautogui.click(clickCoord[0], clickCoord[1])


def selectLootTab(screenshot):
    clickCoord = getLootTabPos(screenshot)
    clickCoord = utils.core.randomCoord(clickCoord[0], clickCoord[1], clickCoord[2], clickCoord[3])
    pyautogui.click(clickCoord[0], clickCoord[1])


def sendMessage(screenshot, phrase):
    enableChatOn(screenshot)
    utils.core.typeKeyboard(phrase)
