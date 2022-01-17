import numpy as np
from time import sleep
from battleList import battleList
from hud import hud
from player import player
from radar import radar
from utils import utils


waypoints = [
    {"coordinate": (33004, 32772, 7)},
    {"coordinate": (32981, 32795, 7)},
    {"coordinate": (32962, 32814, 7)},
    {"coordinate": (32996, 32805, 7)},
    {"coordinate": (33005, 32783, 7)},
]


def getTemporaryCoordinate(screenshot):
    floorLevel = radar.getFloorLevel(screenshot)
    radarToolsPos = radar.getRadarToolsPos(screenshot)
    radarImage = radar.getRadarImage(screenshot, radarToolsPos)
    coordinate = radar.getCoordinate(floorLevel, radarImage)
    return coordinate


def main():
    currentWaypointIndex = 0
    souldRetrySameWaypoint = True
    while True:
        screenshot = utils.getScreenshot()
        coordinate = getTemporaryCoordinate(screenshot)
        coordinateIsEmpty = coordinate is None
        if coordinateIsEmpty:
            print('Cannot get coordinate')
            continue
        hudCoordinates = hud.getCoordinates(screenshot)
        hudImg = hud.getImgByCoordinates(screenshot, hudCoordinates)
        emptyHud = hudImg is None
        if emptyHud:
            print('Cannot find hud')
            continue
        battleListCreatures = battleList.getCreatures(screenshot)
        cannotGetBattleList = battleListCreatures is None
        if cannotGetBattleList:
            print('Cannot get battle list creatures')
            continue
        hasBattleListCreatures = len(battleListCreatures["creatures"]) > 0
        if hasBattleListCreatures:
            souldRetrySameWaypoint = True
            if battleListCreatures["isAttackingAnyCreature"]:
                print('already attacking any creature 1')
                continue
            hudImgFlattened = hudImg.flatten()
            creaturesBars = hud.getCreaturesBars(hudImgFlattened)
            hasHudCreaturesBars = len(creaturesBars) > 0
            if hasHudCreaturesBars:
                hudCreatures = hud.getCreatures(
                    hudImg, creaturesBars, battleListCreatures)
                hasHudCreatures = len(hudCreatures) > 0
                if hasHudCreatures:
                    shortestCreatureIndex = hud.getClosestCreatures(hudCreatures)
                    if shortestCreatureIndex is not None:
                        x = shortestCreatureIndex % 15
                        y = shortestCreatureIndex // 15
                        player.stop(1)
                        screenshot = utils.getScreenshot()
                        temporaryCoordinate = getTemporaryCoordinate(screenshot)
                        if coordinate != temporaryCoordinate:
                            xDifference = coordinate[0] - temporaryCoordinate[0]
                            yDifference = coordinate[1] - temporaryCoordinate[1]
                            x += xDifference
                            y += yDifference
                        hud.rightClickSlot((x, y), hudCoordinates)
                        sleep(1)
                        continue
                else:
                    print('There is no hud creatures')
            else:
                print('There is no hud creatures bars')
        if radar.isNearToCoordinate(
                coordinate, waypoints[currentWaypointIndex]["coordinate"]):
            player.stop(1)
            currentWaypointIndex = 0 if currentWaypointIndex == len(
                waypoints) - 1 else currentWaypointIndex + 1
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue
        if souldRetrySameWaypoint:
            souldRetrySameWaypoint = False
            player.stop(1)
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue


if __name__ == '__main__':
    main()
