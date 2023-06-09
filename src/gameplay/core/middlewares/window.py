import win32gui
import re
from ...typings import Context


def setTibiaWindowMiddleware(gameContext: Context):
    '''
        Windows middleware to set the Tibia window
    '''
    windowsList: list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windowsList) # hwnd -> window handler
    windowsNames = list(
        map(lambda hwnd: win32gui.GetWindowText(hwnd), windowsList)
    )
    regex = re.compile(r'Tibia - .*')

    gameContext['window'] = list(
        filter(lambda window_name: regex.match(window_name), windowsNames)
    )
    if len(gameContext['window']) > 0: # if have more than one window, get the first
        gameContext['window'] = gameContext['window'][0]
        return gameContext
    raise Exception('Tibia window not found')