from time import sleep, time

import cv2

import battleList.core
import hud.creatures
import utils.core
import pygetwindow as gw
import utils.image


def getWindow():
    targetWindowTitle = None
    allTitles = gw.getAllTitles()
    for title in allTitles:
        if title.startswith('Tibia -'):
            targetWindowTitle = title
    hasNoTargetWindowTitle = targetWindowTitle == None
    if hasNoTargetWindowTitle:
        return None
    windowTitles = gw.getWindowsWithTitle(targetWindowTitle)
    hasNoWindowsMatchingTitles = len(windowTitles) == 0
    if hasNoWindowsMatchingTitles:
        return None
    return windowTitles[0]


def main():
    # loop_time = time()
    window = getWindow()

    screensgot = utils.core.getScreenshot(window)
    gray = cv2.cvtColor(screensgot, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('fotopb.png', gray)

    while True:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
        battleListCreatures = battleList.core.getCreatures(screenshot)
        hudCreatures = hud.creatures.getCreatures(screenshot, battleListCreatures)
        print(hudCreatures)
        break
        # timef = (time() - loop_time)
        # timef = timef if timef else 1
        # fps = 1 / timef
        # print('FPS {}'.format(fps))
        # loop_time = time()



if __name__ == '__main__':
    main()
