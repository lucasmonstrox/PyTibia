import numpy as np
import pathlib
import utils.core
import utils.image

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

# floorsImgs = np.load(f'{currentPath}/npys/floorsImgs.npy', allow_pickle=True)

floorsImgs = [
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-0.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-1.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-2.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-3.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-4.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-5.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-6.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-7.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-8.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-9.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-10.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-11.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-12.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-13.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-14.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/floor-15.png')),
]

floorsPathsImgs = [
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-0.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-1.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-2.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-3.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-4.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-5.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-6.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-7.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-8.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-9.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-10.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-11.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-12.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-13.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-14.png')),
    utils.image.RGBtoGray(utils.image.load(
        f'{currentPath}/images/paths/floor-15.png')),
]

floorsPathsSqms = np.load(f'{currentPath}/npys/floorsPathsSqms.npy')

images = {
    "tools": utils.image.loadAsGrey(f'{currentPath}/images/radar-tools.png')
}

floorsLevelsImgs = np.load(f'{currentPath}/npys/floorsLevelsImgs.npy')
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
walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in floors:
    floorHash = utils.core.hashit(floorsLevelsImgs[floor])
    floorsLevelsImgsHashes[floorHash] = floor
    walkableFloorSqms = np.where(
        np.isin(floorsPathsImgs[floor], [105, 226]), 0, 1)
    walkableFloorsSqms[floor] = walkableFloorSqms

# radarImagesCoordinates = np.load(f'{currentPath}/npys/radarImagesCoordinates.npy', allow_pickle=True)
# walkableFloorsSqms = np.load(f'{currentPath}/npys/walkableFloorsSqms.npy')
