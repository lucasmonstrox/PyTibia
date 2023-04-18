import numpy as np
from src.utils.image import loadFromRGBToGray


def main():
    floorsImgs = [
        loadFromRGBToGray('radar/images/floor-0.png'),
        loadFromRGBToGray('radar/images/floor-1.png'),
        loadFromRGBToGray('radar/images/floor-2.png'),
        loadFromRGBToGray('radar/images/floor-3.png'),
        loadFromRGBToGray('radar/images/floor-4.png'),
        loadFromRGBToGray('radar/images/floor-5.png'),
        loadFromRGBToGray('radar/images/floor-6.png'),
        loadFromRGBToGray('radar/images/floor-7.png'),
        loadFromRGBToGray('radar/images/floor-8.png'),
        loadFromRGBToGray('radar/images/floor-9.png'),
        loadFromRGBToGray('radar/images/floor-10.png'),
        loadFromRGBToGray('radar/images/floor-11.png'),
        loadFromRGBToGray('radar/images/floor-12.png'),
        loadFromRGBToGray('radar/images/floor-13.png'),
        loadFromRGBToGray('radar/images/floor-14.png'),
        loadFromRGBToGray('radar/images/floor-15.png')
    ]
    np.save('radar/npys/floorsImgs.npy', floorsImgs)


if __name__ == '__main__':
    main()