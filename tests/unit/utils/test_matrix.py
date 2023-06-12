from src.utils.matrix import hasMatrixInsideOther


def should_return_False_when_has_no_matrix_inside_other():
    firstMatrix = [0, 1]
    secondMatrix = [1, 0]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == False

def should_return_True_when_has_no_matrix_inside_other():
    firstMatrix = [0, 0]
    secondMatrix = [1, 0]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True
