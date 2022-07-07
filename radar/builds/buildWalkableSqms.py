import numpy as np
import utils.core

walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in config["floors"]:
    floorImg = utils.core.loadImgAsArray('radar/images/floor-{}.png'.format(floor))
    floorSqms = np.where(
        np.isin(floorImg, nonWalkablePixelsColors),
        0,
        1
    )
    walkableFloorsSqms[floor] = floorSqms

np.save('radar/npys/walkableFloorsSqms.npy', walkableFloorsSqms)