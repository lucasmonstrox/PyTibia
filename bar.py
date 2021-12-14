import cv2
import d3dshot
from time import time
import cupy as cp
import numpy as np
import pygetwindow as gw
from hud import hud
from utils import utils


def getScreenshot(d3):
    window = gw.getWindowsWithTitle('Tibia - ADM')[0]
    region = (window.top, window.left, window.width - 15, window.height)
    screenshot = d3.screenshot(region=region)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = cp.array(screenshot)
    return screenshot


def main():
    loop_time = time()
    d3 = d3dshot.create(capture_output='numpy')
    screenshot = cp.ascontiguousarray(
        cp.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)))
    while True:
        screenshot = getScreenshot(d3)
        # utils.saveCpImg(screenshot, 'screenshot.png')
        playable = screenshot[35:35 + 352, 151:151 + 480]
        # utils.saveCpImg(playable, 'playable.png')
        playable = playable.flatten()
        creaturesBars = hud.getCreaturesBars(playable)
        print(creaturesBars)
        # break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        # print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
