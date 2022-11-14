import numpy as np
import pathlib
import utils.core
import utils.image
import utils.core
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()
leftHudImg = utils.image.loadAsGrey(f'{currentPath}/images/leftHud.png')
rightHudImg = utils.image.loadAsGrey(f'{currentPath}/images/rightHud.png')
images = {
    720: {
        'holeOpen': utils.image.loadFromRGBToGray(f'{currentPath}/images/waypoint/holeOpen720.png')
    },
    1080: {
        'holeOpen': utils.image.loadFromRGBToGray(f'{currentPath}/images/waypoint/holeOpen1080.png')
    }
}
hudSizes = {
    720: (480, 352),
    1080: (960, 704)
}


def getCoordinate(screenshot, hudSize):
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


def getImgByCoordinate(screenshot, coordinates, hudSize):
    (hudWidth, hudHeight) = hudSize
    img = screenshot[coordinates[1]:coordinates[1] +
                     hudHeight, coordinates[0]:coordinates[0] + hudWidth]
    return img


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


def getSlotImg(hudImg, slot, slotWidth):
    xOfSlot, yOfSlot = slot
    x = xOfSlot * slotWidth
    y = yOfSlot * slotWidth
    slotImg = hudImg[y:y + slotWidth, x:x + slotWidth]
    return slotImg


def isHoleOpen(hudImg, holeOpenImg, coordinate, targetCoordinate):
    slotWidth = len(hudImg[1]) // 15
    slot = getSlotFromCoordinate(coordinate, targetCoordinate)
    slotImg = getSlotImg(hudImg, slot, slotWidth)
    holeOpenLocation = utils.core.locate(slotImg, holeOpenImg)
    isOpen = holeOpenLocation is not None
    return isOpen
