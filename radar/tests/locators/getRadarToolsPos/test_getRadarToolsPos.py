import pathlib
from radar.locators import getRadarToolsPos
import utils.image


def test_should_get_radar_tools_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = utils.image.loadAsGrey(f'{currentPath}/screenshot.png')
    radarToolsPos = getRadarToolsPos(screenshot)
    expectedRadarToolsPos = (1870, 78, 20, 60)
    assert radarToolsPos == expectedRadarToolsPos
