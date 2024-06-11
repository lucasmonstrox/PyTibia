import numpy as np
import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
coordinates = {}
dimensions = {
    'width': 106,
    'height': 109,
    'halfWidth': 53,
    'halfHeight': 54,
}
floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95,
                    0.95, 0.85, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]
floorsImgs = [
    loadFromRGBToGray(
        f'{currentPath}/images/floor-0.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-1.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-2.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-3.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-4.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-5.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-6.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-7.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-8.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-9.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-10.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-11.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-12.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-13.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-14.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floor-15.png'),
]
floorsPathsImgs = [
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-0.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-1.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-2.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-3.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-4.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-5.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-6.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-7.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-8.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-9.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-10.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-11.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-12.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-13.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-14.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/paths/floor-15.png'),
]
floorsPathsSqms = np.load(f'{currentPath}/npys/floorsPathsSqms.npy')
images = {
    'tools': loadFromRGBToGray(f'{currentPath}/images/buttons/radarTools.png')
}
floorsLevelsImgs = [
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/0.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/1.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/2.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/3.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/4.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/5.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/6.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/7.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/8.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/9.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/10.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/11.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/12.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/13.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/14.png'),
    loadFromRGBToGray(
        f'{currentPath}/images/floorLevels/15.png'),
]
floorsLevelsImgsHashes = {}
pixelsColorsValues = {
    'accessPoint': 226,
    'caveFloor': 111,
    'caveWall': 76,
    'commonFloorOrStreet': 1,
    'grassOrRockyGround': 120,
    'ice': 240,
    'lava': 136,
    'mountainOrStone': 102,
    'sand': 213,
    'snow': 255,
    'swamp': 207,
    'treesOrBushes': 60,
    'wall': 106,
    'water': 93,
    'vacuumOrUndiscoveredArea': 0
}
nonWalkablePixelsColors = [
    pixelsColorsValues['caveWall'],
    pixelsColorsValues['lava'],
    pixelsColorsValues['mountainOrStone'],
    pixelsColorsValues['swamp'],
    pixelsColorsValues['treesOrBushes'],
    pixelsColorsValues['wall'],
    pixelsColorsValues['water'],
    pixelsColorsValues['vacuumOrUndiscoveredArea'],
]
walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint8)
availableTilesFrictions = np.array(
    [70, 90, 95, 100, 110, 125, 140, 150, 160, 200, 250])
breakpointTileMovementSpeed = {
    1: 850,
    2: 800,
    3: 750,
    4: 700,
    5: 650,
    6: 600,
    7: 550,
    8: 500,
    9: 450,
    10: 400,
    11: 350,
    12: 300,
    13: 250,
    14: 200,
    15: 150,
    16: 100,
    17: 50,
}
tilesFrictionsWithBreakpoints = {
    70:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 142, 200, 342, 1070]),
    90:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 147, 192, 278, 499, 1842]),
    95:  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 157, 205, 299, 543, 2096]),
    100: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 113, 135, 167, 219, 321, 592, 2382]),
    110: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 150, 187, 248, 367, 696, 3060]),
    125: np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 175, 219, 293, 444, 876, 4419]),
    140: np.array([0, 0, 0, 0, 0, 0, 0, 111, 125, 143, 167, 201, 254, 344, 531, 1092, 6341]),
    150: np.array([0, 0, 0, 0, 0, 0, 0, 120, 135, 155, 181, 219, 278, 380, 595, 1258, 8036]),
    160: np.array([0, 0, 0, 0, 0, 0, 116, 129, 145, 167, 196, 238, 304, 419, 663, 1443, 10167]),
    200: np.array([0, 0, 0, 114, 124, 135, 149, 167, 190, 219, 261, 322, 419, 597, 998, 2444, 25761]),
    250: np.array([117, 126, 135, 146, 160, 175, 195, 220, 252, 295, 356, 446, 598, 884, 1591, 4557, 81351]),
}

for floor in floors:
    floorHash = hashit(floorsLevelsImgs[floor])
    floorsLevelsImgsHashes[floorHash] = floor
    walkableFloorsSqms[floor] = np.where(
        np.isin(floorsPathsImgs[floor], [105, 226]), 0, 1)
