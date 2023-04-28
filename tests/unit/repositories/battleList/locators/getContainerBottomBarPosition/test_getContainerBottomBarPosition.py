import pathlib
from src.repositories.battleList.locators import getContainerBottomBarPosition
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


# TODO: assert "locate" calls and params
def test_should_get_container_bottom_bar_pos():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    containerBottomBarPos = getContainerBottomBarPosition(screenshotImage)
    expectedContainerBottomBarPos = (1748, 621, 156, 4)
    assert containerBottomBarPos == expectedContainerBottomBarPos
