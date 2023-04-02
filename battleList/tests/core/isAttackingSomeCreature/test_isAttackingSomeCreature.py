import numpy as np
from battleList.core import isAttackingSomeCreature
from battleList.typing import creatureType


def test_should_return_False_when_no_creatures_is_being_attacked():
    creatures = np.array([('Rat', False), ('Dragon', False)], dtype=creatureType)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = False
    assert isAttacking == expectedIsAttackingSomeCreature


def test_should_return_False_when_there_are_no_creatures():
    creatures = np.array([], dtype=creatureType)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = False
    assert isAttacking == expectedIsAttackingSomeCreature


def test_should_return_True_when_some_creature_is_being_attacked():
    creatures = np.array([('Rat', True), ('Dragon', False)], dtype=creatureType)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = True
    assert isAttacking == expectedIsAttackingSomeCreature
