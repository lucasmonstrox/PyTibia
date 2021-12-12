from mss import mss
import win32con
import win32ui
import win32gui
import cv2 as cv
# import cupy as cp
from player import player
from radar import radar
import asyncio
import pyautogui
import rx
import numpy as np
from utils import utils
from time import sleep, time
from PIL import Image
from threading import Thread
from skimage import data
from skimage.feature import match_template
from PIL import ImageGrab
from numba import cuda, jit
from timeit import default_timer as timer
from PIL import Image
import math


def clickHudSqm(x, y):
    pass


def main():
    # (x, y) = radar.getPos()
    # radarMiniArea = np.array(pyautogui.screenshot(region=(x, y, 106, 109)))
    # y0 = (radarMiniArea.shape[0] // 2) - 5
    # y1 = (radarMiniArea.shape[0] // 2) + 5
    # x0 = (radarMiniArea.shape[0] // 2) - 7
    # x1 = (radarMiniArea.shape[0] // 2) + 7
    # radarMiniArea = radarMiniArea[y0:y1, x0:x1]
    while True:
        hudFishableArea = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]).flatten()
        allowedPixels = np.nonzero(hudFishableArea)[0]
        index = np.random.choice(len(allowedPixels), size=1, replace=False)[0]
        lengthPerRow = 14
        x = index % lengthPerRow
        y = math.ceil(index / lengthPerRow)

        hudXY = (6, 36)
        hudWH = (772, 566)
        sqmXSize = 772 // 15
        sqmYSize = 566 // 11

        x = x * sqmXSize + hudXY[0]
        y = y * sqmYSize + hudXY[1]

        fishPos = pyautogui.locateOnScreen('fish.png')
        pyautogui.moveTo(fishPos[0], fishPos[1], duration=3)
        pyautogui.rightClick(fishPos[0], fishPos[1], duration=3)
        pyautogui.moveTo(x, y, duration=3)
        pyautogui.click()
        sleep(5)


if __name__ == '__main__':
    main()
