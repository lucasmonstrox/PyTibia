from battleList.core import getContainerBottomBarPos
import utils.image


def test_should_assert_content():
    screenshot = utils.image.loadAsArray(
        'battleList/tests/core/getContainerBottomBarPos/screenshot.png')
    containerBottomBarPos = getContainerBottomBarPos(screenshot)
    assert containerBottomBarPos == (1748, 584, 156, 4)
