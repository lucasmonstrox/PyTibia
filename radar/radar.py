from PIL import Image
import numpy as np
import pyautogui

floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
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
floorsAsPixels = []

# loading all map pixels into numpy arrays in a 3D array
for floor in floors:
    img = Image.open('radar/images/floor-{}.png'.format(floor)).convert('RGB')
    pixelsColors = np.asarray(img)
    matrixOfMapPixelsColors = np.where(
        np.logical_not(
            np.isin(pixelsColors, forbiddenPixels).all(axis=2),
        ),
        1,
        1000
    )
    floorsAsBoolean.append(matrixOfMapPixelsColors)
    floorsAsPixels.append(pixelsColors)

def getCenter():
    radarBounds = pyautogui.locateOnScreen('radar/images/compass.png', confidence=0.8)
    if radarBounds == None:
        return None
    radarHalfSize = 54
    """
    117 is the distance between radar and compass
    2 & 1 is a extra to calculate correct radar center because player cross is not exactly in the middle
    """
    radarCenter = (
        radarBounds.left - 117 + radarHalfSize - 2,
        radarBounds.top + radarHalfSize - 1
    )
    return radarCenter

# save all floor level images into a hash and get current crop to compare with current hash to gain performance
def getFloorLevel():
    # using 7 first cuz is most probably the player is in ground floor
    for floor in [7, 6, 8, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
        pos = pyautogui.locateOnScreen('radar/images/floor-level-{}.png'.format(floor), confidence=0.9)
        isCurrentFloorLevel = pos != None
        if isCurrentFloorLevel:
            return floor
    return None