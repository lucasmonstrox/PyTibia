from numba import njit
import numpy as np


def getAdjacencyMatrix(arr):
    repArrHorizontal = np.ravel(arr)
    arrDim = arr.shape[0] * arr.shape[1]
    arrShape = (arrDim, arrDim)
    repArr = np.broadcast_to(repArrHorizontal, arrShape)
    seqArr = np.arange(1, arrDim + 1)
    verticesWithPossibleRightConnections = np.eye(arrDim, k=1)
    indexesWithPossibleRightConnections = np.where(seqArr % arr.shape[1] == 0, 0, 1)
    indexesWithPossibleRightConnections = np.broadcast_to(indexesWithPossibleRightConnections, arrShape)
    indexesWithPossibleRightConnections = np.rot90(indexesWithPossibleRightConnections, k=-1)
    rightConnections = np.multiply(verticesWithPossibleRightConnections, indexesWithPossibleRightConnections)
    verticesWithPossibleLeftConnections = np.eye(arrDim, k=-1)
    indexesWithPossibleLeftConnections = np.flip(indexesWithPossibleRightConnections)
    leftConnections = np.multiply(verticesWithPossibleLeftConnections, indexesWithPossibleLeftConnections)
    topConnections = np.eye(arrDim, k=-arr.shape[1])
    bottomConnections = np.eye(arrDim, k=arr.shape[1])
    topBottomConnections = np.add(topConnections, bottomConnections)
    leftRightConnections = np.add(leftConnections, rightConnections)
    connections = np.add(topBottomConnections, leftRightConnections)
    connections = np.multiply(connections, repArr)
    connections = np.multiply(connections, np.rot90(repArr, k=-1))
    connections = np.array(connections, dtype=np.uint)
    return connections


@njit(cache=True, fastmath=True)
def hasMatrixInsideOther(matrix, other):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if other[i][j] == 0 and (matrix[i][j] != 0 and matrix[i][j] != 113 and matrix[i][j] != 29 and matrix[i][j] != 57 and matrix[i][j] != 91 and matrix[i][j] != 152 and matrix[i][j] != 170 and matrix[i][j] != 192):
                return False
    return True


@njit(cache=True, fastmath=True)
def hasMatrixInsideOtherNp(matrix, other):
    matrixFlattened = np.ravel(matrix)
    otherFlattened = np.ravel(other)
    blackPixelsIndexes = np.flatnonzero(otherFlattened == 0)
    blackPixels = np.take(matrixFlattened, blackPixelsIndexes)
    didMatch = np.all(blackPixels == 0)
    return didMatch