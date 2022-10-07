from os import walk
import numpy as np
import cv2
from time import sleep, time
import battleList.core
from chat import chat
import hud.creatures
import hud.core
import radar.config
import radar.core
import skills.core
import utils.core
import utils.image
from PIL import Image, ImageOps
import pathlib
import timeit


def main():
    # beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    # hudCoordinate = hud.core.getCoordinate(screenshot)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    radarCoordinate = radar.core.getCoordinate(screenshot)
    battleListCreatures = battleList.core.getCreatures(screenshot)
    # creaturesBars = hud.creatures.getCreaturesBars(hudImg)
    hudCreatures = hud.creatures.getCreatures(
        screenshot, battleListCreatures, radarCoordinate)
    print(hudCreatures)
    # print(hudCreatures)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # utils.image.save(hudImg, 'hudImg.png')
    # res = timeit.repeat(lambda: skills.core.getStamina(
    #     screenshot), repeat=10, number=1)
    # print(res)


if __name__ == '__main__':
    main()
