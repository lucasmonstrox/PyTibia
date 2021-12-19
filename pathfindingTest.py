import numpy as np
from time import time
from skimage.graph import route_through_array


def main():
    loop_time = time()
    while True:
        image = np.array([
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
        ])
        ways = route_through_array(
            image, [0, 0], [2, 3], fully_connected=False)
        print(ways)
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
