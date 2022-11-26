from os import walk
import easyocr
import numpy as np
import cv2
from time import sleep, time
import actionBar.core
import actionBar.locators
import battleList.core
from chat import core
import hud.core
import hud.creatures
import hud.slot
import radar.core
import radar.locators
import radar.extractors
import skills.core
import utils.core
import utils.image
from PIL import Image, ImageOps
import pathlib
import timeit
import dxcam
import scipy.fft
import gameplay.waypoint
from PIL import Image
from inventory.core import getBackpackSlotImg, openBackpack


def main():
    test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    coordinates = np.array([[1, 2]])
    # fa = test[coordinates[-1:]]
    # beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    # map = utils.image.RGBtoGray(
    #     utils.image.load('radar/images/paths/floor-11.png'))
    # reader = easyocr.Reader(['en'])
    # while True:
    # nonGrayScreenshot = utils.core.getScreenshot()
    nonGrayScreenshot = utils.image.load('screenshot.png')
    screenshot = utils.image.RGBtoGray(nonGrayScreenshot)
    # backpackSlotImg = getBackpackSlotImg(screenshot, 'fur backpack', 1)
    # utils.image.save(screenshot, 'screenshot.png')
    hudSize = (960, 704)
    resolution = 1080
    battleListCreatures = battleList.core.getCreatures(screenshot)
    hudCoordinate = hud.core.getCoordinate(screenshot, hudSize)
    hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate, hudSize)
    coordinate = radar.core.getCoordinate(screenshot)
    hudCreatures = hud.creatures.getCreatures(
        battleListCreatures, 'left', hudCoordinate, hudImg, coordinate, resolution)
    targetCreature = hud.creatures.getTargetCreature(hudCreatures)
    print(hudCreatures)
    # def getBattleListCreatures():
    #     battleList.core.getCreatures(screenshot)

    # def getHudCreatures():
    #     hud.creatures.getCreatures(
    #         battleListCreatures, 'left', hudCoordinate, hudImg, coordinate, resolution)
    # res2 = timeit.repeat(lambda: getBattleListCreatures(), repeat=10, number=1)
    # monsters = hud.creatures.getCreatureByType(hudCreatures, 'creature')
    # players = hud.creatures.getCreatureByType(hudCreatures, 'player')
    # closestCreature = hud.creatures.getClosestCreature(
    #     hudCreatures, coordinate)
    # radar.core.goToCoordinate(screenshot, coordinate, [33094, 32790, 7])
    # def cenas(screenshot):
    #     floorLevel = radar.core.getFloorLevel(screenshot)
    #     cannotGetFloorLevel = floorLevel is None
    #     if cannotGetFloorLevel:
    #         return None
    #     radarToolsPos = radar.locators.getRadarToolsPos(screenshot)
    #     cannotGetRadarToolsPos = radarToolsPos is None
    #     if cannotGetRadarToolsPos:
    #         return None
    #     radarImg = radar.extractors.getRadarImg(screenshot, radarToolsPos)
    #     radarHashedImg = utils.core.hashitHex(radarImg)
    # res2 = timeit.repeat(lambda: cenas(screenshot), repeat=10, number=1)
    # utils.image.save(screenshot, 'screenshot.png')
    # count2 = actionBar.core.getSlotCount(screenshot, '1')
    # if count2 == 7:
    #     utils.image.save(screenshot, 'screenshot-7.png')
    #     return
    # if count2 == 53:
    #     utils.image.save(screenshot, 'screenshot.png')
    # utils.image.save(screenshot, 'screenshot.png')
    # hudCoordinate = hud.core.getCoordinate(screenshot)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # utils.image.save(hudImg, 'hudImg.png')
    # coordinate = radar.core.getCoordinate(screenshot)
    # battleListCreatures = battleList.core.getCreatures(screenshot)
    # hudCreatures = hud.creatures.getCreatures(
    #     battleListCreatures, 'left', hudCoordinate, hudImg, coordinate)
    # walkpoints = gameplay.waypoint.generateFloorWalkpoints(
    #     coordinate, [33093, 32788, 7])
    # count1 = actionBar.core.getSlotCount(screenshot, '2')

    # closestCreature = hud.creatures.getClosestCreature(
    #     hudCreatures, coordinate)
    # targetCreature = hud.creatures.getTargetCreature(hudCreatures)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # utils.image.save(hudImg, 'hudImg.png')
    # res1 = timeit.repeat(lambda: np.fft.fft(
    #     np.ascontiguousarray(lava3)), repeat=10, number=1)
    # res2 = timeit.repeat(lambda: utils.core.hashit(lava3), repeat=10, number=1)


if __name__ == '__main__':
    main()
