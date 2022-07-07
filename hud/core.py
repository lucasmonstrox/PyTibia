import numpy as np
from utils import utils


hudWidth = 480
leftHudImg = utils.loadImgAsArray('hud/images/leftHud.png')
rightHudImg = utils.loadImgAsArray('hud/images/rightHud.png')
hudSize = (480, 352)


# TODO: cache it
def getCoordinates(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    rightSidebarArrows = getRightSidebarArrows(screenshot)
    (hudWidth, hudHeight) = (480, 352)
    hudCenter = (
        (rightSidebarArrows[0] - leftSidebarArrows[0]) // 2) + leftSidebarArrows[0]
    hudLeftPos = hudCenter - (hudWidth // 2) - 1
    hud = screenshot[leftSidebarArrows[1] + 5: leftSidebarArrows[1] +
                     5 + hudHeight, hudLeftPos:hudLeftPos + 1]
    hud = np.where(np.logical_and(hud >= 18, hud <= 30), 1, 0)
    isHudDetected = np.all(hud == 1)
    if isHudDetected:
        x = hudLeftPos + 1
        y = leftSidebarArrows[1] + 5
        bbox = (x, y, 480, 352)
        return bbox


def getImgByCoordinates(screenshot, coordinates):
    return screenshot[coordinates[1]:coordinates[1] +
                      352, coordinates[0]:coordinates[0] + 480]


@utils.cacheObjectPos
def getLeftSidebarArrows(screenshot):
    return utils.locate(screenshot, leftHudImg)


@utils.cacheObjectPos
def getRightSidebarArrows(screenshot):
    return utils.locate(screenshot, rightHudImg)


def getSlotFromCoordinate(currentCoordinate, coordinate):
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