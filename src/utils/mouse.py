import pyautogui


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def leftClick(x, y):
    pyautogui.leftClick(x, y)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def rightClick(x, y):
    pyautogui.rightClick(x, y)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def mouseMove(x, y):
    pyautogui.moveTo(x, y)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def mouseScroll(scrolls):
    pyautogui.vscroll(scrolls)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def mouseDrag(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, button='left')
