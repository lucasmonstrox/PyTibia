import unittest
from battleList.core import isCreatureBeingAttacked
import utils.image


class TestIsCreatureBeingAttacked(unittest.TestCase):
    def test_should_return_False_when_creature_is_not_being_attacked(self):
        slotImg = utils.image.loadAsArray(
            'battleList/tests/isCreatureBeingAttacked/creatureIsntBeingAttacked.png')
        result = isCreatureBeingAttacked(slotImg)
        self.assertFalse(result)

    def test_should_return_True_when_creature_is_being_attacked(self):
        slotImg = utils.image.loadAsArray(
            'battleList/tests/isCreatureBeingAttacked/creatureIsBeingAttacked.png')
        result = isCreatureBeingAttacked(slotImg)
        self.assertTrue(result)

    def test_should_return_True_when_creature_is_being_attacked_highlighted(self):
        slotImg = utils.image.loadAsArray(
            'battleList/tests/isCreatureBeingAttacked/creatureIsBeingAttackedHighlighted.png')
        result = isCreatureBeingAttacked(slotImg)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
