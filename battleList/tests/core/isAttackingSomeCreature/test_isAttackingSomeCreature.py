import numpy as np
import unittest
from battleList.core import isAttackingSomeCreature
from battleList.types import creatureType


class TestIsAttackingSomeCreature(unittest.TestCase):
    def test_should_return_False_when_creatures_array_is_empty(self):
        creatures = np.array([], dtype=creatureType)
        result = isAttackingSomeCreature(creatures)
        self.assertFalse(result)

    def test_should_return_False_when_there_is_no_creature_being_attacked(self):
        creatures = np.array([('Rat', False)], dtype=creatureType)
        result = isAttackingSomeCreature(creatures)
        self.assertFalse(result)

    def test_should_return_True_when_some_creature_is_being_attacked(self):
        creatures = np.array([('Rat', True)], dtype=creatureType)
        result = isAttackingSomeCreature(creatures)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
