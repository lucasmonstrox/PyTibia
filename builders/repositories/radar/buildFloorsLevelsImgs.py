import numpy as np
from src.utils.image import loadFromRGBToGray


def main():
    floorsLevelsImgs = [
        loadFromRGBToGray('radar/images/floor-levels/0.png'),
        loadFromRGBToGray('radar/images/floor-levels/1.png'),
        loadFromRGBToGray('radar/images/floor-levels/2.png'),
        loadFromRGBToGray('radar/images/floor-levels/3.png'),
        loadFromRGBToGray('radar/images/floor-levels/4.png'),
        loadFromRGBToGray('radar/images/floor-levels/5.png'),
        loadFromRGBToGray('radar/images/floor-levels/6.png'),
        loadFromRGBToGray('radar/images/floor-levels/7.png'),
        loadFromRGBToGray('radar/images/floor-levels/8.png'),
        loadFromRGBToGray('radar/images/floor-levels/9.png'),
        loadFromRGBToGray('radar/images/floor-levels/10.png'),
        loadFromRGBToGray('radar/images/floor-levels/11.png'),
        loadFromRGBToGray('radar/images/floor-levels/12.png'),
        loadFromRGBToGray('radar/images/floor-levels/13.png'),
        loadFromRGBToGray('radar/images/floor-levels/14.png'),
        loadFromRGBToGray('radar/images/floor-levels/15.png'),
    ]
    np.save('radar/npys/floorsLevelsImgs.npy', floorsLevelsImgs)


if __name__ == '__main__':
    main()