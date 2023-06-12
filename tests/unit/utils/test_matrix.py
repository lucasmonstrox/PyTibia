import numpy as np
from src.utils.matrix import getAdjacencyMatrix, hasMatrixInsideOther


def test_should_call_function_getAdjacencyMatrix_and_return_correct_adjacency_matrix():
    matrix = np.array([
        [1, 1],
        [0, 1]
    ])
    correctAdjacencyMatrix = np.array([
        [0, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ])
    assert np.array_equal(getAdjacencyMatrix(matrix), correctAdjacencyMatrix) == True

def test_should_return_False_when_has_no_matrix_inside_other():
    firstMatrix = np.array([[0, 1]])
    secondMatrix = np.array([[1, 0]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == False

def test_should_return_True_when_has_no_matrix_inside_other():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 0]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_113():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 113]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_29():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 29]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_57():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 57]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_91():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 91]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_152():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 152]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_170():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 170]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True

def test_should_return_True_when_has_matrix_inside_other_by_pixel_color_192():
    firstMatrix = np.array([[0, 0]])
    secondMatrix = np.array([[1, 192]])
    assert hasMatrixInsideOther(firstMatrix, secondMatrix) == True
