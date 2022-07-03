import numpy as np
from utils import utils

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

images = {
    "tools": utils.loadImgAsArray('radar/images/radar-tools.png')
}

floorsLevelsImgs = np.load('radar/npys/floorsLevelsImgs.npy')
floorsLevelsImgsHashes = {}
nonWalkablePixelsColors = [75, 1, 102, 59, 0, 106, 92]
walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in floors:
    floorHash = utils.hashit(floorsLevelsImgs[floor])
    floorsLevelsImgsHashes[floorHash] = floor
    walkableFloorSqms = np.where(
        np.isin(floorsImgs[floor], nonWalkablePixelsColors), 0, 1
    )
    walkableFloorsSqms[floor] = walkableFloorSqms

# radarImagesCoordinates = np.load('radar/npys/radarImagesCoordinates.npy', allow_pickle=True)

# walkableFloorsSqms = np.load('radar/npys/walkableFloorsSqms.npy')

