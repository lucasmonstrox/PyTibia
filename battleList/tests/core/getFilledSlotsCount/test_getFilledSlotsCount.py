import unittest
from battleList.core import getFilledSlotsCount
import utils.image


class TestGetFilledSlotsCount(unittest.TestCase):
    def test_return_0_when_battle_list_empty(self):
        emptyBattleListContent = utils.image.loadAsArray(
            'battleList/tests/getFilledSlotsCount/emptyBattleListContent.png')
        filledSlotsCount = getFilledSlotsCount(emptyBattleListContent)
        self.assertEqual(filledSlotsCount, 0)

    def test_return_1_when_battle_list_has_only_one_creature(self):
        onlyOneCreatureBattleListContent = utils.image.loadAsArray(
            'battleList/tests/getFilledSlotsCount/onlyOneCreatureBattleListContent.png')
        filledSlotsCount = getFilledSlotsCount(
            onlyOneCreatureBattleListContent)
        self.assertEqual(filledSlotsCount, 1)

    def test_return_44_when_battle_list_is_full(self):
        fullBattleListContent = utils.image.loadAsArray(
            'battleList/tests/getFilledSlotsCount/fullBattleListContent.png')
        filledSlotsCount = getFilledSlotsCount(fullBattleListContent)
        self.assertEqual(filledSlotsCount, 44)


if __name__ == '__main__':
    unittest.main()
