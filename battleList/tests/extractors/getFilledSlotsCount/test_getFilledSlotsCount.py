import pathlib
from battleList.extractors import getFilledSlotsCount
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_0_when_battle_list_content_is_empty():
    emptyBattleListContentImg = utils.image.loadAsGrey(
        f'{currentPath}/emptyBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(emptyBattleListContentImg)
    assert filledSlotsCount == 0


def test_should_return_1_when_battle_list_has_only_one_creature():
    onlyOneCreatureInBattleListContentImg = utils.image.loadAsGrey(
        f'{currentPath}/onlyOneCreatureInBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(
        onlyOneCreatureInBattleListContentImg)
    assert filledSlotsCount == 1


def test_should_return_44_when_battle_list_content_is_full():
    fullCreaturesInBattleListContentImg = utils.image.loadAsGrey(
        f'{currentPath}/fullCreaturesInBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(fullCreaturesInBattleListContentImg)
    assert filledSlotsCount == 44
