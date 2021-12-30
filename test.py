import cv2
import numpy as np
from time import time
from hud import hud
from utils import utils


def main():
    loop_time = time()
    while True:
        screenshot = utils.getScreenshot()
        hudCoordinates = hud.getCoordinates(screenshot)
        # hud.clickSlot((7, 4), hudCoordinates)
        hud.rightClickSlot((1, 0), hudCoordinates)
        print(hudCoordinates)
        break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
