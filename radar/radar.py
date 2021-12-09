from PIL import Image
import cv2
import numpy as np
from numba import njit, jit
import pyautogui

images = {
    "radarTools": cv2.cvtColor(
        np.array(cv2.imread('radar/images/radar-tools.png')), cv2.COLOR_RGB2GRAY)
}
floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95,
                    0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]
floorsAreaImgs = [
    Image.open('radar/images/floor-0.png').convert('RGB'),
    Image.open('radar/images/floor-1.png').convert('RGB'),
    Image.open('radar/images/floor-2.png').convert('RGB'),
    Image.open('radar/images/floor-3.png').convert('RGB'),
    Image.open('radar/images/floor-4.png').convert('RGB'),
    Image.open('radar/images/floor-5.png').convert('RGB'),
    Image.open('radar/images/floor-6.png').convert('RGB'),
    Image.open('radar/images/floor-7.png').convert('RGB'),
    Image.open('radar/images/floor-8.png').convert('RGB'),
    Image.open('radar/images/floor-9.png').convert('RGB'),
    Image.open('radar/images/floor-10.png').convert('RGB'),
    Image.open('radar/images/floor-11.png').convert('RGB'),
    Image.open('radar/images/floor-12.png').convert('RGB'),
    Image.open('radar/images/floor-13.png').convert('RGB'),
    Image.open('radar/images/floor-14.png').convert('RGB'),
    Image.open('radar/images/floor-15.png').convert('RGB'),
]
floorsLevelImgs = [
    cv2.imread('radar/images/floor-level-0.png'),
    cv2.imread('radar/images/floor-level-1.png'),
    cv2.imread('radar/images/floor-level-2.png'),
    cv2.imread('radar/images/floor-level-3.png'),
    cv2.imread('radar/images/floor-level-4.png'),
    cv2.imread('radar/images/floor-level-5.png'),
    cv2.imread('radar/images/floor-level-6.png'),
    cv2.imread('radar/images/floor-level-7.png'),
    cv2.imread('radar/images/floor-level-8.png'),
    cv2.imread('radar/images/floor-level-9.png'),
    cv2.imread('radar/images/floor-level-10.png'),
    cv2.imread('radar/images/floor-level-11.png'),
    cv2.imread('radar/images/floor-level-12.png'),
    cv2.imread('radar/images/floor-level-13.png'),
    cv2.imread('radar/images/floor-level-14.png'),
    cv2.imread('radar/images/floor-level-15.png'),
]

floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsLevelImgsHashes = {}
toolsAreaWidth = 176

for floor in floors:
    floorImgArray = cv2.cvtColor(
        np.array(floorsLevelImgs[floor]), cv2.COLOR_RGB2GRAY)
    floorHash = hash(floorImgArray.tostring())
    floorsLevelImgsHashes[floorHash] = floor


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


def getFloorLevel(screenshot):
    """
     Avg FPS: 400+
    """
    left, top, width, height = getRadarToolsPos(screenshot)
    gapBetweenRadarToolsAndLevels = 8
    left = left + width + gapBetweenRadarToolsAndLevels
    # radar tools are a little lower than the radar level
    extraY = 7
    top = top - extraY
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = hash(floorLevelImg.tostring())
    hashNotExists = not floorImgHash in floorsLevelImgsHashes
    if hashNotExists:
        return None
    floorLevel = floorsLevelImgsHashes[floorImgHash]
    return floorLevel


def getRadarToolsPos(screenshot):
    """
     Avg FPS: 400+
    """
    screenshotWidth = len(screenshot[0])
    grayToolsArea = getRightContent(screenshot)
    res = cv2.matchTemplate(grayToolsArea, images['radarTools'], cv2.TM_CCOEFF)
    pos = cv2.minMaxLoc(res)[3]
    left = pos[0] + screenshotWidth - toolsAreaWidth
    top = pos[1]
    width = len(images['radarTools'][0])
    height = len(images['radarTools'])
    return (left, top, width, height)


def getRightContent(screenshot):
    '''
    Avg FPS: Unlimited
    '''
    screenshotWidth = len(screenshot[0])
    cropX0 = screenshotWidth - toolsAreaWidth
    cropX1 = screenshotWidth
    toolsArea = screenshot[:, cropX0:cropX1]
    return toolsArea


def getPos():
    # TODO: check previous tibia location. If didnt move, avoid this comparation
    radarBounds = pyautogui.locateOnScreen(
        'radar/images/compass.png', confidence=0.8)
    if radarBounds == None:
        return None
    gapBetweenRadarAndCompass = 11
    radarWidth = 106
    radarCenter = (
        radarBounds.left - radarWidth - gapBetweenRadarAndCompass,
        radarBounds.top
    )
    return radarCenter
