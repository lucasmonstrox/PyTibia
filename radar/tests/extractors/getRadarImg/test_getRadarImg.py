import numpy as np
import pathlib
from radar.extractors import getRadarImg
import utils.image
import utils.core


def test_should_get_radar_img():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = utils.image.loadAsGrey(f'{currentPath}/screenshot.png')
    expectedRadarImg = utils.image.loadAsGrey(f'{currentPath}/radarImg.png')
    radarToolsPos = (1870, 78, 20, 60)
    radarImg = getRadarImg(screenshot, radarToolsPos)
    np.testing.assert_array_equal(radarImg, expectedRadarImg)
