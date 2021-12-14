import cupy as cp
import cv2


upperBar = cp.array(cv2.imread('blackbar.png', cv2.IMREAD_GRAYSCALE)).flatten()


def getCreaturesBars(blackPixels):
    blackPixelsIndexes = cp.nonzero(blackPixels == 0)[0]
    f = cp.where(blackPixelsIndexes <= blackPixels.size - upperBar.size)[0]
    blackPixelsIndexes = cp.take(blackPixelsIndexes, f)
    noBlackPixels = len(blackPixelsIndexes) == 0
    if noBlackPixels:
        return cp.array([])
    x = cp.arange(upperBar.size)
    x = cp.broadcast_to(x, (blackPixelsIndexes.size, upperBar.size))
    y = blackPixelsIndexes.reshape(blackPixelsIndexes.size, 1)
    y = cp.pad(y, ((0, 0), (0, upperBar.size - 1)), 'maximum')
    final = cp.take(blackPixels, x + y)
    possibleCreatures = cp.nonzero((final == upperBar).all(1))[0]
    hasNoCreatures = len(possibleCreatures) == 0
    if hasNoCreatures:
        return cp.array([])
    creatures = cp.take(blackPixelsIndexes, possibleCreatures)
    return creatures


def getCreaturesBars_deprecated(arr, seq):
    r_seq = cp.arange(seq.size)
    # TODO: initialize values directly
    arr = arr[cp.arange(arr.size - seq.size + 1)[:, None] + r_seq]
    possibleMonsters = cp.nonzero((arr == seq).all(1))[0]
    if len(possibleMonsters) == 0:
        return cp.array([])
    # possibleMonsters = cp.where(
    #     cp.logical_and(
    #         cp.logical_and(arr[possibleMonsters + 480] == 0,
    #                        arr[possibleMonsters + 960] == 0),
    #         arr[possibleMonsters + 1440] == 0
    #     ),
    #     0, possibleMonsters
    # )
    possibleMonsters = possibleMonsters[possibleMonsters != 0]
    return possibleMonsters
