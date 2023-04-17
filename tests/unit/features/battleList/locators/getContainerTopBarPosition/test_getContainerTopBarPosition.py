import pathlib
from src.features.battleList.locators import getContainerTopBarPosition
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


# TODO: assert "locate" calls and params
def test_should_get_container_top_bar_pos():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    containerTopBarPos = getContainerTopBarPosition(screenshotImage)
    expectedContainerTopBarPos = (1572, 25, 81, 13)
    assert containerTopBarPos == expectedContainerTopBarPos
