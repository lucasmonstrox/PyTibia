import pyautogui
from hud.hud import getLeftSidebarArrows
from utils import utils
import pytesseract
from pytesseract import Output

from utils.utils import cropImg

chatMenuImg = utils.loadImgAsArray('chat/images/chatMenu.png')
chatOnImg = utils.loadImgAsArray('chat/images/chatOn.png')
chatOnImgTemp = utils.loadImgAsArray('chat/images/chatOnTemp.png')
chatOffImg = utils.loadImgAsArray('chat/images/chatOff.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def readMessages(screenshot):
    messagesCoordinates = getMessagesBox(screenshot)
    messagesBox = cropImg(screenshot, messagesCoordinates[0], messagesCoordinates[1], messagesCoordinates[2],
                          messagesCoordinates[3])
    d = pytesseract.image_to_string(messagesBox, lang=None, config='--oem 3 --psm 6')
    output = d.splitlines()
    filteredOutput = []
    del output[0]
    for i in range(len(output)):
        output[i] = output[i].strip()
        if len(output[i]) > 2:
            filteredOutput.append(output[i])

    return filteredOutput


def getChatMenu(screenshot):
    return utils.locate(screenshot, chatMenuImg)


def getChatStatus(screenshot):
    chatStatus = utils.locate(screenshot, chatOnImgTemp, 0.985)
    if chatStatus is None:
        return utils.locate(screenshot, chatOffImg, 0.985), False
    else:
        return chatStatus, True


def setChat(screenshot, flag):
    if flag is True:
        if getChatStatus(screenshot)[1] is False:
            utils.press('enter')
    else:
        if getChatStatus(screenshot)[1] is True:
            utils.press('enter')


def getChatsBox(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenu(screenshot)
    return leftSidebarArrows[0] + 10, chatMenu[1], chatMenu[0] - (leftSidebarArrows[0] + 10), 20


def getMessagesBox(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    chatMenu = getChatMenu(screenshot)
    chatStatus = getChatStatus(screenshot)
    return leftSidebarArrows[0], chatMenu[1] + 18, chatStatus[0][0] + 40, (chatStatus[0][1] - 6) - (chatMenu[1] + 13)


def getServerLog(screenshot):
    chatCoordinates = getChatsBox(screenshot)
    chatsBar = cropImg(screenshot, chatCoordinates[0], chatCoordinates[1], chatCoordinates[2], chatCoordinates[3])
    d = pytesseract.image_to_data(chatsBar, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes - 1):
        if d['text'][i] == 'Server' and d['text'][i + 1] == 'Log':
            (x, y, width, height) = (d['left'][i], d['top'][i], (d['left'][i + 1] + d['width'][i + 1]) - d['left'][i],
                                     (d['top'][i + 1] + d['height'][i + 1]) - d['top'][i])
            break

    x += chatCoordinates[0]
    y += chatCoordinates[1]

    return x, y, width, height


def setServerLog(screenshot):
    clickCoord = getServerLog(screenshot)
    clickCoord = utils.randomCoord(clickCoord[0], clickCoord[1], clickCoord[2], clickCoord[3])
    pyautogui.click(clickCoord[0], clickCoord[1])


def sendMessage(screenshot, phrase):
    setChat(screenshot, True)
    utils.typeKeyboard(phrase)
