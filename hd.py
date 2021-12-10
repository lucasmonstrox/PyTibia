

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


dromedaryHash = cp.array(cv2.imread(
    'dromedaryHash.png', cv2.IMREAD_GRAYSCALE)).flatten()
dromedaryHash = cp.where(dromedaryHash == 0, 1, 0)
dromedaryHashKeys = cp.nonzero(dromedaryHash)

frostDragonHash = cp.array(cv2.imread(
    'frostDragonHash.png', cv2.IMREAD_GRAYSCALE)).flatten()
frostDragonHash = cp.where(frostDragonHash == 0, 1, 0)
frostDragonHashKeys = cp.nonzero(frostDragonHash)

messHash = cp.array(cv2.imread('messHash.png', cv2.IMREAD_GRAYSCALE))

creaturesHashes = {
    "Dromedary": {
        "hash": dromedaryHash,
        "hashKeys": dromedaryHashKeys
    },
    "Frost Dragon": {
        "hash": frostDragonHash,
        "hashKeys": frostDragonHashKeys
    }
}


def getMonsterNameFromMessHash(creaturesNames, possibleCreatureHash):
    possibleCreatureHash = possibleCreatureHash.flatten()
    possibleCreatureHash = cp.where(possibleCreatureHash == 0, 1, 0)
    creatureHash = possibleCreatureHash.flatten()
    for creatureName in creaturesNames:
        pixelsOfName = cp.take(
            creatureHash, creaturesHashes[creatureName]["hashKeys"])
        isSameCreature = cp.all(pixelsOfName == 1)
        if isSameCreature:
            return creatureName


def main():
    loop_time = time()
    while True:
        print(getMonsterNameFromMessHash(
            ["Dromedary", "Frost Dragon"], messHash))
        break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
