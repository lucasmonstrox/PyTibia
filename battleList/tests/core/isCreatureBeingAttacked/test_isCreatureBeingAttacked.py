import pathlib
from battleList.core import isCreatureBeingAttacked
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_creature_is_not_being_attacked():
    slotImg = utils.image.loadAsGrey(
        f'{currentPath}/creatureIsntBeingAttacked.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == False


def test_should_return_True_when_creature_is_being_attacked():
    slotImg = utils.image.loadAsGrey(
        f'{currentPath}/creatureIsBeingAttacked.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == True


def test_should_return_True_when_creature_is_being_attacked_highlighted():
    slotImg = utils.image.loadAsGrey(
        f'{currentPath}/creatureIsBeingAttackedHighlighted.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == True
