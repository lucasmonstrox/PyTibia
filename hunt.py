from time import sleep
from battleList import battleList
from hud import hud
from player import player
from radar import radar
from utils import utils
import pyautogui


waypoints = [
    {"coordinate": (33004, 32772, 7)},
    {"coordinate": (32981, 32795, 7)},
    {"coordinate": (32962, 32814, 7)},
    {"coordinate": (32996, 32805, 7)},
    {"coordinate": (33005, 32783, 7)},
]


def main():
    currentWaypointIndex = 0
    souldRetrySameWaypoint = True
    while True:
        screenshot = utils.getScreenshot()
        coordinate = radar.getCoordinate(screenshot)
        coordinateIsEmpty = coordinate is None
        if coordinateIsEmpty:
            print('Cannot get coordinate')
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
            hudCreatures = hud.getCreatures(screenshot, battleListCreatures)
            hasHudCreatures = len(hudCreatures) > 0
            if hasHudCreatures:
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
        if radar.isNearToCoordinate(
                coordinate, waypoints[currentWaypointIndex]["coordinate"]):
            souldRetrySameWaypoint = False
            print('checking waypoint', waypoints[currentWaypointIndex]["coordinate"])
            player.stop()
            currentWaypointIndex = 0 if currentWaypointIndex == len(
                waypoints) - 1 else currentWaypointIndex + 1
            print('going to waypoint', waypoints[currentWaypointIndex]["coordinate"])
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue
        if souldRetrySameWaypoint:
            print('Retrying same waypoint', waypoints[currentWaypointIndex]["coordinate"])
            souldRetrySameWaypoint = False
            player.stop()
            radar.goToCoordinateByRadarClick(
                screenshot, coordinate, waypoints[currentWaypointIndex]["coordinate"])
            continue


if __name__ == '__main__':
    main()
