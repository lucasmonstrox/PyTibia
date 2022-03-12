from time import sleep
from battleList import battleList
from hud import hud
import numpy as np
from radar import radar
from utils import utils


def cavebotThread():
    while True:
        screenshot = utils.getScreenshot()
        currentPlayerCoordinate = radar.getCoordinate(screenshot)
        currentPlayerCoordinateIsEmpty = currentPlayerCoordinate is None
        if currentPlayerCoordinateIsEmpty:
            print('Cannot get coordinate')
            continue
        battleListCreatures = battleList.getCreatures(screenshot)
        cannotGetBattleList = battleListCreatures is None
        if cannotGetBattleList:
            print('Cannot get battle list creatures')
            continue
        hasNoBattleListCreatures = len(battleListCreatures) == 0
        if hasNoBattleListCreatures:
            print('hasNoBattleListCreatures')
            continue
        isAttackingAnyCreature = np.any(battleListCreatures['isBeingAttacked'] == True)
        if isAttackingAnyCreature:
            # TODO: check creature still reachable
            print('already attacking any creature 1')
            continue
        hudCreatures = hud.getCreatures(screenshot, battleListCreatures)
        hasNoHudCreatures = len(hudCreatures) == 0
        if hasNoHudCreatures:
            print('has no hud creatures')
            continue
        closestCreature = hud.getClosestCreature(hudCreatures, currentPlayerCoordinate, radar.walkableSqms)
        hasNoClosestCreature = closestCreature == None
        if hasNoClosestCreature:
            print('has no closest creature')
            continue
        hasOnlyCreature = len(hudCreatures) == 1
        if hasOnlyCreature:
            battleList.attackSlot(screenshot, 0)
        else:
            (x, y) = closestCreature['windowCoordinate']
            utils.rightClick(x, y)
        sleep(0.25)
