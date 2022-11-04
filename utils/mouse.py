from time import sleep
import pyautogui
from hud.core import getCoordinate


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
    pyautogui.mouseDown()
    pyautogui.moveTo(x2, y2, 0.5)
    pyautogui.mouseUp()


def clickOnHud(screenshot, currentCoordinate, clickCoordinate):
    (hudX, hudY, hudW, hudH) = getCoordinate(screenshot)
    (x1, y1, z1) = currentCoordinate
    (x2, y2, z2) = clickCoordinate
    if abs(x1-x2) > 7 or abs(y1-y2) > 5 or z1 != z2:
        return
    (centerX, centerY) = (hudW/2, hudH/2)
    (diffX, diffY) = ((x1-x2)*(hudH/11), (y1-y2)*(hudH/11))
    pyautogui.click(hudX+centerX-diffX, hudY+centerY-diffY)
    sleep(0.25)
