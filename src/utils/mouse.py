import pyautogui


def leftClick(x, y):
    pyautogui.leftClick(x, y)


def rightClick(x, y):
    pyautogui.rightClick(x, y)


def mouseMove(x, y):
    pyautogui.moveTo(x, y)


def mouseScroll(scrolls):
    pyautogui.vscroll(scrolls)


def mouseDrag(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, button='left')
