import pyautogui
from src.shared.typings import XYCoordinate


# TODO: add unit tests
def drag(x1y1: XYCoordinate, x2y2: XYCoordinate):
    pyautogui.moveTo(x1y1[0], x1y1[1])
    pyautogui.dragTo(x2y2[0], x2y2[1], button='left')


# TODO: add unit tests
def leftClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.leftClick()
        return
    pyautogui.leftClick(windowCoordinate[0], windowCoordinate[1])


# TODO: add unit tests
def moveTo(windowCoordinate: XYCoordinate):
    pyautogui.moveTo(windowCoordinate[0], windowCoordinate[1])


# TODO: add unit tests
def scroll(clicks: int):
    pyautogui.scroll(clicks)


# TODO: add unit tests
def rightClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.rightClick()
        return
    pyautogui.rightClick(windowCoordinate[0], windowCoordinate[1])
