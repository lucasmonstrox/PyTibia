import pathlib
from src.repositories.battleList.core import getFilledSlotsCount
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_0_when_battle_list_content_is_empty():
    emptyBattleListContentImage = loadFromRGBToGray(
        f'{currentPath}/emptyBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(emptyBattleListContentImage)
    assert filledSlotsCount == 0


def test_should_return_1_when_battle_list_has_only_one_creature():
    onlyOneCreatureInBattleListContentImage = loadFromRGBToGray(
        f'{currentPath}/onlyOneCreatureInBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(
        onlyOneCreatureInBattleListContentImage)
    assert filledSlotsCount == 1


def test_should_return_44_when_battle_list_content_is_full():
    fullCreaturesInBattleListContentImage = loadFromRGBToGray(
        f'{currentPath}/fullCreaturesInBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(fullCreaturesInBattleListContentImage)
    assert filledSlotsCount == 44
