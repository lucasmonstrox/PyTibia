from numba import cuda, jit
import hashlib
from functools import lru_cache
from PIL import Image, ImageGrab
import cv2
import numpy as np
import pyautogui
from utils import utils

floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95,
                    0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]
floorsAreaImgs = [
    np.array(Image.open('radar/images/floor-0.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-1.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-2.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-3.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-4.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-5.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-6.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-7.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-8.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-9.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-10.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-11.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-12.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-13.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-14.png').convert('RGB')),
    np.array(Image.open('radar/images/floor-15.png').convert('RGB')),
]
floorsLevelImgs = [
    Image.open('radar/images/floor-level-0.png').convert('RGB'),
    Image.open('radar/images/floor-level-1.png').convert('RGB'),
    Image.open('radar/images/floor-level-2.png').convert('RGB'),
    Image.open('radar/images/floor-level-3.png').convert('RGB'),
    Image.open('radar/images/floor-level-4.png').convert('RGB'),
    Image.open('radar/images/floor-level-5.png').convert('RGB'),
    Image.open('radar/images/floor-level-6.png').convert('RGB'),
    Image.open('radar/images/floor-level-7.png').convert('RGB'),
    Image.open('radar/images/floor-level-8.png').convert('RGB'),
    Image.open('radar/images/floor-level-9.png').convert('RGB'),
    Image.open('radar/images/floor-level-10.png').convert('RGB'),
    Image.open('radar/images/floor-level-11.png').convert('RGB'),
    Image.open('radar/images/floor-level-12.png').convert('RGB'),
    Image.open('radar/images/floor-level-13.png').convert('RGB'),
    Image.open('radar/images/floor-level-14.png').convert('RGB'),
    Image.open('radar/images/floor-level-15.png').convert('RGB'),
]
floorsLevelImgsHashes = {}

for floor in floors:
    floorImgArray = np.array(floorsLevelImgs[floor])
    floorHash = hash(str(floorImgArray))
    floorsLevelImgsHashes[floorHash] = floor

coordinatesHashes = {}
radarHeight = 109
radarWidth = 106
radarHalfWidth = int(radarWidth / 2) - 1
radarHeightHalf = int(radarHeight / 2)
floorImg = np.array(Image.open('radar/images/floor-7.png').convert('RGB'))
firstX = radarHalfWidth
lastX = 34303 - 31744 - radarWidth
firstY = radarHeightHalf
lastY = 33023 - 30976 - radarHeight

firstX = 33054 - 31744
lastX = 33254 - 31744
firstY = 32758 - 30976
lastY = 32895 - 30976

# for yPixel in range(firstY, lastY):
#     for xPixel in range(firstX, lastX):
#         coordinateImg = floorImg[yPixel - radarHeightHalf:yPixel +
#                                  radarHeightHalf, xPixel - radarHalfWidth:xPixel + radarHalfWidth].copy()
#         # quadrado de cima
#         coordinateImg[52][53] = [255, 255, 255]
#         coordinateImg[52][54] = [255, 255, 255]
#         coordinateImg[53][53] = [255, 255, 255]
#         coordinateImg[53][54] = [255, 255, 255]
#         # quadrado da esquerda
#         coordinateImg[54][51] = [255, 255, 255]
#         coordinateImg[54][52] = [255, 255, 255]
#         coordinateImg[55][51] = [255, 255, 255]
#         coordinateImg[55][52] = [255, 255, 255]
#         # quadrado do centro
#         coordinateImg[54][53] = [255, 255, 255]
#         coordinateImg[54][54] = [255, 255, 255]
#         coordinateImg[55][53] = [255, 255, 255]
#         coordinateImg[55][54] = [255, 255, 255]
#         # quadrado da direita
#         coordinateImg[54][55] = [255, 255, 255]
#         coordinateImg[54][56] = [255, 255, 255]
#         coordinateImg[55][55] = [255, 255, 255]
#         coordinateImg[55][56] = [255, 255, 255]
#         # quadrado de baixo
#         coordinateImg[56][53] = [255, 255, 255]
#         coordinateImg[56][54] = [255, 255, 255]
#         coordinateImg[57][53] = [255, 255, 255]
#         coordinateImg[57][54] = [255, 255, 255]
#         coordinateHash = hashlib.md5(
#             np.array(coordinateImg).tostring()).hexdigest()
#         coordinate = (xPixel + 31744, yPixel + 30976, 7)
#         (x, y, z) = coordinate
#         im = Image.fromarray(coordinateImg)
#         im.save(
#             f'radar/images/coordinates/{x}-{y}-{z}.png'.format(x, y, z))
#         coordinateX, coordinateY, coordinateZ = coordinate
#         coordinatesHashes[coordinateHash] = coordinate
#         print(x, y, z)
# print(hashlib.md5(np.array([255, 255, 255]).tostring()).hexdigest())
# print(hashlib.md5(np.array([255, 255, 254]).tostring()).hexdigest())
# print(hashlib.md5(np.array([255, 255, 255]).tostring()).hexdigest())
# hashlib.md5(bytes([255, 255, 255])).hexdigest())
# hashlib.md5([255, 255, 254].tostring().encode())
# hashlib.md5([255, 255, 255].tostring().encode())
# print(hash(bytes([255, 255, 255])))
# print(hash(bytes([255, 255, 254])))
# print(hash(bytes([255, 255, 255])))

darkPixelColor = [0, 0, 0]
pyramidEdgeColor = [255, 255, 0]
stonePixelColor = [102, 102, 102]
treePixelColor = [0, 102, 0]
waterPixelColor = [51, 102, 153]
wallPixelColor = [255, 51, 0]
forbiddenPixels = [
    darkPixelColor,
    pyramidEdgeColor,
    stonePixelColor,
    treePixelColor,
    wallPixelColor,
    waterPixelColor
]
floorsAsBoolean = []

# loading all map pixels into numpy arrays in a 3D array
for floor in floors:
    floorAreaImg = floorsAreaImgs[floor]
    pixelsColors = np.asarray(floorAreaImg)
    matrixOfMapPixelsColors = np.where(
        np.isin(pixelsColors, forbiddenPixels, invert=True).any(axis=2),
        1,
        1000
    )
    floorsAsBoolean.append(matrixOfMapPixelsColors)


def getCenterBounds():
    # TODO: check previous tibia location. If didnt move, avoid this comparation
    radarBounds = pyautogui.locateOnScreen(
        'radar/images/compass.png', confidence=0.8)
    if radarBounds == None:
        return None
    """
    radar width is 106
    distance between radar and compass is 11
    117 is the distance of radar width + radar area and compass
    53 is the half width of radar area
    2 is a extra to calculate correct radar center because player cross is not exactly in the middle
    """
    gapBetweenRadarAndCompass = 11
    radarWidth = 106
    radarHorizontalHalfSize = 53
    # True value is 54.5 since radar height is 109
    radarVerticalHalfSize = 54
    radarCenter = (
        radarBounds.left - radarWidth - gapBetweenRadarAndCompass + radarHorizontalHalfSize,
        radarBounds.top + radarVerticalHalfSize
    )
    return radarCenter


# TODO: find by zone(cities, hunts, etc)
# TODO: find through whole map when bounds not found(looks like user is changing zone)
def getCoordinate(screenshot):
    radarWidth = 106
    radarHeight = 109
    radarPos = getPos(screenshot)
    if not radarPos:
        # TODO: throw a custom exception
        return None
    radarPosX, radarPosY = radarPos
    floorLevel = getFloorLevel(screenshot)
    radarScreenshot = screenshot[radarPosY:radarPosY +
                                 radarHeight, radarPosX: radarPosX + radarWidth]
    firstX = 33035 - 31744
    firstY = 32733 - 30976
    lastX = 33309 - 31744
    lastY = 32912 - 30976
    img = floorsAreaImgs[floorLevel]
    img = img[firstY:lastY, firstX:lastX]
    currentPositionBounds = pyautogui.locate(
        radarScreenshot,
        img,
        confidence=floorsConfidence[floorLevel]
    )
    playerXPixel = currentPositionBounds.left + 53 + firstX
    playerYPixel = currentPositionBounds.top + 54 + firstY
    playerCoordinateX, playerCoordinateY = utils.getCoordinateFromPixel(
        (playerYPixel, playerXPixel))
    playerCoordinate = (playerCoordinateX, playerCoordinateY, floorLevel)
    return playerCoordinate


# radarToolsImg = cv2.imread('radar/images/radar-tools.png')
radarToolsImg = cv2.cvtColor(
    np.array(cv2.imread('radar/images/radar-tools.png')), cv2.COLOR_RGB2GRAY)
radarCompassImg = np.array(cv2.imread('radar/images/compass.png'))
cache = {}


def getToolsScreenshotArea(screenshot):
    screenshotWidth = len(screenshot[0])
    toolsScreenshotArea = screenshot[:, screenshotWidth - 177:screenshotWidth]
    return toolsScreenshotArea


def getRadarToolsPos(screenshot):
    """
    FPS: 225
    """
    screenshotWidth = len(screenshot[0])
    toolsArea = getToolsScreenshotArea(screenshot)
    grayToolsArea = cv2.cvtColor(toolsArea, cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(grayToolsArea, radarToolsImg, cv2.TM_CCOEFF_NORMED)
    pos = cv2.minMaxLoc(res)[3]
    x = pos[0] + screenshotWidth - 177
    y = pos[1]
    return (x, y)


def getFloorLevel(screenshot):
    screenshotLen = len(screenshot[0])
    # TODO: WTF???
    screenshot = screenshot[:, screenshotLen-50:screenshotLen]
    left, top, width, height = getRadarToolsPos(screenshot)
    gapBetweenRadarToolsAndLevels = 8
    left = left + width + gapBetweenRadarToolsAndLevels
    # radar tools are a little lower than the radar level
    extraY = 7
    top = top - extraY
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = hash(str(floorLevelImg))
    hashNotExists = not floorImgHash in floorsLevelImgsHashes
    if hashNotExists:
        return None
    floorLevel = floorsLevelImgsHashes[floorImgHash]
    return floorLevel


def getPos(screenshot):
    screenshotWidth = len(screenshot[0])
    screenshotHeight = len(screenshot)
    # TODO: WTF???
    screenshot = screenshot[:, screenshotWidth-176:screenshotWidth]
    left, top, width, height = utils.locate(radarCompassImg, screenshot)
    gapBetweenRadarAndCompass = 11
    radarWidth = 106
    radarCenter = (
        screenshotWidth - 176 + left - radarWidth - gapBetweenRadarAndCompass,
        top
    )
    return radarCenter
