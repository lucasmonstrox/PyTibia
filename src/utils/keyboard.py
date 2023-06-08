import pyautogui


def hotkey(*args):
    pyautogui.hotkey(*args)


# TODO: add unit tests
def keyDown(key: str):
    pyautogui.keyDown(key)


# TODO: add unit tests
def keyUp(key: str):
    pyautogui.keyUp(key)


def press(*args):
    pyautogui.press(*args)


# TODO: add unit tests
def write(phrase: str):
    pyautogui.write(phrase)