import cv2
import numpy as np
from utils import utils
import pyautogui

config = {
    "radar": {
        "width": 106,
        "height": 109
    },
}
images = {
    "radarTools": utils.loadImgAsArray('radar/images/radar-tools.png')
}
floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95,
                    0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]
floorsAreaImgs = [
    utils.loadImgAsArray('radar/images/floor-0.png'),
    utils.loadImgAsArray('radar/images/floor-1.png'),
    utils.loadImgAsArray('radar/images/floor-2.png'),
    utils.loadImgAsArray('radar/images/floor-3.png'),
    utils.loadImgAsArray('radar/images/floor-4.png'),
    utils.loadImgAsArray('radar/images/floor-5.png'),
    utils.loadImgAsArray('radar/images/floor-6.png'),
    utils.loadImgAsArray('radar/images/floor-7.png'),
    utils.loadImgAsArray('radar/images/floor-8.png'),
    utils.loadImgAsArray('radar/images/floor-9.png'),
    utils.loadImgAsArray('radar/images/floor-10.png'),
    utils.loadImgAsArray('radar/images/floor-11.png'),
    utils.loadImgAsArray('radar/images/floor-12.png'),
    utils.loadImgAsArray('radar/images/floor-13.png'),
    utils.loadImgAsArray('radar/images/floor-14.png'),
    utils.loadImgAsArray('radar/images/floor-15.png')
]
floorsLevelImgs = [
    utils.loadImgAsArray('radar/images/floor-levels/0.png'),
    utils.loadImgAsArray('radar/images/floor-levels/1.png'),
    utils.loadImgAsArray('radar/images/floor-levels/2.png'),
    utils.loadImgAsArray('radar/images/floor-levels/3.png'),
    utils.loadImgAsArray('radar/images/floor-levels/4.png'),
    utils.loadImgAsArray('radar/images/floor-levels/5.png'),
    utils.loadImgAsArray('radar/images/floor-levels/6.png'),
    utils.loadImgAsArray('radar/images/floor-levels/7.png'),
    utils.loadImgAsArray('radar/images/floor-levels/8.png'),
    utils.loadImgAsArray('radar/images/floor-levels/9.png'),
    utils.loadImgAsArray('radar/images/floor-levels/10.png'),
    utils.loadImgAsArray('radar/images/floor-levels/11.png'),
    utils.loadImgAsArray('radar/images/floor-levels/12.png'),
    utils.loadImgAsArray('radar/images/floor-levels/13.png'),
    utils.loadImgAsArray('radar/images/floor-levels/14.png'),
    utils.loadImgAsArray('radar/images/floor-levels/15.png'),
]
floorsLevelImgsHashes = {}
toolsAreaWidth = 176

for floor in floors:
    floorHash = utils.hashit(floorsLevelImgs[floor])
    floorsLevelImgsHashes[floorHash] = floor


# floorsAsBoolean = []
caveWallPixelColor = 75
lavaPixelColor = 1
mountainOrStonePixelColor = 102
treeOrBushPixelColor = 59
vacummPixelColor = 0
wallPixelColor = 106
waterPixelColor = 92
forbiddenPixelsColors = [
    caveWallPixelColor,
    lavaPixelColor,
    mountainOrStonePixelColor,
    treeOrBushPixelColor,
    vacummPixelColor,
    wallPixelColor,
    waterPixelColor
]
floorAreaImg = floorsAreaImgs[7]
floorSevenImg = utils.loadImgAsArray('radar/images/floor-7.png')
floorSevenBooleans = np.where(
    np.isin(floorSevenImg, forbiddenPixelsColors),
    False,
    True
)
lastCoordinate = None


def getCoordinate(floorLevel, radarImage):
    coordinate = utils.locate(
        floorsAreaImgs[floorLevel], radarImage, confidence=0.75)
    cannotGetCoordinate = coordinate is None
    if cannotGetCoordinate:
        return None
    (xPixel, yPixel, _, _) = coordinate
    xCoordinate, yCoordinate = utils.getCoordinateFromPixel(
        (xPixel + 53, yPixel + 54))
    return (xCoordinate, yCoordinate, floorLevel)


def getCoordinate_perf(floorLevel, radarImage):
    global lastCoordinate
    image = floorsAreaImgs[floorLevel] if lastCoordinate is None else getQuadrantImg(
        lastCoordinate)
    match = cv2.matchTemplate(image, radarImage, cv2.TM_CCOEFF_NORMED)
    (_, confidence, _, (x, y)) = cv2.minMaxLoc(match)
    if confidence >= 0.7:
        lastCoordinate = (31744 + x + 53, 30976 + y + 54, floorLevel)
        return lastCoordinate
    match = cv2.matchTemplate(
        floorsAreaImgs[floorLevel], radarImage, cv2.TM_CCOEFF_NORMED)
    (_, _, _, (x, y)) = cv2.minMaxLoc(match)
    lastCoordinate = (31744 + x + 53, 30976 + y + 54, floorLevel)
    return lastCoordinate


def getFloorLevel(screenshot):
    radarToolsPos = getRadarToolsPos(screenshot)
    radarToolsPosIsEmpty = radarToolsPos is None
    if radarToolsPosIsEmpty:
        return None
    left, top, width, height = radarToolsPos
    left = left + width + 8
    top = top - 7
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = utils.hashit(floorLevelImg)
    hashNotExists = not floorImgHash in floorsLevelImgsHashes
    if hashNotExists:
        return None
    floorLevel = floorsLevelImgsHashes[floorImgHash]
    return floorLevel


def getQuadrantImg(lastCoordinate):
    (_, _, floorLevel) = lastCoordinate
    (x, y) = utils.getPixelFromCoordinate(lastCoordinate)
    floorAreaImg = floorsAreaImgs[floorLevel]
    radarHalfWidth = 53
    radarHalfHeight = 54
    if x < 1280:
        firstQuadrantImg = floorAreaImg[0:1024 + radarHalfHeight, 0:1280 +
                                        radarHalfWidth]
        thirdQuadrantImg = floorAreaImg[0:1024 + radarHalfHeight:2048, 1280 -
                                        radarHalfWidth:2560]
        return firstQuadrantImg if y < 1024 else thirdQuadrantImg
    secondQuadrantImg = floorAreaImg[1024 - radarHalfHeight:, 0:1280 +
                                     radarHalfWidth]
    fourthQuadrantImg = floorAreaImg[1024 - radarHalfHeight:, 1280 -
                                     radarHalfWidth:2560]
    return secondQuadrantImg if y < 1024 else fourthQuadrantImg


def getRadarImage(screenshot, radarToolsPos):
    radarToolsPosX = radarToolsPos[0]
    radarToolsPosY = radarToolsPos[1]
    x0 = radarToolsPosX - config['radar']['width'] - 11
    x1 = x0 + config['radar']['width']
    y0 = radarToolsPosY - 50
    y1 = y0 + config['radar']['height']
    radarImage = screenshot[y0:y1, x0:x1]
    return radarImage


@utils.cacheObjectPos
def getRadarToolsPos(screenshot):
    return utils.locate(screenshot, images['radarTools'])


def goToCoordinateByRadarClick(screenshot, playerCoordinate, coordinate):
    (radarToolsPosX, radarToolsPosY, _, _) = getRadarToolsPos(screenshot)
    x0 = radarToolsPosX - config['radar']['width'] - 11
    y0 = radarToolsPosY - 50
    radarCenterX = x0 + 53
    radarCenterY = y0 + 54
    (playerPixelCoordinateX, playerPixelCoordinateY) = utils.getPixelFromCoordinate(
        playerCoordinate)
    (destinationPixelCoordinateX,
     destinationPixelCoordinateY) = utils.getPixelFromCoordinate(coordinate)
    x = destinationPixelCoordinateX - playerPixelCoordinateX + radarCenterX
    y = destinationPixelCoordinateY - playerPixelCoordinateY + radarCenterY
    pyautogui.click(x, y)


def goToCoordinateByScreenClick(currentCoordinate, coordinate):
    playerCoordinateX, playerCoordinateY, playerCoordinateZ = currentCoordinate
    playerWindowCoordinateX, playerWindowCoordinateY = getPlayerWindowCoordinate()
    destinationX, destinationY, destinationZ = coordinate
    squareMeterSize = utils.getSquareMeterSize()
    # TODO: avoid battleye detection clicking in a random pixel inside squaremeter
    mouseClickX = playerWindowCoordinateX + \
        ((destinationX - playerCoordinateX) * squareMeterSize)
    # TODO: avoid battleye detection clicking in a random pixel inside squaremeter
    mouseClickY = playerWindowCoordinateY + \
        ((destinationY - playerCoordinateY) * squareMeterSize)
    # TODO: avoid battleye detection adding humanoid movementation
    pyautogui.click(mouseClickX, mouseClickY)


def isCoordinateWalkable(coordinate):
    (x, y) = utils.getPixelFromCoordinate(coordinate)
    walkable = floorSevenBooleans[y, x]
    return walkable


def isCoordinateVisible(currentCoordinate, targetCoordinate):
    return False


def isForbiddenPixelColor(pixelColor):
    return np.isin(pixelColor, forbiddenPixelsColors)


def isNearToCoordinate(coordinate, coordinateToCheck, tolerance=10):
    (x, y, _) = coordinate
    (xToCheck, yToCheck, _) = coordinateToCheck
    xDistance = abs(x - xToCheck)
    yDistance = abs(y - yToCheck)
    isNear = xDistance <= tolerance and yDistance <= tolerance
    return isNear
