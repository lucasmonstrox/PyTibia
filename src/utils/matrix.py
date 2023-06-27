from numba import njit
from src.shared.typings import GrayImage


@njit(cache=True, fastmath=True)
def hasMatrixInsideOther(matrix: GrayImage, other: GrayImage) -> bool:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if other[i][j] == 0 and (matrix[i][j] != 0 and matrix[i][j] != 113 and matrix[i][j] != 29 and matrix[i][j] != 57 and matrix[i][j] != 91 and matrix[i][j] != 152 and matrix[i][j] != 170 and matrix[i][j] != 192):
                return False
    return True
