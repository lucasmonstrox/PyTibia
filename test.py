from os import walk
import numpy as np
import cv2
from time import sleep, time
import actionBar.core
import battleList.core
from chat import chat
import hud.core
import hud.creatures
import hud.slot
import radar.core
import skills.core
import utils.core
import utils.image
from PIL import Image, ImageOps
import pathlib
import timeit
import dxcam
import scipy.fft
import gameplay.waypoint


def main():
    test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    coordinates = np.array([[1, 2]])
    # fa = test[coordinates[-1:]]
    # print(np.take(test, coordinates, axis=0))
    # beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    # map = utils.image.RGBtoGray(
    #     utils.image.load('radar/images/paths/floor-11.png'))
    nonGrayScreenshot = utils.core.getScreenshot()
    # utils.image.save(nonGrayScreenshot, 'nonGrayScreenshot.png')
    screenshot = utils.image.RGBtoGray(nonGrayScreenshot)
    # utils.image.save(screenshot, 'screenshot.png')
    hudCoordinate = hud.core.getCoordinate(screenshot)
    hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    utils.image.save(hudImg, 'hudImg.png')
    radarCoordinate = radar.core.getCoordinate(screenshot)
    battleListCreatures = battleList.core.getCreatures(screenshot)
    hudCreatures = hud.creatures.getCreatures(
        battleListCreatures, 'left', hudCoordinate, hudImg, radarCoordinate)
    walkpoints = gameplay.waypoint.generateFloorWalkpoints(
        radarCoordinate, [33093, 32788, 7])
    print(walkpoints)
    # closestCreature = hud.creatures.getClosestCreature(
    #     hudCreatures, radarCoordinate)
    # targetCreature = hud.creatures.getTargetCreature(hudCreatures)
    # print(hud.creatures.getNearestCreaturesCount(hudCreatures))
    # print(targetCreature)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # utils.image.save(hudImg, 'hudImg.png')
    # res1 = timeit.repeat(lambda: np.fft.fft(
    #     np.ascontiguousarray(lava3)), repeat=10, number=1)
    # res2 = timeit.repeat(lambda: utils.core.hashit(lava3), repeat=10, number=1)
    # print(res1)
    # print(res2)


if __name__ == '__main__':
    main()
