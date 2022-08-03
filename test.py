import numpy as np
from time import sleep, time
import battleList.core
from chat import chat
import hud.creatures
import radar.config, radar.core
import utils.core, utils.image, utils.window
import utils.window


def main():
    # loop_time = time()
    window = utils.window.getWindow()
    beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    while True:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
        radarCoordinate = radar.core.getCoordinate(screenshot)
        battleListCreatures = battleList.core.getCreatures(screenshot)
        hudCreatures = hud.creatures.getCreatures(screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
        if battleList.core.isAttackingSomeCreature(battleListCreatures):
            (pixelCoordinateX, pixelCoordinateY) = utils.core.getPixelFromCoordinate(radarCoordinate)
            walkableFloorsSqms = radar.config.walkableFloorsSqms.copy()[radarCoordinate[2], pixelCoordinateY-5:pixelCoordinateY+6, pixelCoordinateX-7:pixelCoordinateX+8]
            beingAttackedCreature =  hudCreatures[hudCreatures['isBeingAttacked'] == True][0]
            hasTargetToCreatureByIndex = hud.creatures.hasTargetToCreatureByIndex(walkableFloorsSqms, hudCreatures['slot'], beingAttackedCreature['slot'])
            print('hasTargetToCreatureByIndex', hasTargetToCreatureByIndex)
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
