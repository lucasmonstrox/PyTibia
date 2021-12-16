import cupy as cp


y = cp.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    480, 506,
    960, 986,
    1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466
])

allBlack = cp.zeros(y.size, dtype=cp.uint8)
hudWidth = 480


def getCreaturesBars(blackPixels):
    blackPixelsIndexes = cp.nonzero(blackPixels == 0)[0]
    noBlackPixels = blackPixelsIndexes.size == 0
    if noBlackPixels:
        return cp.array([])
    x = cp.arange(y.size)
    x = cp.broadcast_to(blackPixelsIndexes, (y.size, blackPixelsIndexes.size))
    x = cp.transpose(x)
    z = cp.add(x, y)
    pixelsColorsIndexes = cp.take(blackPixels, z)
    g = (pixelsColorsIndexes == allBlack).all(1)
    possibleCreatures = cp.nonzero(g)[0]
    hasNoCreatures = possibleCreatures.size == 0
    if hasNoCreatures:
        return cp.array([])
    creatures = cp.take(blackPixelsIndexes, possibleCreatures)
    creatures = cp.array(
        list(map(lambda i: [i % hudWidth, i // hudWidth], creatures)))
    return creatures
