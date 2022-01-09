import cv2
import numpy as np
from time import time
from hud import hud
from utils import utils
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

def main():
    graph = [
        [0, 1, 2, 0],
        [0, 0, 0, 1],
        [2, 0, 0, 3],
        [0, 0, 0, 0]
    ]
    graph = csr_matrix(graph)
    res = dijkstra(csgraph=graph, directed=False, unweighted=True, indices=[[0,1], [2,3]])
    print(res)
    # loop_time = time()
    # while True:
    #     screenshot = utils.getScreenshot()
    #     hudCoordinates = hud.getCoordinates(screenshot)
    #     # hud.clickSlot((7, 4), hudCoordinates)
    #     hud.rightClickSlot((2, 4), hudCoordinates)
    #     print(hudCoordinates)
    #     break
    #     timef = (time() - loop_time)
    #     timef = timef if timef else 1
    #     fps = 1 / timef
    #     print('FPS {}'.format(fps))
    #     loop_time = time()


if __name__ == '__main__':
    main()
