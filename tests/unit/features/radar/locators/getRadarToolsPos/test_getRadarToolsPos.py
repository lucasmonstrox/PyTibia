import pathlib
from src.features.radar.locators import getRadarToolsPos
from src.utils.image import loadFromRGBToGray


def test_should_get_radar_tools_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    radarToolsPos = getRadarToolsPos(screenshot)
    expectedRadarToolsPos = (1870, 78, 20, 60)
    assert radarToolsPos == expectedRadarToolsPos
