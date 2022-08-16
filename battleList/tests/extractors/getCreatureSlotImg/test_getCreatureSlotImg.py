import numpy as np
import pathlib
from battleList.extractors import getCreatureSlotImg
import utils.image


# TODO: test all slots using different creatures
def test_should_assert_creature_slots_images():
    currentPath = pathlib.Path(__file__).parent.resolve()
    firstSlot = utils.image.loadAsGrey(f'{currentPath}/firstSlot.png')
    secondSlot = utils.image.loadAsGrey(f'{currentPath}/secondSlot.png')
    lastSlot = utils.image.loadAsGrey(f'{currentPath}/lastSlot.png')
    content = utils.image.loadAsGrey(f'{currentPath}/content.png')
    firstSlotAfterExtraction = getCreatureSlotImg(content, 0)
    secondSlotAfterExtraction = getCreatureSlotImg(content, 1)
    lastSlotAfterExtraction = getCreatureSlotImg(content, 43)
    np.testing.assert_array_equal(firstSlot, firstSlotAfterExtraction)
    np.testing.assert_array_equal(secondSlot, secondSlotAfterExtraction)
    np.testing.assert_array_equal(lastSlot, lastSlotAfterExtraction)
