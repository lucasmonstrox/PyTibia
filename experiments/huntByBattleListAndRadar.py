import cv2
import numpy as np
from battleList import battleList
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
    screenshot = np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE))
    currentWaypointIndex = 0
    souldRetrySameWaypoint = True
    while True:
        screenshot = utils.getScreenshot()
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
            print('going to attack creature')
            player.stop()
            battleList.attackSlot(screenshot, 0)
            continue
        else:
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
