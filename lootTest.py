import numpy as np
import cv2
from time import sleep, time
import actionBar.cooldown
import actionBar.slot
import battleList.core
from chat import chat
import hud.creatures
import radar.config
import radar.core
import utils.core
import utils.image
import utils.window
import utils.window
from PIL import Image, ImageOps


def main():
    # loop_time = time()
    window = utils.window.getWindow()
    beingAttackedCreature = None
    corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    previousHudCreatures = np.array([])
    clickedTargetCreature = 123
    lastClickedTarget = None  # [6, 5]
    while True:
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
        # slotCount = actionBar.slot.getSlotCount(screenshot)
        radarCoordinate = radar.core.getCoordinate(screenshot)
        battleListCreatures = battleList.core.getCreatures(screenshot)
        currentHudCreatures = hud.creatures.getCreatures(
            screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
        beingAttackedIndexes = np.where(
            currentHudCreatures['isBeingAttacked'] == True)[0]
        hasCreatureBeingAttacked = len(beingAttackedIndexes) > 0
        hasNewLoot = chat.hasNewLoot(screenshot)
        if hasNewLoot and beingAttackedCreature:
            corpsesToLoot = np.append(
                corpsesToLoot, [beingAttackedCreature], axis=0)
        if len(previousHudCreatures) > 0 and hasNewLoot and lastClickedTarget:
            creatureIndex = 0
            deathCreature = None
            for creatureSlot in previousHudCreatures['slot']:
                if np.array_equal(creatureSlot, lastClickedTarget):
                    deathCreature = previousHudCreatures[creatureIndex]
                    corpsesToLoot = np.append(
                        corpsesToLoot, [deathCreature], axis=0)
                    lastClickedTarget = None
                    break
                creatureIndex += 1
        print('hasNewLoot', hasNewLoot)
        hasExoriCooldown = actionBar.cooldown.hasExoriCooldown(screenshot)
        print('hasExoriCooldown', hasExoriCooldown)
        if hasNewLoot and hasExoriCooldown:
            targetSlots = np.array([
                [4, 6],
                [4, 7],
                [4, 8],
                [5, 6],
                [5, 8],
                [6, 6],
                [6, 7],
                [6, 8],
            ])
            previousHudCreaturesBySlots = np.array(
                [], dtype=hud.creatures.creatureType)
            currentHudCreaturesBySlots = np.array(
                [], dtype=hud.creatures.creatureType)
            diff = np.array([], dtype=hud.creatures.creatureType)
            for previousHudCreature in previousHudCreatures:
                if np.isin(previousHudCreature['slot'], targetSlots).all():
                    previousHudCreaturesBySlots = np.append(
                        previousHudCreaturesBySlots, [previousHudCreature])
            for currentHudCreature in currentHudCreatures:
                if np.isin(currentHudCreature['slot'], targetSlots).all():
                    currentHudCreaturesBySlots = np.append(
                        currentHudCreaturesBySlots, [currentHudCreature])
            for previousHudCreature in previousHudCreaturesBySlots:
                creatureDoesNotExists = True
                for currentHudCreature in currentHudCreatures:
                    previousHudCreatureHash = utils.core.hashitHex(
                        previousHudCreature)
                    currentHudCreatureHash = utils.core.hashitHex(
                        currentHudCreature)
                    if previousHudCreatureHash == currentHudCreatureHash:
                        creatureDoesNotExists = False
                        break
                if creatureDoesNotExists:
                    diff = np.append(diff, [previousHudCreature])
        if hasCreatureBeingAttacked:
            beingAttackedCreature = currentHudCreatures[beingAttackedIndexes[0]]
        else:
            beingAttackedCreature = None
        previousHudCreatures = currentHudCreatures
        # timef = (time() - loop_time)
        # timef = timef if timef else 1
        # fps = 1 / timef
        # # print('FPS {}'.format(fps))
        print('corpsesToLoot', corpsesToLoot)
        # loop_time = time()


if __name__ == '__main__':
    main()
