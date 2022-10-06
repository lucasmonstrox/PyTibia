from os import walk
import numpy as np
import cv2
from time import sleep, time
import battleList.core
from chat import chat
import hud.core
import hud.creatures
import radar.config
import radar.core
import utils.core
import utils.image
from PIL import Image, ImageOps
import pathlib
import timeit


def main():
    test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    coordinates = np.array([[1, 2]])
    # fa = test[coordinates[-1:]]
    # print(np.take(test, coordinates, axis=0))
    # beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    # utils.image.save(screenshot, 'screenshot.png')
    radarCoordinate = radar.core.getCoordinate(screenshot)
    battleListCreatures = battleList.core.getCreatures(screenshot)
    # print('battleListCreatures', battleListCreatures)
    hudCreatures = hud.creatures.getCreatures(
        screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
    # closedHoleImg = utils.image.RGBtoGray(
    #     utils.image.load('hud/images/waypoint/closed-hole.png'))
    # hudCoordinate = hud.core.getCoordinate(screenshot)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # hudSliceToLocate = hudImg[0:1, 32:-32]
    # slotImg = hud.core.getSlotImg(hudImg, [7, 6])
    # isClosedHole = utils.core.locate(slotImg, closedHoleImg)
    # utils.image.save(hudImg[0:32, 32:-32], 'hudImg2.png')
    # res = utils.core.locate(hudImg, hudSliceToLocate)
    # print(res)
    # print('hudCreatures', hudCreatures)
    # res = timeit.repeat(lambda: utils.core.locate(
    #     hudImg[0:1, :], hudSliceToLocate), repeat=10, number=1)
    # res = timeit.repeat(lambda: hud.creatures.getCreatures(
    #     screenshot, battleListCreatures, radarCoordinate=radarCoordinate), repeat=10, number=1)
    # print(res)
    # a = new_panel.array([
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10]
    # ])
    # r = np.take(a, [[0, 1, 2], [5, 6, 7]])
    # print(r)
    # while True:
    # loop_time = time()
    # hudCreatures = hud.creatures.getCreatures(
    #     screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
    # # print(hudCreatures)
    # res = battleList.core.isAttackingSomeCreature(battleListCreatures)
    # print(res)
    # battleListCreatures = battleList.core.getCreatures(screenshot)
    # break
    # timef = (time() - loop_time)
    # timef = timef if timef else 1
    # fps = 1 / timef
    # print('FPS {}'.format(fps))


if __name__ == '__main__':
    main()
