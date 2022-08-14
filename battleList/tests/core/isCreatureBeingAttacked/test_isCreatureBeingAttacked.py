from battleList.core import isCreatureBeingAttacked
import utils.image


def test_should_return_False_when_creature_is_not_being_attacked():
    slotImg = utils.image.loadAsArray(
        'battleList/tests/core/isCreatureBeingAttacked/creatureIsntBeingAttacked.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == False


def test_should_return_True_when_creature_is_being_attacked():
    slotImg = utils.image.loadAsArray(
        'battleList/tests/core/isCreatureBeingAttacked/creatureIsBeingAttacked.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == True


def test_should_return_True_when_creature_is_being_attacked_highlighted():
    slotImg = utils.image.loadAsArray(
        'battleList/tests/core/isCreatureBeingAttacked/creatureIsBeingAttackedHighlighted.png')
    result = isCreatureBeingAttacked(slotImg)
    assert result == True
