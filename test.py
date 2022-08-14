import numpy as np
import cv2
from time import sleep, time
import actionBar.slot
import battleList.core
from chat import chat
import hud.creatures
import hud.core
import radar.config
import radar.core
import utils.core
import utils.image
import utils.window
import utils.window
from PIL import Image, ImageOps
import pathlib


def main():
    window = utils.window.getWindow()
    beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    radarCoordinate = radar.core.getCoordinate(screenshot)
    battleListCreatures = battleList.core.getCreatures(screenshot)
    print(battleListCreatures)
    hudCoordinate = hud.core.getCoordinate(screenshot)
    hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    creaturesBars = hud.creatures.getCreaturesBars(hudImg.flatten())
    while True:
        loop_time = time()
        # hudCreatures = hud.creatures.getCreatures(
        # screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
        # print(hudCreatures)
        res = battleList.core.isAttackingSomeCreature(battleListCreatures)
        print(res)
        break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))


if __name__ == '__main__':
    main()
