import numpy as np
from src.repositories.radar.config import floors
from src.utils.image import load


def main():
    floorsPathsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint8)
    for floor in floors:
        floorPaths = load(f'radar/images/paths/floor-{floor}.png')
        floorPaths = floorPaths[:, :, :1]
        floorPaths = floorPaths.reshape(2048, 2560)
        floorsPathsSqms[floor] = floorPaths
    np.save('radar/npys/floorsPathsSqms.npy', floorsPathsSqms)


if __name__ == '__main__':
    main()