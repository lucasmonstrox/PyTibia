import pyautogui
from src.shared.typings import XYCoordinate


def drag(x1y1: XYCoordinate, x2y2: XYCoordinate):
    pyautogui.moveTo(x1y1[0], x1y1[1])
    pyautogui.dragTo(x2y2[0], x2y2[1], button='left')


def leftClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.leftClick()
        return
    pyautogui.leftClick(windowCoordinate[0], windowCoordinate[1])


def moveTo(windowCoordinate: XYCoordinate):
    pyautogui.moveTo(windowCoordinate[0], windowCoordinate[1])


def rightClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.rightClick()
        return
    pyautogui.rightClick(windowCoordinate[0], windowCoordinate[1])


def scroll(clicks: int):
    pyautogui.scroll(clicks)
