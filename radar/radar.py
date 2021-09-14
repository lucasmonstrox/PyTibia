from PIL import Image
import numpy as np
import pyautogui

floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]
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
    floorHash = hash(floorImgArray.tostring())
    floorsLevelImgsHashes[floorHash] = floor

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
    floorsAsBoolean.append(pixelsColors)

def getCenterBounds():
     # TODO: check previous tibia location. If didnt move, avoid this comparation
    radarBounds = pyautogui.locateOnScreen('radar/images/compass.png', confidence=0.8)
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

def getFloorLevel():
    # TODO: check previous tibia location. If didnt move, avoid this comparison
    pos = pyautogui.locateOnScreen('radar/images/radar-tools.png', confidence=0.85)
    if pos == None:
        return None
    gapBetweenRadarToolsAndLevels = 8
    left = pos.left + pos.width + gapBetweenRadarToolsAndLevels
    # radar tools are a little lower than the radar level
    extraY = 7
    top = pos.top - extraY
    height = 67
    width = 2
    floorLevelImg = pyautogui.screenshot(region=(left, top, width, height))
    if floorLevelImg == None:
        return None
    floorLevelImg = np.array(floorLevelImg)
    floorImgHash = hash(floorLevelImg.tostring())
    hashNotExists = not floorImgHash in floorsLevelImgsHashes
    if hashNotExists:
        return None
    floorLevel = floorsLevelImgsHashes[floorImgHash]
    return floorLevel

def getPos():
     # TODO: check previous tibia location. If didnt move, avoid this comparation
    radarBounds = pyautogui.locateOnScreen('radar/images/compass.png', confidence=0.8)
    if radarBounds == None:
        return None
    gapBetweenRadarAndCompass = 11
    radarWidth = 106
    radarCenter = (
        radarBounds.left - radarWidth - gapBetweenRadarAndCompass,
        radarBounds.top
    )
    return radarCenter