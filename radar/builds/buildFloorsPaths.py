import numpy as np
import radar.config
import utils.core
import utils.image

floorsPathsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint8)
for floor in radar.config.floors:
    floorPaths = utils.image.load(f'radar/images/paths/floor-{floor}.png')
    floorPaths = floorPaths[:, :, :1]
    floorPaths = floorPaths.reshape(2048, 2560)
    floorsPathsSqms[floor] = floorPaths
np.save('radar/npys/floorsPathsSqms.npy', floorsPathsSqms)
