import matplotlib.pyplot as plt
import networkx as nx
from radar import radar
from time import time
import numpy as np
from utils import utils


def main():
    loop_time = time()
    
    G = nx.DiGraph()
    pixels = utils.loadImgAsArray('radar/images/floor-7.png')
    startingXCoordinate = 31744
    startingYCoordinate = 30976
    floorLevel = 7
    (xPixel, yPixel) = utils.getPixelFromCoordinate((startingXCoordinate, startingYCoordinate, floorLevel))
    # pixels = pixels[yPixel:yPixel + 13, xPixel:xPixel + 13]
    # utils.saveImg(pixels, 'pixels.png')
    y = -1
    totalFreePixels = 0
    for row in pixels:
        x = -1
        y += 1
        if y > len(pixels) - 1:
            break
        print(' ')
        for _ in row:
            print(' ')
            x += 1
            print('x, y', x, y)
            print('x > len(row) - 1', x, len(row))
            if x > len(row) - 1:
                break
            pixel = pixels[y][x]
            isForbiddenPixel = np.isin(pixel, radar.forbiddenPixelsColors)
            print('pixel: ', pixel, 'isForbiddenPixel: ', isForbiddenPixel)
            if isForbiddenPixel:
                continue
            totalFreePixels += 1
            XCoordinate = x + startingXCoordinate
            YCoordinate = y + startingYCoordinate
            print('XCoordinate: ', XCoordinate, 'YCoordinate: ', YCoordinate)
            G.add_node((XCoordinate, YCoordinate, floorLevel))
            shouldAddTopRelation = y > 0 and not radar.isForbiddenPixelColor(pixels[y - 1][x])
            print('shouldAddTopRelation: ', shouldAddTopRelation)
            if shouldAddTopRelation:
                G.add_edge((XCoordinate, YCoordinate, floorLevel), (XCoordinate, YCoordinate - 1, floorLevel))
            shouldAddRightRelation = x < len(pixels[y]) - 1 and not radar.isForbiddenPixelColor(pixels[y][x + 1])
            print('shouldAddRightRelation: ', shouldAddRightRelation)
            if shouldAddRightRelation:
                G.add_edge((XCoordinate, YCoordinate, floorLevel), (XCoordinate + 1, YCoordinate, floorLevel))
            shouldAddBottomRelation = y < len(pixels) - 1 and not radar.isForbiddenPixelColor(pixels[y + 1][x])
            print('shouldAddBottomRelation: ', shouldAddBottomRelation)
            if shouldAddBottomRelation:
                G.add_edge((XCoordinate, YCoordinate, floorLevel), (XCoordinate, YCoordinate + 1, floorLevel))
            shouldAddLeftRelation = x > 0 and not radar.isForbiddenPixelColor(pixels[y][x - 1])
            print('shouldAddLeftRelation: ', shouldAddLeftRelation)
            if shouldAddLeftRelation:
                G.add_edge((XCoordinate, YCoordinate, floorLevel), (XCoordinate - 1, YCoordinate, floorLevel))
        
        # break
    print('totalFreePixels', totalFreePixels)
    return
    # nx.draw_networkx(G, with_labels=True)
    # plt.show()
    while True:
        try:
            paths = nx.single_source_dijkstra(G, (32997, 32774, 7), target=(33005, 32773, 7))
            # print(paths)
            paths = nx.single_source_dijkstra(G, (33003, 32772, 7), target=(32952, 32863, 7))
            # print(paths)
        except:
            print('No path found')
        # break
        # print(nx.multi_source_dijkstra_path(G, sources=[7, 5], target=1))
        # break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()

if __name__ == '__main__':
    main()