from battleList.core import getContainerTopBarPos
import utils.image


def test_should_assert_content():
    screenshot = utils.image.loadAsArray(
        'battleList/tests/core/getContainerTopBarPos/screenshot.png')
    containerTopBarPos = getContainerTopBarPos(screenshot)
    assert containerTopBarPos == (1572, 25, 81, 13)
