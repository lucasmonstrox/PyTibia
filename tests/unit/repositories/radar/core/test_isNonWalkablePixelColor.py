from src.repositories.radar.config import pixelsColorsValues
from src.repositories.radar.core import isNonWalkablePixelColor


def test_should_return_False_when_pixel_color_is_an_access_point():
    result = isNonWalkablePixelColor(pixelsColorsValues['accessPoint'])
    assert result == False


def test_should_return_False_when_pixel_color_is_cave_floor():
    result = isNonWalkablePixelColor(pixelsColorsValues['caveFloor'])
    assert result == False


def test_should_return_False_when_pixel_color_is_common_floor_or_street():
    result = isNonWalkablePixelColor(pixelsColorsValues['commonFloorOrStreet'])
    assert result == False


def test_should_return_False_when_pixel_color_is_grass_or_rocky_ground():
    result = isNonWalkablePixelColor(pixelsColorsValues['grassOrRockyGround'])
    assert result == False


def test_should_return_False_when_pixel_color_is_sand():
    result = isNonWalkablePixelColor(pixelsColorsValues['sand'])
    assert result == False


def test_should_return_False_when_pixel_color_is_snow():
    result = isNonWalkablePixelColor(pixelsColorsValues['snow'])
    assert result == False


def test_should_return_True_when_pixel_color_is_cave_wall():
    result = isNonWalkablePixelColor(pixelsColorsValues['caveWall'])
    assert result == True


def test_should_return_True_when_pixel_color_is_lava():
    result = isNonWalkablePixelColor(pixelsColorsValues['lava'])
    assert result == True


def test_should_return_True_when_pixel_color_is_mountain_or_stone():
    result = isNonWalkablePixelColor(pixelsColorsValues['mountainOrStone'])
    assert result == True


def test_should_return_True_when_pixel_color_is_swamp():
    result = isNonWalkablePixelColor(pixelsColorsValues['swamp'])
    assert result == True


def test_should_return_True_when_pixel_color_is_trees_or_bushes():
    result = isNonWalkablePixelColor(pixelsColorsValues['treesOrBushes'])
    assert result == True


def test_should_return_True_when_pixel_color_is_wall():
    result = isNonWalkablePixelColor(pixelsColorsValues['wall'])
    assert result == True


def test_should_return_True_when_pixel_color_is_water():
    result = isNonWalkablePixelColor(pixelsColorsValues['water'])
    assert result == True


def test_should_return_True_when_pixel_color_is_vacuum_or_undiscovered_area():
    result = isNonWalkablePixelColor(
        pixelsColorsValues['vacuumOrUndiscoveredArea'])
    assert result == True
