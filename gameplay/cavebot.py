import numpy as np
import pyautogui
import time
import battleList.core
import gameplay.waypoint
import hud.creatures


# TODO: add unit tests
def handleCavebot(battleListCreatures, cavebotManager, hudCreatures, radarCoordinate, walkpointsManager):
    copiedWalkpointsManager = walkpointsManager.copy()
    copyOfCavebotManager = cavebotManager.copy()
    if battleList.core.isAttackingSomeCreature(battleListCreatures):
        copyOfCavebotManager['status'] = 'attackingTarget'
        targetCreature = hud.creatures.getTargetCreature(hudCreatures)
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            copyOfCavebotManager['status'] = None
            return copyOfCavebotManager, copiedWalkpointsManager
        hasNoTargetToTargetCreature = hud.creatures.hasTargetToCreature(
            hudCreatures, targetCreature, radarCoordinate) == False
        if hasNoTargetToTargetCreature:
            targetCreature = hud.creatures.getClosestCreature(
                hudCreatures, radarCoordinate)
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                copyOfCavebotManager['status'] = None
                return copyOfCavebotManager, copiedWalkpointsManager
            x, y = targetCreature['windowCoordinate']
            pyautogui.rightClick(x, y)
            time.sleep(0.05)
            copiedWalkpointsManager['lastCoordinateVisited'] = None
            copiedWalkpointsManager['lastCoordinateVisitedAt'] = None
            copiedWalkpointsManager['points'] = gameplay.waypoint.generateFloorWalkpoints(
                radarCoordinate, targetCreature['radarCoordinate'])
            copiedWalkpointsManager['points'] = copiedWalkpointsManager['points'][:-1]
            if copiedWalkpointsManager['lastPressedKey'] is not None:
                pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
                copiedWalkpointsManager['lastPressedKey'] = None
            return copyOfCavebotManager, copiedWalkpointsManager
        if len(copiedWalkpointsManager['points']) == 0:
            # print('radarCoordinate', radarCoordinate)
            # print('targetCreatureRadarCoordinate', targetCreature['radarCoordinate'])
            copiedWalkpointsManager['points'] = gameplay.waypoint.generateFloorWalkpoints(
                    radarCoordinate, targetCreature['radarCoordinate'])
    else:
        # print('status', copyOfCavebotManager['status'])
        # if copyOfCavebotManager['status'] == 'tryingToAttackTarget':
        # return copyOfCavebotManager, copiedWalkpointsManager
        # copiedWalkpointsManager['points'] = np.array([])
        # copyOfCavebotManager['status'] = 'tryingToAttackTarget'
        targetCreature = hud.creatures.getClosestCreature(
            hudCreatures, radarCoordinate)
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            return copyOfCavebotManager, copiedWalkpointsManager
        x, y = targetCreature['windowCoordinate']
        pyautogui.rightClick(x, y)
        time.sleep(0.05)
        copiedWalkpointsManager['lastCoordinateVisited'] = None
        copiedWalkpointsManager['lastCoordinateVisitedAt'] = None
        copiedWalkpointsManager['points'] = gameplay.waypoint.generateFloorWalkpoints(
            radarCoordinate, targetCreature['radarCoordinate'])
        copiedWalkpointsManager['points'] = copiedWalkpointsManager['points'][:-1]
        if copiedWalkpointsManager['lastPressedKey'] is not None:
            pyautogui.keyUp(copiedWalkpointsManager['lastPressedKey'])
            copiedWalkpointsManager['lastPressedKey'] = None
    # if copyOfCavebotManager['status'] != 'tryingToAttackTarget':
    # print('targetCreatureCoordinate', targetCreature['radarCoordinate'])
    # copiedWalkpointsManager['points'] = gameplay.waypoint.generateFloorWalkpoints(
    #     radarCoordinate, targetCreature['radarCoordinate'])
    return copyOfCavebotManager, copiedWalkpointsManager
