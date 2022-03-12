

from time import time
from battleList import battleList
from utils import utils


def main():
    loop_time = time()
    screenshot = utils.loadImgAsArray('screenshot.png')
    while True:
        screenshot = utils.getScreenshot()
        creatures = battleList.getCreatures(screenshot)
        print(creatures)
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
