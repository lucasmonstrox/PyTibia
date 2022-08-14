import numpy as np
from battleList.core import getCreatureSlotImg
import utils.image


# TODO: test all slots using different creatures
def test_should_assert_slots():
    firstSlot = utils.image.loadAsArray(
        'battleList/tests/core/getCreatureSlotImg/firstSlot.png')
    secondSlot = utils.image.loadAsArray(
        'battleList/tests/core/getCreatureSlotImg/secondSlot.png')
    lastSlot = utils.image.loadAsArray(
        'battleList/tests/core/getCreatureSlotImg/lastSlot.png')
    content = utils.image.loadAsArray(
        'battleList/tests/core/getCreatureSlotImg/content.png')
    firstSlotAfterExtraction = getCreatureSlotImg(content, 0)
    secondSlotAfterExtraction = getCreatureSlotImg(content, 1)
    lastSlotAfterExtraction = getCreatureSlotImg(content, 43)
    np.testing.assert_array_equal(firstSlot, firstSlotAfterExtraction)
    np.testing.assert_array_equal(secondSlot, secondSlotAfterExtraction)
    np.testing.assert_array_equal(lastSlot, lastSlotAfterExtraction)
