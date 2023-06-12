from src.utils.coordinate import getClosestCoordinate, getCoordinateFromPixel, getDirectionBetweenCoordinates, getPixelFromCoordinate


def test_should_call_function_getClosestCoordinate_and_return_closest_coordinate():
    coordinate = (1, 1, 1)
    closestCoordinate = (2, 2, 1)
    coordinates = [(9, 9, 1), closestCoordinate]
    assert getClosestCoordinate(coordinate, coordinates) == closestCoordinate

def test_should_return_pixel_from_coordinate():
    pixelCoordinate = (0, 0)
    assert getCoordinateFromPixel(pixelCoordinate) == (31744, 30976)

def test_should_return_right_when_next_x_coordinate_is_greather_than_current_x_coordinate():
    coordinate = (0, 0, 0)
    nextCoordinate = (1, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'right'

def test_should_return_left_when_current_x_coordinate_is_greather_than_next_x_coordinate():
    coordinate = (1, 0, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'left'

def test_should_return_down_when_next_y_coordinate_is_greather_than_current_y_coordinate():
    coordinate = (0, 0, 0)
    nextCoordinate = (0, 1, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'down'

def test_should_return_up_when_currnet_y_coordinate_is_greather_than_next_y_coordinate():
    coordinate = (0, 1, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) == 'up'

def test_should_return_None_when_x_or_y_are_equals():
    coordinate = (0, 0, 0)
    nextCoordinate = (0, 0, 0)
    assert getDirectionBetweenCoordinates(coordinate, nextCoordinate) is None

def test_should_return_pixel_from_coordinate():
    coordinate = (31744, 30976, 7)
    assert getPixelFromCoordinate(coordinate) == (0, 0)
