import cv2
import numpy as np
import pyautogui
from time import sleep
from battleList import battleList
from hud import hud
from player import player
from radar import radar
from utils import utils
from skimage.graph import route_through_array


def getHudSlotFromCoordinate(currentCoordinate, coordinate):
    diffX = coordinate[0] - currentCoordinate[0]
    diffXAbs = abs(diffX)
    if diffXAbs > 7:
        # TODO: throw an exception
        print('diffXAbs > 7')
        return None
    diffY = coordinate[1] - currentCoordinate[1]
    diffYAbs = abs(diffY)
    if diffYAbs > 5:
        # TODO: throw an exception
        print('diffYAbs > 5')
        return None
    hudCoordinateX = 7 + diffX
    hudCoordinateY = 5 + diffY
    return (hudCoordinateX, hudCoordinateY)


waypoints = [
    {"coordinate": (33004, 32772, 7)},
    {"coordinate": (32981, 32795, 7)},
    {"coordinate": (32962, 32814, 7)},
    {"coordinate": (32996, 32805, 7)},
    {"coordinate": (33005, 32783, 7)},
]


def main():
    screenshot = np.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE))
    # isMoving = False
    currentWaypointIndex = 0
    souldRetrySameWaypoint = True
    while True:
        screenshot = utils.getScreenshot()
        # hudCoordinates = hud.getCoordinates(screenshot)
        # hudImg = hud.getImgByCoordinates(screenshot, hudCoordinates)
        # emptyHud = hudImg is None
        # if emptyHud:
        #     print('Cannot find hud')
        #     continue
        battleListCreatures = battleList.getCreatures(screenshot)
        cannotGetBattleList = battleListCreatures is None
        if cannotGetBattleList:
            print('Cannot get battle list creatures')
            continue
        hasBattleListCreatures = len(battleListCreatures["creatures"]) > 0
        print('hasBattleListCreatures', hasBattleListCreatures)
        print(battleListCreatures)
        # hudWalkableCreatures = np.zeros(165, dtype=np.uint8).reshape(11, 15)
        if hasBattleListCreatures:
            souldRetrySameWaypoint = True
            # hudImgFlattened = hudImg.flatten()
            # creaturesBars = hud.getCreaturesBars(hudImgFlattened)
            # hasHudCreaturesBars = len(creaturesBars) > 0
            # if hasHudCreaturesBars:
            #     hudCreatures = hud.getCreatures(
            #         hudImg, creaturesBars, battleListCreatures)
            #     hasHudCreatures = len(hudCreatures) > 0
            # if hasHudCreatures:
            # for creature in hudCreatures:
            #     hudWalkableCreatures[creature["slot"]
            #                          [1], creature["slot"][0]] = 1
            if battleListCreatures["isAttackingAnyCreature"]:
                print('already attacking any creature 1')
                continue
            print('going to attack creature')
            player.stop()
            battleList.attackSlot(screenshot, 0)
            continue
            # else:
            #     print('There is no hud creatures')
            # else:
            #     print('There is no hud creatures bars')
        else:
            floorLevel = radar.getFloorLevel(screenshot)
            radarToolsPos = radar.getRadarToolsPos(screenshot)
            radarImage = radar.getRadarImage(screenshot, radarToolsPos)
            coordinate = radar.getCoordinate(floorLevel, radarImage)
            coordinateIsEmpty = coordinate is None
            if coordinateIsEmpty:
                print('Cannot get coordinate')
                continue
            # (x, y) = utils.getPixelFromCoordinate(coordinate)
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
            # hudWalkable = radar.floorSevenBooleans[y-5:y+6, x-7:x+8]
            # hudWalkable[5, 7] = 1
            # hudWalkable = np.add(hudWalkable, hudWalkableCreatures)
            # if currentWaypointIndex == len(waypoints) - 1:
            #     currentWaypointIndex = 0
            #     if isMoving:
            #         differentCoordinates = waypoints[currentWaypointIndex] != coordinate
            #         if differentCoordinates:
            #             isMoving = False
            # else:
            #     if coordinate == waypoints[currentWaypointIndex]["coordinate"]:
            #         currentWaypointIndex = currentWaypointIndex + 1
            # targetHudCoordinate = getHudSlotFromCoordinate(
            #     coordinate, waypoints[currentWaypointIndex]["coordinate"])
            # costs = np.where(hudWalkable, 10, 1)
            # indices, _ = route_through_array(
            #     costs, [5, 7], [targetHudCoordinate[1], targetHudCoordinate[0]], fully_connected=False)
            # if len(indices) < 2:
            #     continue
            # shouldGoUp = indices[0][0] > indices[1][0]
            # if shouldGoUp:
            #     pyautogui.press('up')
            #     isMoving = True
            #     continue
            # shouldGoDown = indices[0][0] < indices[1][0]
            # if shouldGoDown:
            #     pyautogui.press('down')
            #     isMoving = True
            #     continue
            # shouldGoLeft = indices[0][1] > indices[1][1]
            # if shouldGoLeft:
            #     pyautogui.press('left')
            #     isMoving = True
            #     continue
            # shouldGoRight = indices[0][1] < indices[1][1]
            # if shouldGoRight:
            #     pyautogui.press('right')
            #     isMoving = True
            #     continue
            # print(path)
            # sqmSize = 32
            # closestCreature = None
            # closestCreaturePath = None
            # for creature in creatures:
            #     creatureHudX = creature["x"] // sqmSize
            #     creatureHudY = creature["y"] // sqmSize
            #     hudWalkable[creatureHudY, creatureHudX] = 1
            #     creaturePath = route_through_array(hudWalkable, [7, 5], [
            #         creatureHudY, creatureHudX], fully_connected=False)
            #     if closestCreature is None:
            #         closestCreature = creature
            #         closestCreaturePath = creaturePath
            #         continue
            #     if len(creaturePath) < len(closestCreaturePath):
            #         closestCreature = creature
            #         closestCreaturePath = creaturePath


if __name__ == '__main__':
    main()
