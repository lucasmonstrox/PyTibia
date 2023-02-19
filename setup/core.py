import configparser
import pathlib
import pyautogui
from time import sleep, time
import hud.core
import utils.core
from utils.core import cacheObjectPos
import utils.image
import utils.mouse


currentPath = pathlib.Path(__file__).parent.resolve()
default = None
login = None
loginScreenImg = utils.image.loadAsGrey(f'{currentPath}/setup/images/login-screen.png')
tibiaIconImg = utils.image.loadAsGrey(f'{currentPath}/setup/images/tibia-icon.png')
emptyFieldImg = utils.image.loadAsGrey(f'{currentPath}/setup/images/empty-field.png')
selectCharWindowImg = utils.image.loadAsGrey(
    f'{currentPath}/setup/images/select-char-window.png')
wrongCredImg = utils.image.loadAsGrey(f'{currentPath}/setup/images/wrong-cred.png')
deadScreenImg = utils.image.loadAsGrey(f'{currentPath}/setup/images/dead-screen.png')


def loadConfigs():
    global default, login
    config = configparser.ConfigParser()
    config.read(f'{currentPath}/setup/pytibia.ini')
    default = config['DEFAULT']
    login = config['LOGIN']


@cacheObjectPos
def getLoginWindowCoord(screenshot):
    return utils.core.locate(screenshot, loginScreenImg)


@cacheObjectPos
def getCharacterWindowCoord(screenshot):
    return utils.core.locate(screenshot, selectCharWindowImg)


def isEmailEmpty(screenshot):
    (x, y, _, _) = getLoginWindowCoord(screenshot)
    x = x + 91
    y = y + 28
    result = utils.core.locate(utils.image.crop(
        screenshot, x, y, 13, 22), emptyFieldImg, confidence=0.99)

    if result is None:
        return False
    else:
        return True


def setEmail(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    utils.mouse.leftClick(x + 103, y + 39)
    if isEmailEmpty(screenshot) is False:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
    pyautogui.typewrite(login['Email'])


def isPasswordEmpty(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    x = x + 91
    y = y + 58

    result = utils.core.locate(utils.image.crop(
        screenshot, x, y, 13, 22), emptyFieldImg, confidence=0.99)

    if result is None:
        return False
    else:
        return True


def setPassword(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    utils.mouse.leftClick(x + 103, y + 69)
    if isPasswordEmpty(screenshot) is False:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
    pyautogui.typewrite(login['Password'])
    return


def openClient(screenshot):
    iconCoord = utils.core.locate(tibiaIconImg, screenshot)
    if iconCoord is not None:
        (x, y, _, _) = iconCoord
        utils.mouse.leftClick(x, y)

    openClientTimeout = float(default['openClientTimeout'])
    openClientStartTime = time()
    elapsedOpenClientTime = 0.0
    print('Waiting for client to open...')
    LoginScreenPos = None
    while elapsedOpenClientTime < openClientTimeout:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        elapsedOpenClientTime = time() - openClientStartTime
        LoginScreenPos = getLoginWindowCoord(screenshot)

        if LoginScreenPos is not None:
            break

    if LoginScreenPos is None:
        print('Opening up time out')
        return
    else:
        print(f'Client opened in: {elapsedOpenClientTime} seconds')

    return


def logIn():

    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    setEmail(screenshot)
    setPassword(screenshot)
    utils.core.press('enter')
    loginTimeout = float(default['LoginTimeout'])
    loginStartTime = time()
    elapsedLoginTime = 0.0
    print('Waiting for character screen to show...')
    charScreenPos = None
    while elapsedLoginTime < loginTimeout:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        elapsedLoginTime = time() - loginStartTime
        charScreenPos = getCharacterWindowCoord(screenshot)
        wrongCredPos = utils.core.locate(wrongCredImg, screenshot)

        if wrongCredPos is not None:
            print('Wrong login credentials')
            return
        if charScreenPos is not None:
            break

    if charScreenPos is None:
        print('Character screen time out')
        return
    else:
        print(f'Character screen loaded in: {elapsedLoginTime} seconds')

    for i in range(0, int(login['CharacterIndex'])):
        utils.core.press('down')

    utils.core.press('enter')

    worldConnectTimeout = float(default['worldConnectTimeout'])
    worldConnectStartTime = time()
    elapsedWorldConnectTime = 0.0
    print('Waiting for character screen to show...')
    LeftSidebarArrowPos = None
    while elapsedWorldConnectTime < worldConnectTimeout:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        elapsedWorldConnectTime = time() - worldConnectStartTime
        LeftSidebarArrowPos = hud.core.getLeftSidebarArrows(screenshot)
        if LeftSidebarArrowPos is not None:
            break

    if LeftSidebarArrowPos is None:
        print('World load time out')
        return
    else:
        print(f'Game World loaded in: {elapsedWorldConnectTime} seconds')

    return


def isLoggedIn(screenshot):
    LeftSidebarArrowPos = hud.core.getLeftSidebarArrows(screenshot)
    if LeftSidebarArrowPos is None:
        return False
    return True


def checkDeathAndRelogin(screenshot):
    isDead = utils.core.locate(deadScreenImg, screenshot)
    if isDead is not None:
        print('Death detected, restarting login...')
        utils.core.press('esc')
        utils.core.press('esc')
        sleep(3)
        logIn()
