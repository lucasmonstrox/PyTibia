

import cv2
import d3dshot
from time import time
import cupy as cp
import math
import pygetwindow as gw
from utils import utils


upperBar = cp.array(cv2.imread('blackbar.png', cv2.IMREAD_GRAYSCALE)).flatten()


'''
[01,02,03,04,05]
[11,12,13,14,15]
[06,07,08,09,10]
'''


i = 12
lengthPerRow = 5
x = i % lengthPerRow
y = math.ceil(i / lengthPerRow)


[3, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 0]


# TODO: use asyncio to get possible monsters
def getPossibleMonstersInPlayableWindow(arr, seq):
    r_seq = cp.arange(seq.size)
    # TODO: initialize values directly
    arr = cp.where(arr == 0, 1, 0)
    arrKeys = cp.nonzero(arr == 1)
    print(len(arrKeys[0]))
    # arr = arr[cp.arange(arr.size - seq.size + 1)[:, None] + r_seq]
    # possibleMonsters = cp.nonzero((arr == seq).all(1))[0]
    # if len(possibleMonsters) == 0:
    #     return cp.array([])
    # print(arr[0])
    # possibleMonsters = cp.where(
    # cp.logical_and(
    # cp.logical_and(arr[possibleMonsters + 480] == 0,
    #                arr[possibleMonsters + 960] == 0),
    # arr[possibleMonsters + 1440] == 0
    # ),
    # 0, possibleMonsters
    # )
    # x = possibleMonsters[0] % 480
    # y = math.ceil(possibleMonsters[0] / 480)
    # print('x, y', (x, y))
    # possibleMonsters = possibleMonsters[possibleMonsters != 0]
    # return possibleMonsters


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
        # screenshot = getScreenshot(d3)
        playable = screenshot[35:35 + 352, 151:151 + 480].flatten()
        possibleMonsters = getPossibleMonstersInPlayableWindow(
            playable, upperBar)
        # print(possibleMonsters)
        break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
