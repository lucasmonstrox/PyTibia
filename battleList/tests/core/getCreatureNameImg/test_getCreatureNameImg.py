import numpy as np
from battleList.core import getCreatureNameImg
import utils.image


def test_should_get_creature_name_img():
    slotImg = utils.image.loadAsArray(
        'battleList/tests/core/getCreatureNameImg/slotImg.png')
    ratNameImg = utils.image.loadAsArray(
        'battleList/images/monsters/Rat.png')
    creatureNameImg = getCreatureNameImg(slotImg)
    np.testing.assert_array_equal(creatureNameImg, ratNameImg)
