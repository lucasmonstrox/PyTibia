import pyautogui


def hotkey(*args):
    pyautogui.hotkey(*args)


def keyDown(key: str):
    pyautogui.keyDown(key)


def keyUp(key: str):
    pyautogui.keyUp(key)


def press(*args):
    pyautogui.press(*args)


def write(phrase: str):
    pyautogui.write(phrase)