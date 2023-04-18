import pyautogui


# TODO: add unit tests
def leftClick(x: int, y: int):
    pyautogui.leftClick(x, y)


# TODO: add unit tests
def rightClick(x: int, y: int):
    pyautogui.rightClick(x, y)


# TODO: add unit tests
def mouseMove(x: int, y: int):
    pyautogui.moveTo(x, y)


# TODO: add unit tests
def mouseScroll(scrolls: int):
    pyautogui.vscroll(scrolls)


# TODO: add unit tests
def mouseDrag(x1: int, y1: int, x2: int, y2: int):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, button='left')
