import pathlib
from src.repositories.radar.locators import getRadarToolsPosition
from src.utils.image import loadFromRGBToGray


def test_should_get_radar_tools_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    radarToolsPos = getRadarToolsPosition(screenshot)
    expectedRadarToolsPos = (1870, 78, 20, 60)
    assert radarToolsPos == expectedRadarToolsPos
