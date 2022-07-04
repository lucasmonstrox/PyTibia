from time import sleep, time
import actionBar.cooldown
from hud import hud
from radar import radar
from utils import utils
import pygetwindow as gw


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
    loop_time = time()
    window = getWindow()
    while True:
        screenshot = utils.getScreenshot(window)
        print(actionBar.cooldown.hasAttackCooldown(screenshot))
        print(actionBar.cooldown.hasExoriCooldown(screenshot))
        print(actionBar.cooldown.hasExoriGranCooldown(screenshot))
        print(actionBar.cooldown.hasExoriMasCooldown(screenshot))
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()
        

if __name__ == '__main__':
    main()
