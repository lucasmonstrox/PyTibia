from time import sleep, time
from battleList import battleList
from hud import hud
from player import player
from radar import radar
from utils import utils
import pygetwindow as gw
import numpy as np


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
    while True:
        screenshot = utils.getScreenshot(window)
        battleListCreatures = battleList.getCreatures(screenshot)
        hudCreatures = hud.getCreatures(screenshot, battleListCreatures)
        print(hudCreatures)
        # break
        # timef = (time() - loop_time)
        # timef = timef if timef else 1
        # fps = 1 / timef
        # print('FPS {}'.format(fps))
        # loop_time = time()
    
        

if __name__ == '__main__':
    main()
