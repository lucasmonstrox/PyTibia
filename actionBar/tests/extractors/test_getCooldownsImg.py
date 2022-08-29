import numpy as np
import pathlib
from actionBar.extractors import getCooldownsImg
from utils.image import load, RGBtoGray


def test_should_get_left_side_arrows_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    cooldownsImg = RGBtoGray(load(f'{currentPath}/cooldownsImg.png'))
    cooldownsImgAfterExtraction = getCooldownsImg(screenshotImg)
    np.testing.assert_array_equal(cooldownsImg, cooldownsImgAfterExtraction)
