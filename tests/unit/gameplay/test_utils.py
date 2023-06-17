from src.gameplay.utils import coordinatesAreEqual


def test_should_return_False_when_x0_is_greater_than_x1():
    assert coordinatesAreEqual((1, 2, 3), (0, 2, 3)) == False


def test_should_return_False_when_x1_is_greater_than_x0():
    assert coordinatesAreEqual((0, 2, 3), (1, 2, 3)) == False


def test_should_return_False_when_y0_is_greater_than_y1():
    assert coordinatesAreEqual((1, 1, 3), (1, 0, 3)) == False


def test_should_return_False_when_y1_is_greater_than_y0():
    assert coordinatesAreEqual((1, 0, 3), (1, 1, 3)) == False


def test_should_return_False_when_z0_is_greater_than_z1():
    assert coordinatesAreEqual((1, 2, 1), (1, 2, 0)) == False


def test_should_return_False_when_z1_is_greater_than_z0():
    assert coordinatesAreEqual((1, 2, 0), (1, 2, 1)) == False


def test_should_return_True_when_coordinates_are_equal():
    assert coordinatesAreEqual((1, 2, 3), (1, 2, 3)) == True
