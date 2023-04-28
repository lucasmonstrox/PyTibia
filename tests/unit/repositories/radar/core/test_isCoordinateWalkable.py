from src.repositories.radar.core import isCoordinateWalkable


def test_should_return_False_when_cordinate_is_not_walkable():
    coordinate = (33094, 32789, 7)
    result = isCoordinateWalkable(coordinate)
    assert result == False


def test_should_return_True_when_cordinate_is_walkable():
    coordinate = (33094, 32790, 7)
    result = isCoordinateWalkable(coordinate)
    assert result == True
