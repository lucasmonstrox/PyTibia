import utils.image
import utils.image
import numpy as np


def main():
    floorsImgs = [
        utils.image.loadAsGrey('radar/images/floor-0.png'),
        utils.image.loadAsGrey('radar/images/floor-1.png'),
        utils.image.loadAsGrey('radar/images/floor-2.png'),
        utils.image.loadAsGrey('radar/images/floor-3.png'),
        utils.image.loadAsGrey('radar/images/floor-4.png'),
        utils.image.loadAsGrey('radar/images/floor-5.png'),
        utils.image.loadAsGrey('radar/images/floor-6.png'),
        utils.image.loadAsGrey('radar/images/floor-7.png'),
        utils.image.loadAsGrey('radar/images/floor-8.png'),
        utils.image.loadAsGrey('radar/images/floor-9.png'),
        utils.image.loadAsGrey('radar/images/floor-10.png'),
        utils.image.loadAsGrey('radar/images/floor-11.png'),
        utils.image.loadAsGrey('radar/images/floor-12.png'),
        utils.image.loadAsGrey('radar/images/floor-13.png'),
        utils.image.loadAsGrey('radar/images/floor-14.png'),
        utils.image.loadAsGrey('radar/images/floor-15.png')
    ]
    np.save('radar/npys/floorsImgs.npy', floorsImgs)


if __name__ == '__main__':
    main()