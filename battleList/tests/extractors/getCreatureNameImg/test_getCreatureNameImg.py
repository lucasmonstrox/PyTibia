import numpy as np
import pathlib
from battleList.extractors import getCreatureNameImg
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_get_creature_name_img():
    slotImg = utils.image.loadAsArray(f'{currentPath}/slotImg.png')
    ratNameImg = utils.image.loadAsArray(f'{currentPath}/images/monsters/Rat.png')
    creatureNameImg = getCreatureNameImg(slotImg)
    np.testing.assert_array_equal(creatureNameImg, ratNameImg)
