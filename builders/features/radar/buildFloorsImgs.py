import numpy as np
from src.utils.image import loadAsGrey


def main():
    floorsImgs = [
        loadAsGrey('radar/images/floor-0.png'),
        loadAsGrey('radar/images/floor-1.png'),
        loadAsGrey('radar/images/floor-2.png'),
        loadAsGrey('radar/images/floor-3.png'),
        loadAsGrey('radar/images/floor-4.png'),
        loadAsGrey('radar/images/floor-5.png'),
        loadAsGrey('radar/images/floor-6.png'),
        loadAsGrey('radar/images/floor-7.png'),
        loadAsGrey('radar/images/floor-8.png'),
        loadAsGrey('radar/images/floor-9.png'),
        loadAsGrey('radar/images/floor-10.png'),
        loadAsGrey('radar/images/floor-11.png'),
        loadAsGrey('radar/images/floor-12.png'),
        loadAsGrey('radar/images/floor-13.png'),
        loadAsGrey('radar/images/floor-14.png'),
        loadAsGrey('radar/images/floor-15.png')
    ]
    np.save('radar/npys/floorsImgs.npy', floorsImgs)


if __name__ == '__main__':
    main()