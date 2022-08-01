import numpy as np
import utils.core, utils.image
import utils.core
import utils.image

leftHudImg = utils.image.loadAsArray('hud/images/leftHud.png')
rightHudImg = utils.image.loadAsArray('hud/images/rightHud.png')
hudSize = (480, 352)


# TODO: cache it
def getCoordinate(screenshot):
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    rightSidebarArrows = getRightSidebarArrows(screenshot)
    global hudSize
    (hudWidth, hudHeight) = hudSize
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
        bbox = (x, y, hudWidth, hudHeight)
        return bbox


def getImgByCoordinate(screenshot, coordinates):
    global hudSize
    (hudWidth, hudHeight) = hudSize
    return screenshot[coordinates[1]:coordinates[1] +
                      hudHeight, coordinates[0]:coordinates[0] + hudWidth]


@utils.core.cacheObjectPos
def getLeftSidebarArrows(screenshot):
    return utils.core.locate(screenshot, leftHudImg)


@utils.core.cacheObjectPos
def getRightSidebarArrows(screenshot):
    return utils.core.locate(screenshot, rightHudImg)


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
    return hudCoordinateX, hudCoordinateY


