import numpy as np
from src.features.radar.config import floors
from src.features.radar.core import isNonWalkablePixelColor
from src.utils.image import loadAsGrey


def main():
    walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)
    for floor in floors:
        floorImg = loadAsGrey(f'src/features/radar/images/floor-{floor}.png')
        floorSqms = np.where(isNonWalkablePixelColor(floorImg), 0, 1)
        walkableFloorsSqms[floor] = floorSqms
    np.save('src/features/radar/npys/walkableFloorsSqms.npy', walkableFloorsSqms)


if __name__ == '__main__':
    main()