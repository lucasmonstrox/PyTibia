import cv2
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


def main():
    screenshot = utils.loadImgAsArray('screenshot.png')
    currentWaypointIndex = 0
    souldRetrySameWaypoint = True
    while True:
        screenshot = utils.getScreenshot()
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
            player.stop()
            hudImgFlattened = hudImg.flatten()
            creaturesBars = hud.getCreaturesBars(hudImgFlattened)
            hasHudCreaturesBars = len(creaturesBars) > 0
            if hasHudCreaturesBars:
                hudCreatures = hud.getCreatures(
                    hudImg, creaturesBars, battleListCreatures)
                hasHudCreatures = len(hudCreatures) > 0
                if hasHudCreatures:
                    print('going to attack creature')
                    hud.rightClickSlot(hudCreatures[0]["slot"], hudCoordinates)
                    sleep(2)
                    continue
                else:
                    print('There is no hud creatures')
            else:
                print('There is no hud creatures bars')
        floorLevel = radar.getFloorLevel(screenshot)
        radarToolsPos = radar.getRadarToolsPos(screenshot)
        radarImage = radar.getRadarImage(screenshot, radarToolsPos)
        coordinate = radar.getCoordinate(floorLevel, radarImage)
        coordinateIsEmpty = coordinate is None
        if coordinateIsEmpty:
            print('Cannot get coordinate')
            continue
        if radar.isNearToCoordinate(
                coordinate, waypoints[currentWaypointIndex]["coordinate"]):
            player.stop()
            currentWaypointIndex = 0 if currentWaypointIndex == len(
                waypoints) - 1 else currentWaypointIndex + 1
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue
        if souldRetrySameWaypoint:
            souldRetrySameWaypoint = False
            player.stop()
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue


if __name__ == '__main__':
    main()
