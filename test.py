import numpy as np
import cv2
from time import sleep, time
import actionBar.slot
import battleList.core
from chat import chat
import hud.creatures
import radar.config, radar.core
import utils.core, utils.image, utils.window
import utils.window
from PIL import Image, ImageOps


def main():
    # loop_time = time()
    window = utils.window.getWindow()
    beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    while True:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        slotCount = actionBar.slot.getSlotCount(screenshot)
        print(slotCount)
        # for digit in np.arange(10):
        # digit = 4
        # number = Image.open('actionBar/images/slotDigits/{}.png'.format(digit))
        # number = ImageOps.grayscale(number)
        # newNumber = np.array(number.copy(), dtype=np.uint8)
        # newNumber = np.where(newNumber == 0, 0, 255)
        # newNumber = np.array(newNumber, dtype=np.uint8)
        # utils.image.save(newNumber, 'actionBar/images/slotDigits/{}.png'.format(digit))
        # utils.image.save(screenshot, 'screenshot.png')
        # radarCoordinate = radar.core.getCoordinate(screenshot)
        # battleListCreatures = battleList.core.getCreatures(screenshot)
        # hudCreatures = hud.creatures.getCreatures(screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
        # if battleList.core.isAttackingSomeCreature(battleListCreatures):
        #     (pixelCoordinateX, pixelCoordinateY) = utils.core.getPixelFromCoordinate(radarCoordinate)
        #     walkableFloorsSqms = radar.config.walkableFloorsSqms.copy()[radarCoordinate[2], pixelCoordinateY-5:pixelCoordinateY+6, pixelCoordinateX-7:pixelCoordinateX+8]
        #     beingAttackedCreature =  hudCreatures[hudCreatures['isBeingAttacked'] == True][0]
        #     hasTargetToCreatureByIndex = hud.creatures.hasTargetToCreatureByIndex(walkableFloorsSqms, hudCreatures['slot'], beingAttackedCreature['slot'])
        #     print('hasTargetToCreatureByIndex', hasTargetToCreatureByIndex)
        # break
        # beingAttackedIndexes = np.where(hudCreatures['isBeingAttacked'] == True)[0]
        # hasCreatureBeingAttacked = len(beingAttackedIndexes) > 0
        # if chat.hasNewLoot(screenshot) and beingAttackedCreature:
        #     corpsesToLoot = np.append(corpsesToLoot, [beingAttackedCreature], axis=0)
        # if hasCreatureBeingAttacked:
        #     beingAttackedCreature = hudCreatures[beingAttackedIndexes[0]]
        # else:
        #     beingAttackedCreature = None
        # timef = (time() - loop_time)
        # timef = timef if timef else 1
        # fps = 1 / timef
        # # print('FPS {}'.format(fps))
        # print('corpsesToLoot', corpsesToLoot)
        # loop_time = time()


if __name__ == '__main__':
    main()
