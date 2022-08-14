import pathlib
from battleList.locators import getContainerTopBarPos
import utils.image


def test_should_get_container_top_bar_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = utils.image.loadAsArray(f'{currentPath}/screenshot.png')
    containerTopBarPos = getContainerTopBarPos(screenshot)
    expectedContainerTopBarPos = (1572, 25, 81, 13)
    assert containerTopBarPos == expectedContainerTopBarPos
