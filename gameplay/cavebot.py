import pyautogui
import time
import battleList.core
import gameplay.waypoint
import hud.creatures


# TODO: add unit tests
def handleCavebot(battleListCreatures, hudCreatures, radarCoordinate, walkpointsManager):
    copiedWalkpointsManager = walkpointsManager.copy()
    if battleList.core.isAttackingSomeCreature(battleListCreatures):
        targetCreature = hud.creatures.getTargetCreature(hudCreatures)
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            return copiedWalkpointsManager
        hasNoTargetToTargetCreature = hud.creatures.hasTargetToCreature(
            hudCreatures, targetCreature, radarCoordinate) == False
        if hasNoTargetToTargetCreature:
            targetCreature = hud.creatures.getClosestCreature(
                hudCreatures, radarCoordinate)
            hasNoTargetCreature = targetCreature == None
            if hasNoTargetCreature:
                return copiedWalkpointsManager
            x, y = targetCreature['windowCoordinate']
            pyautogui.rightClick(x, y)
            time.sleep(1)
    else:
        targetCreature = hud.creatures.getClosestCreature(
            hudCreatures, radarCoordinate)
        hasNoTargetCreature = targetCreature == None
        if hasNoTargetCreature:
            return copiedWalkpointsManager
        x, y = targetCreature['windowCoordinate']
        pyautogui.rightClick(x, y)
        time.sleep(1)
    copiedWalkpointsManager['points'] = gameplay.waypoint.generateFloorWalkpoints(
        radarCoordinate, targetCreature['radarCoordinate'])
    return copiedWalkpointsManager
