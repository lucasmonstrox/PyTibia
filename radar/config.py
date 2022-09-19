import numpy as np
import utils.core
import utils.image

coordinates = {}

dimensions = {
    "width": 106,
    "height": 109,
    "halfWidth": 53,
    "halfHeight": 54,
}

floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

floorsConfidence = [0.85, 0.85, 0.9, 0.95, 0.95, 0.95,
                    0.95, 0.85, 0.95, 0.95, 0.95, 0.95, 0.95, 0.9, 0.85, 0.85]

# floorsImgs = np.load('radar/npys/floorsImgs.npy', allow_pickle=True)

floorsImgs = [
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-0.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-1.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-2.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-3.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-4.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-5.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-6.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-7.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-8.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-9.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-10.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-11.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-12.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-13.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-14.png')),
    utils.image.RGBtoGray(utils.image.load('radar/images/floor-15.png')),
]

floorsPathsSqms = np.load('radar/npys/floorsPathsSqms.npy')

images = {
    "tools": utils.image.loadAsGrey('radar/images/radar-tools.png')
}

floorsLevelsImgs = np.load('radar/npys/floorsLevelsImgs.npy')
floorsLevelsImgsHashes = {}
pixelsColorsValues = {
    "accessPoint": 226,
    "caveFloor": 111,
    "caveWall": 76,
    "commonFloorOrStreet": 1,
    "grassOrRockyGround": 120,
    "ice": 240,
    "lava": 136,
    "mountainOrStone": 102,
    "sand": 213,
    "snow": 255,
    "swamp": 207,
    "treesOrBushes": 60,
    "wall": 106,
    "water": 93,
    "vacuumOrUndiscoveredArea": 0
}
nonWalkablePixelsColors = [
    pixelsColorsValues["caveWall"],
    pixelsColorsValues["lava"],
    pixelsColorsValues["mountainOrStone"],
    pixelsColorsValues["swamp"],
    pixelsColorsValues["treesOrBushes"],
    pixelsColorsValues["wall"],
    pixelsColorsValues["water"],
    pixelsColorsValues["vacuumOrUndiscoveredArea"],
]
walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in floors:
    floorHash = utils.core.hashit(floorsLevelsImgs[floor])
    floorsLevelsImgsHashes[floorHash] = floor
    walkableFloorSqms = np.where(
        np.isin(floorsImgs[floor], nonWalkablePixelsColors), 0, 1)
    walkableFloorsSqms[floor] = walkableFloorSqms

# radarImagesCoordinates = np.load('radar/npys/radarImagesCoordinates.npy', allow_pickle=True)
# walkableFloorsSqms = np.load('radar/npys/walkableFloorsSqms.npy')
