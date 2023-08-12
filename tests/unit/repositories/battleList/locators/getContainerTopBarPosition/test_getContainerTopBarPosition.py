import pathlib
from src.repositories.battleList.locators import getBattleListIconPosition
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


# TODO: assert "locate" calls and params
def test_should_get_battle_list_icon_position():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    battleListIconPosition = getBattleListIconPosition(screenshotImage)
    expectedContainerTopBarPos = (1573, 26, 11, 11)
    assert battleListIconPosition == expectedContainerTopBarPos
