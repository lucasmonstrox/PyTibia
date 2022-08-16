import pathlib
from battleList.locators import getContainerBottomBarPos
import utils.image


def test_should_get_container_bottom_bar_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = utils.image.loadAsGrey(f'{currentPath}/screenshot.png')
    containerBottomBarPos = getContainerBottomBarPos(screenshot)
    expectedContainerBottomBarPos = (1748, 584, 156, 4)
    assert containerBottomBarPos == expectedContainerBottomBarPos
