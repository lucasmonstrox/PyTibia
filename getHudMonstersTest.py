import cv2
import numpy as np
from time import time
from hud import hud
from battleList import battleList
from utils import utils


def main():
    loop_time = time()
    screenshot = np.ascontiguousarray(
        np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)))
    while True:
        screenshot = utils.getScreenshot()
        playable = screenshot[35:35 + 352, 64:64 + 480]
        playableFlattened = playable.flatten()
        battleListCreatures = battleList.getCreatures(screenshot)
        hasNoBattleListCreatures = len(battleListCreatures) == 0
        if hasNoBattleListCreatures:
            print('There is no battle list creatures')
            continue
        creaturesBars = hud.getCreaturesBars(playableFlattened)
        hasNoHudCreaturesBars = len(creaturesBars) == 0
        if hasNoHudCreaturesBars:
            print('There is no hud creatures bars')
            continue
        creatures = hud.getCreatures(
            playable, creaturesBars, battleListCreatures)
        print(creatures)
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
