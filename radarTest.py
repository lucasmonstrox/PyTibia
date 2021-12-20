

import cv2
import numpy as np
from time import time
from radar import radar
from utils import utils


def main():
    loop_time = time()
    screenshot = np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE))
    while True:
        screenshot = utils.getScreenshot()
        floorLevel = radar.getFloorLevel(screenshot)
        radarToolsPos = radar.getRadarToolsPos(screenshot)
        radarImage = radar.getRadarImage(screenshot, radarToolsPos)
        coordinate = radar.getCoordinate(floorLevel, radarImage)
        print(coordinate)
        # break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
