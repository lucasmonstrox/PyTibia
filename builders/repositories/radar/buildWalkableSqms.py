import numpy as np
from src.repositories.radar.config import floors
from src.repositories.radar.core import isNonWalkablePixelColor
from src.utils.image import loadFromRGBToGray


def main():
    walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)
    for floor in floors:
        floorImg = loadFromRGBToGray(f'src/repositories/radar/images/floor-{floor}.png')
        floorSqms = np.where(isNonWalkablePixelColor(floorImg), 0, 1)
        walkableFloorsSqms[floor] = floorSqms
    np.save('src/repositories/radar/npys/walkableFloorsSqms.npy', walkableFloorsSqms)


if __name__ == '__main__':
    main()