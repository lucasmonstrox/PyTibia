import numpy as np
import utils.core
import utils.image
import utils.core
import utils.image


leftHudImg = utils.image.loadAsGrey('hud/images/leftHud.png')
rightHudImg = utils.image.loadAsGrey('hud/images/rightHud.png')
hudSize = (960, 704)


# TODO: cache it
def getCoordinate(screenshot):
    global hudSize
    leftSidebarArrows = getLeftSidebarArrows(screenshot)
    cannotGetLeftSidebarArrows = leftSidebarArrows is None
    if cannotGetLeftSidebarArrows:
        return None
    rightSidebarArrows = getRightSidebarArrows(screenshot)
    cannotGetRightSidebarArrows = rightSidebarArrows is None
    if cannotGetRightSidebarArrows:
        return None
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
        return None
    diffY = coordinate[1] - currentCoordinate[1]
    diffYAbs = abs(diffY)
    if diffYAbs > 5:
        return None
    hudCoordinateX = 7 + diffX
    hudCoordinateY = 5 + diffY
    return hudCoordinateX, hudCoordinateY


# TODO: add unit tests
def getSlotImg(hudImg, slot):
    xOfSlot, yOfSlot = slot
    slotWidth = 64
    x = xOfSlot * slotWidth
    y = yOfSlot * slotWidth
    slotImg = hudImg[y:y+slotWidth, x:x+slotWidth]
    return slotImg


# TODO: add unit tests
def isHoleOpen(hudImg, coordinate, targetCoordinate):
    slot = getSlotFromCoordinate(coordinate, targetCoordinate)
    slotImg = getSlotImg(hudImg, slot)
    holeOpenImg = utils.image.RGBtoGray(
        utils.image.load('hud/images/waypoint/holeOpenImg.png'))
    holeOpenLocation = utils.core.locate(slotImg, holeOpenImg)
    isOpen = holeOpenLocation is not None
    return isOpen
