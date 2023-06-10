from src.gameplay.utils import coordinatesAreEqual


def test_should_return_False_when_coordinates_X_are_different():
    assert coordinatesAreEqual((1, 2, 3), (0, 2, 3)) == False

def test_should_return_False_when_coordinates_Y_are_different():
    assert coordinatesAreEqual((1, 2, 3), (1, 0, 3)) == False

def test_should_return_False_when_coordinates_Y_are_different():
    assert coordinatesAreEqual((1, 2, 3), (1, 2, 0)) == False

def test_should_return_True_when_coordinates_are_equal():
    assert coordinatesAreEqual((1, 2, 3), (1, 2, 3)) == True