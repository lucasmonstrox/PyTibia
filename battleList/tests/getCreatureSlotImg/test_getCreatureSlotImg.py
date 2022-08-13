import numpy as np
import unittest
from battleList.core import getCreatureSlotImg
import utils.image


# TODO: test all slots using different creatures
class TestGetCreatureSlotImg(unittest.TestCase):
    def test_should_asser_slots(self):
        firstSlot = utils.image.loadAsArray(
            'battleList/tests/getCreatureSlotImg/firstSlot.png')
        secondSlot = utils.image.loadAsArray(
            'battleList/tests/getCreatureSlotImg/secondSlot.png')
        lastSlot = utils.image.loadAsArray(
            'battleList/tests/getCreatureSlotImg/lastSlot.png')
        content = utils.image.loadAsArray(
            'battleList/tests/getCreatureSlotImg/content.png')
        firstSlotAfterExtraction = getCreatureSlotImg(content, 0)
        secondSlotAfterExtraction = getCreatureSlotImg(content, 1)
        lastSlotAfterExtraction = getCreatureSlotImg(content, 43)
        np.testing.assert_array_equal(firstSlot, firstSlotAfterExtraction)
        np.testing.assert_array_equal(secondSlot, secondSlotAfterExtraction)
        np.testing.assert_array_equal(lastSlot, lastSlotAfterExtraction)


if __name__ == '__main__':
    unittest.main()
