import numpy as np
from src.repositories.battleList.core import getBeingAttackedCreatureCategory
from src.repositories.battleList.typings import Creature


def test_should_return_None_when_there_are_no_creatures():
    creatures = np.array([], dtype=Creature)
    beingAttackedCreatureCategory = getBeingAttackedCreatureCategory(creatures)
    expectedBeingAttackedCreatureCategory = None
    assert beingAttackedCreatureCategory == expectedBeingAttackedCreatureCategory


def test_should_return_None_when_no_creatures_is_being_attacked():
    creatures = np.array([('Rat', False), ('Dragon', False)], dtype=Creature)
    beingAttackedCreatureCategory = getBeingAttackedCreatureCategory(creatures)
    expectedBeingAttackedCreatureCategory = None
    assert beingAttackedCreatureCategory == expectedBeingAttackedCreatureCategory


def test_should_return_Rat_when_Rat_is_being_attacked_creature_category():
    creatures = np.array([('Rat', True), ('Dragon', False)], dtype=Creature)
    beingAttackedCreatureCategory = getBeingAttackedCreatureCategory(creatures)
    expectedBeingAttackedCreatureCategory = 'Rat'
    assert beingAttackedCreatureCategory == expectedBeingAttackedCreatureCategory