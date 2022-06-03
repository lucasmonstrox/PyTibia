from time import sleep
from battleList import battleList
from hud import hud
from radar import radar
from utils import utils


def cavebotObserver(screenshot, currentPlayerCoordinate, battleListCreatures):
    hudCreatures = hud.getCreatures(screenshot, battleListCreatures)
    hasNoHudCreatures = len(hudCreatures) == 0
    if hasNoHudCreatures:
        print('has no hud creatures')
        return
    closestCreature = hud.getClosestCreature(hudCreatures, currentPlayerCoordinate, radar.walkableSqms)
    hasNoClosestCreature = closestCreature == None
    if hasNoClosestCreature:
        print('has no closest creature')
        return
    hasOnlyCreature = len(hudCreatures) == 1
    if hasOnlyCreature:
        battleList.attackSlot(screenshot, 0)
    else:
        (x, y) = closestCreature['windowCoordinate']
        utils.rightClick(x, y)
    sleep(0.25)
