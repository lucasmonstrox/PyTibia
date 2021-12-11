

import cv2
import d3dshot
from battleList import battleList
import numpy as np
import pygetwindow as gw
from time import time


def getScreenshot(d3):
    window = gw.getWindowsWithTitle('Tibia - ADM')[0]
    region = (window.top, window.left, window.width - 15, window.height)
    screenshot = d3.screenshot(region=region)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = np.array(screenshot)
    return screenshot


def main():
    loop_time = time()
    d3 = d3dshot.create(capture_output='numpy')
    screenshot = np.ascontiguousarray(
        np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)))
    while True:
        # screenshot = getScreenshot(d3)
        creatures = battleList.getCreatures(screenshot)
        # print(creatures, flush=True)
        # break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
