from src.utils.matrix import hasMatrixInsideOther


def should_return_False_when_has_no_matrix_inside_other():
    firstMatrix = [0, 1]
    secondMatrix = [1, 0]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == False

def should_return_True_when_has_no_matrix_inside_other():
    firstMatrix = [0, 0]
    secondMatrix = [1, 0]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_113():
    firstMatrix = [0, 0]
    secondMatrix = [1, 113]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_29():
    firstMatrix = [0, 0]
    secondMatrix = [1, 29]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_57():
    firstMatrix = [0, 0]
    secondMatrix = [1, 57]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_91():
    firstMatrix = [0, 0]
    secondMatrix = [1, 91]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_152():
    firstMatrix = [0, 0]
    secondMatrix = [1, 152]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_170():
    firstMatrix = [0, 0]
    secondMatrix = [1, 170]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def should_return_True_when_has_matrix_inside_other_by_pixel_color_192():
    firstMatrix = [0, 0]
    secondMatrix = [1, 192]
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True
