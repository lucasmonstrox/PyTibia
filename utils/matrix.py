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
    return connections


def hasMatrixInsideOther(matrix, other):
    matrixFlattened = matrix.flatten()
    otherFlattened = other.flatten()
    blackPixelsIndexes = np.nonzero(otherFlattened == 0)[0]
    blackPixels = np.take(matrixFlattened, blackPixelsIndexes)
    didMatch = np.all(blackPixels == 0)
    return True if didMatch else False