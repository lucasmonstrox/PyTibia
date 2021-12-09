

import cv2
import d3dshot
from battle import battleList
from player import player
from time import time
import cupy as cp
import math
import numpy as np
import pyautogui
import pygetwindow as gw
from utils import utils


playable = cp.array(cv2.imread(
    'playable.png', cv2.IMREAD_GRAYSCALE), dtype=cp.uint8)
screenshot = np.array(cv2.imread(
    'screenshot.png', cv2.IMREAD_GRAYSCALE), dtype=cp.uint8)
upperBar = cp.array(cv2.imread(
    'blackbar.png', cv2.IMREAD_GRAYSCALE), dtype=cp.uint8)


'''
[01,02,03,04,05]
[11,12,13,14,15]
[06,07,08,09,10]
'''


i = 61220
lengthPerRow = 480
x = i % lengthPerRow
y = math.ceil(i/lengthPerRow)


# TODO: use asyncio to get possible monsters
def getPossibleMonstersInPlayableWindow(arr, seq):
    r_seq = cp.arange(seq.size)
    # TODO: initialize values directly
    arr = arr[cp.arange(arr.size - seq.size + 1)[:, None] + r_seq]
    possibleMonsters = cp.nonzero((arr == seq).all(1))[0]
    possibleMonsters = cp.where(
        cp.logical_and(
            cp.logical_and(arr[possibleMonsters + 480] == 0,
                           arr[possibleMonsters + 960] == 0),
            arr[possibleMonsters + 1440] == 0
        ),
        0, possibleMonsters
    )
    possibleMonsters = possibleMonsters[possibleMonsters != 0]
    return possibleMonsters


def getScreenshot(d3):
    window = gw.getWindowsWithTitle('Tibia - ADM')[0]
    region = (window.top, window.left, window.width - 15, window.height)
    screenshot = d3.screenshot(region=region)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    # screenshot = cp.array(screenshot)
    screenshot = np.array(screenshot)
    return screenshot


def main():
    loop_time = time()
    d3 = d3dshot.create(capture_output='numpy')
    # playableFlatten = playable.flatten()
    screenshot = np.ascontiguousarray(
        np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)))
    while True:
        # screenshot = getScreenshot(d3)
        battleList.getCreatures(screenshot)
        # break
        # playable = screenshotCp[35:35 + 352, 151:151 + 480]
        # playableFlatten = playable.flatten()
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
