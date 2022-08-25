import numpy as np
import radar.config
import radar.core
import utils.core
import utils.image

walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in radar.config.floors:
    floorImg = utils.image.loadAsGrey(f'radar/images/floor-{floor}.png')
    floorSqms = np.where(radar.core.isNonWalkablePixelColor(floorImg), 0, 1)
    walkableFloorsSqms[floor] = floorSqms

np.save('radar/npys/walkableFloorsSqms.npy', walkableFloorsSqms)
