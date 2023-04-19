from src.repositories.radar.core import isCloseToCoordinate


def test_should_return_False_when_possible_cordinate_is_not_in_coordinate():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32791, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=0)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_vertically_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_diagonaly_right_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33096, 32788, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_horizontaly_right_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_diagonaly_bottom_right_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33096, 32792, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_vertically_below_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_diagonaly_bottom_left_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33092, 32792, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_horizontaly_left_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33091, 32790, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_False_when_possible_cordinate_is_not_close_diagonaly_left_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33092, 32788, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=2)
    assert result == False


def test_should_return_True_when_possible_cordinate_is_in_coordinate():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32790, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=0)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_not_close_vertically_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_diagonaly_right_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33096, 32788, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_horizontaly_right_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_diagonaly_bottom_right_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33096, 32792, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_vertically_below_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33094, 32793, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_diagonaly_bottom_left_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33092, 32792, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_horizontaly_left_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33091, 32790, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True


def test_should_return_True_when_possible_cordinate_is_close_diagonaly_left_top_from_coordinate_by_3_of_distance_tolerance():
    currentCoordinate = (33094, 32790, 7)
    possibleCloseCoordinate = (33092, 32788, 7)
    result = isCloseToCoordinate(
        currentCoordinate, possibleCloseCoordinate, distanceTolerance=3)
    assert result == True
