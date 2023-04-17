import numpy as np
from src.utils.image import loadAsGrey


def main():
    floorsLevelsImgs = [
        loadAsGrey('radar/images/floor-levels/0.png'),
        loadAsGrey('radar/images/floor-levels/1.png'),
        loadAsGrey('radar/images/floor-levels/2.png'),
        loadAsGrey('radar/images/floor-levels/3.png'),
        loadAsGrey('radar/images/floor-levels/4.png'),
        loadAsGrey('radar/images/floor-levels/5.png'),
        loadAsGrey('radar/images/floor-levels/6.png'),
        loadAsGrey('radar/images/floor-levels/7.png'),
        loadAsGrey('radar/images/floor-levels/8.png'),
        loadAsGrey('radar/images/floor-levels/9.png'),
        loadAsGrey('radar/images/floor-levels/10.png'),
        loadAsGrey('radar/images/floor-levels/11.png'),
        loadAsGrey('radar/images/floor-levels/12.png'),
        loadAsGrey('radar/images/floor-levels/13.png'),
        loadAsGrey('radar/images/floor-levels/14.png'),
        loadAsGrey('radar/images/floor-levels/15.png'),
    ]
    np.save('radar/npys/floorsLevelsImgs.npy', floorsLevelsImgs)


if __name__ == '__main__':
    main()