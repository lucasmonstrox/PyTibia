

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


def getCreaturesPositions(arr, seq):
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
