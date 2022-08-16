import numpy as np
import radar.config
import utils.core
import utils.image

walkableFloorsSqms = np.ndarray(shape=(16, 2048, 2560), dtype=np.uint)

for floor in radar.config["floors"]:
    floorImg = utils.image.loadAsGrey(
        'radar/images/floor-{}.png'.format(floor))
    floorSqms = np.where(
        np.isin(floorImg, radar.config.nonWalkablePixelsColors),
        0,
        1
    )
    walkableFloorsSqms[floor] = floorSqms

np.save('radar/npys/walkableFloorsSqms.npy', walkableFloorsSqms)
