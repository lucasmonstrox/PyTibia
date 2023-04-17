import configparser
import pathlib
import pyautogui
from time import sleep, time
from src.utils.core import cacheObjectPos, getScreenshot, locate, press
from src.utils.image import loadAsGrey
from src.utils.mouse import leftClick


currentPath = pathlib.Path(__file__).parent.resolve()
default = None
login = None
loginScreenImg = loadAsGrey(f'{currentPath}/setup/images/login-screen.png')
tibiaIconImg = loadAsGrey(f'{currentPath}/setup/images/tibia-icon.png')
emptyFieldImg = loadAsGrey(f'{currentPath}/setup/images/empty-field.png')
selectCharWindowImg = loadAsGrey(
    f'{currentPath}/setup/images/select-char-window.png')
wrongCredImg = loadAsGrey(f'{currentPath}/setup/images/wrong-cred.png')
deadScreenImg = loadAsGrey(f'{currentPath}/setup/images/dead-screen.png')


def loadConfigs():
    global default, login
    config = configparser.ConfigParser()
    config.read(f'{currentPath}/setup/pytibia.ini')
    default = config['DEFAULT']
    login = config['LOGIN']


@cacheObjectPos
def getLoginWindowCoord(screenshot):
    return locate(screenshot, loginScreenImg)


@cacheObjectPos
def getCharacterWindowCoord(screenshot):
    return locate(screenshot, selectCharWindowImg)


def isEmailEmpty(screenshot):
    (x, y, _, _) = getLoginWindowCoord(screenshot)
    x = x + 91
    y = y + 28
    result = locate(crop(
        screenshot, x, y, 13, 22), emptyFieldImg, confidence=0.99)

    if result is None:
        return False
    else:
        return True


def setEmail(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    leftClick(x + 103, y + 39)
    if isEmailEmpty(screenshot) is False:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
    pyautogui.typewrite(login['Email'])


def isPasswordEmpty(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    x = x + 91
    y = y + 58
    result = locate(crop(
        screenshot, x, y, 13, 22), emptyFieldImg, confidence=0.99)
    if result is None:
        return False
    else:
        return True


def setPassword(screenshot):
    (x, y, w, h) = getLoginWindowCoord(screenshot)
    leftClick(x + 103, y + 69)
    if isPasswordEmpty(screenshot) is False:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
    pyautogui.typewrite(login['Password'])


def openClient(screenshot):
    iconCoord = locate(tibiaIconImg, screenshot)
    if iconCoord is not None:
        (x, y, _, _) = iconCoord
        leftClick(x, y)
    openClientTimeout = float(default['openClientTimeout'])
    openClientStartTime = time()
    elapsedOpenClientTime = 0.0
    print('Waiting for client to open...')
    LoginScreenPos = None
    while elapsedOpenClientTime < openClientTimeout:
        screenshot = getScreenshot()
        elapsedOpenClientTime = time() - openClientStartTime
        LoginScreenPos = getLoginWindowCoord(screenshot)
        if LoginScreenPos is not None:
            break
    if LoginScreenPos is None:
        print('Opening up time out')
        return
    print(f'Client opened in: {elapsedOpenClientTime} seconds')


def logIn():
    screenshot = getScreenshot()
    setEmail(screenshot)
    setPassword(screenshot)
    press('enter')
    loginTimeout = float(default['LoginTimeout'])
    loginStartTime = time()
    elapsedLoginTime = 0.0
    charScreenPos = None
    while elapsedLoginTime < loginTimeout:
        screenshot = getScreenshot()
        elapsedLoginTime = time() - loginStartTime
        charScreenPos = getCharacterWindowCoord(screenshot)
        wrongCredPos = locate(wrongCredImg, screenshot)
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
    for _ in range(0, int(login['CharacterIndex'])):
        press('down')
    press('enter')
    worldConnectTimeout = float(default['worldConnectTimeout'])
    worldConnectStartTime = time()
    elapsedWorldConnectTime = 0.0
    print('Waiting for character screen to show...')
    LeftSidebarArrowPos = None
    while elapsedWorldConnectTime < worldConnectTimeout:
        screenshot = getScreenshot()
        elapsedWorldConnectTime = time() - worldConnectStartTime
        # LeftSidebarArrowPos = src.features.hud.core.getLeftSidebarArrows(screenshot)
        LeftSidebarArrowPos = None
        if LeftSidebarArrowPos is not None:
            break
    if LeftSidebarArrowPos is None:
        print('World load time out')
        return
    print(f'Game World loaded in: {elapsedWorldConnectTime} seconds')


def isLoggedIn(screenshot):
    # LeftSidebarArrowPos = src.features.hud.core.getLeftSidebarArrows(screenshot)
    LeftSidebarArrowPos = None
    if LeftSidebarArrowPos is None:
        return False
    return True


def checkDeathAndRelogin(screenshot):
    isDead = locate(deadScreenImg, screenshot)
    if isDead is not None:
        print('Death detected, restarting login...')
        press('esc')
        press('esc')
        sleep(3)
        logIn()
