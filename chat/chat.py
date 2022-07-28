import pyautogui
from ahocorapy.keywordtree import KeywordTree
from hud.core import getLeftSidebarArrows
import utils.core, utils.image
import pytesseract
from pytesseract import Output

chatMenuImg = utils.image.loadAsArray('chat/images/chatMenu.png')
chatOnImg = utils.image.loadAsArray('chat/images/chatOn.png')
chatOnImgTemp = utils.image.loadAsArray('chat/images/chatOnTemp.png')
chatOffImg = utils.image.loadAsArray('chat/images/chatOff.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def readMessagesFromActiveChatTab(screenshot):
    (x, y, width, height) = getChatMessagesContainerPos(screenshot)
    chatMessagesContainer = utils.image.crop(screenshot, x, y, width, height)
    chatMessagesContainer = utils.image.convertGraysToBlack(chatMessagesContainer)
    messages = utils.image.toString(chatMessagesContainer, "6").splitlines()
    messages = list(filter(None, messages))
    return messages


def getLootMessages(activeChatText):
    return searchInActiveChatTab(activeChatText, ['Loot of'])


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


def getServerLogTabPos(screenshot):
    chatCoordinates = getChatsTabs(screenshot)
    chatsBar = utils.image.crop(screenshot, chatCoordinates[0], chatCoordinates[1], chatCoordinates[2], chatCoordinates[3])
    chatsBar = utils.image.convertGraysToBlack(chatsBar)
    d = utils.image.toTextData(chatsBar)
    n_boxes = len(d['level'])
    for i in range(n_boxes - 1):
        if d['text'][i] == 'Server' and d['text'][i + 1] == 'Log':
            (x, y, width, height) = (d['left'][i], d['top'][i], (d['left'][i + 1] + d['width'][i + 1]) - d['left'][i],
                                     (d['top'][i + 1] + d['height'][i + 1]) - d['top'][i])
            break
    x += chatCoordinates[0]
    y += chatCoordinates[1]
    return x, y, width, height


def selectServerLogTab(screenshot):
    clickCoord = getServerLogTabPos(screenshot)
    clickCoord = utils.core.randomCoord(clickCoord[0], clickCoord[1], clickCoord[2], clickCoord[3])
    pyautogui.click(clickCoord[0], clickCoord[1])


def sendMessage(screenshot, phrase):
    enableChatOn(screenshot)
    utils.core.typeKeyboard(phrase)
