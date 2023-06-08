import pyautogui


# TODO: add types
# TODO: add unit tests
def drag(x1y1, x2y2):
    pyautogui.moveTo(x1y1[0], x1y1[1])
    pyautogui.dragTo(x2y2[0], x2y2[1], button='left')


# TODO: add types
# TODO: add unit tests
def leftClick(windowCoordinate=None):
    if windowCoordinate is None:
        pyautogui.leftClick()
        return
    pyautogui.leftClick(windowCoordinate[0], windowCoordinate[1])


# TODO: add types
# TODO: add unit tests
def move(windowCoordinate):
    pyautogui.moveTo(windowCoordinate[0], windowCoordinate[1])


# TODO: add types
# TODO: add unit tests
def moveTo(windowCoordinate):
    pyautogui.moveTo(windowCoordinate)


# TODO: add unit tests
def scroll(clicks: int):
    pyautogui.scroll(clicks)


# TODO: add types
# TODO: add unit tests
def rightClick(windowCoordinate=None):
    if windowCoordinate is None:
        pyautogui.rightClick()
        return
    pyautogui.rightClick(windowCoordinate[0], windowCoordinate[1])
