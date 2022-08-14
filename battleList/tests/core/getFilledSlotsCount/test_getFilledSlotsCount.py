from battleList.core import getFilledSlotsCount
import utils.image


def test_return_0_when_battle_list_is_empty():
    emptyBattleListContent = utils.image.loadAsArray(
        'battleList/tests/core/getFilledSlotsCount/emptyBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(emptyBattleListContent)
    assert filledSlotsCount == 0


def test_return_1_when_battle_list_has_only_one_creature():
    onlyOneCreatureBattleListContent = utils.image.loadAsArray(
        'battleList/tests/core/getFilledSlotsCount/onlyOneCreatureBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(
        onlyOneCreatureBattleListContent)
    assert filledSlotsCount == 1


def test_return_44_when_battle_list_is_full():
    fullBattleListContent = utils.image.loadAsArray(
        'battleList/tests/core/getFilledSlotsCount/fullBattleListContent.png')
    filledSlotsCount = getFilledSlotsCount(fullBattleListContent)
    assert filledSlotsCount == 44
