import utils.core
import numpy as np

floorsImgs = [
    utils.core.loadImgAsArray('radar/images/floor-0.png'),
    utils.core.loadImgAsArray('radar/images/floor-1.png'),
    utils.core.loadImgAsArray('radar/images/floor-2.png'),
    utils.core.loadImgAsArray('radar/images/floor-3.png'),
    utils.core.loadImgAsArray('radar/images/floor-4.png'),
    utils.core.loadImgAsArray('radar/images/floor-5.png'),
    utils.core.loadImgAsArray('radar/images/floor-6.png'),
    utils.core.loadImgAsArray('radar/images/floor-7.png'),
    utils.core.loadImgAsArray('radar/images/floor-8.png'),
    utils.core.loadImgAsArray('radar/images/floor-9.png'),
    utils.core.loadImgAsArray('radar/images/floor-10.png'),
    utils.core.loadImgAsArray('radar/images/floor-11.png'),
    utils.core.loadImgAsArray('radar/images/floor-12.png'),
    utils.core.loadImgAsArray('radar/images/floor-13.png'),
    utils.core.loadImgAsArray('radar/images/floor-14.png'),
    utils.core.loadImgAsArray('radar/images/floor-15.png')
]

np.save('radar/npys/floorsImgs.npy', floorsImgs)