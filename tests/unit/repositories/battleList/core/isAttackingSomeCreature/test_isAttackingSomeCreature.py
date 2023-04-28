import numpy as np
from src.repositories.battleList.core import isAttackingSomeCreature
from src.repositories.battleList.typings import Creature


def test_should_return_False_when_no_creatures_is_being_attacked():
    creatures = np.array([('Rat', False), ('Dragon', False)], dtype=Creature)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = False
    assert isAttacking == expectedIsAttackingSomeCreature


def test_should_return_False_when_there_are_no_creatures():
    creatures = np.array([], dtype=Creature)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = False
    assert isAttacking == expectedIsAttackingSomeCreature


def test_should_return_True_when_some_creature_is_being_attacked():
    creatures = np.array([('Rat', True), ('Dragon', False)], dtype=Creature)
    isAttacking = isAttackingSomeCreature(creatures)
    expectedIsAttackingSomeCreature = True
    assert isAttacking == expectedIsAttackingSomeCreature
