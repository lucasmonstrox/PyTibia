import numpy as np
from battleList.core import isAttackingSomeCreature
from battleList.types import creatureType


def test_should_return_False_when_creatures_array_is_empty():
    creatures = np.array([], dtype=creatureType)
    result = isAttackingSomeCreature(creatures)
    assert result == False


def test_should_return_False_when_there_is_no_creature_being_attacked():
    creatures = np.array([('Rat', False)], dtype=creatureType)
    result = isAttackingSomeCreature(creatures)
    assert result == False


def test_should_return_True_when_some_creature_is_being_attacked():
    creatures = np.array([('Rat', True)], dtype=creatureType)
    result = isAttackingSomeCreature(creatures)
    assert result == True
