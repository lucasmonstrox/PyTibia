import numpy as np


def hasMatrixInsideOther(matrix, other):
    matrixFlattened = matrix.flatten()
    otherFlattened = other.flatten()
    blackPixelsIndexes = np.nonzero(otherFlattened == 0)[0]
    blackPixels = np.take(matrixFlattened, blackPixelsIndexes)
    didMatch = np.all(blackPixels == 0)
    return True if didMatch else False