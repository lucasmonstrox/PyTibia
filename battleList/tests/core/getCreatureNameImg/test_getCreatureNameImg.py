import numpy as np
import unittest
from battleList.core import getCreatureNameImg
import utils.image


class TestGetCreatureNameImg(unittest.TestCase):
    def test_should_get_Rat_img(self):
        slotImg = utils.image.loadAsArray(
            'battleList/tests/core/getCreatureNameImg/slotImg.png')
        ratNameImg = utils.image.loadAsArray(
            'battleList/images/monsters/Rat.png')
        creatureNameImg = getCreatureNameImg(slotImg)
        np.testing.assert_array_equal(creatureNameImg, ratNameImg)


if __name__ == '__main__':
    unittest.main()
