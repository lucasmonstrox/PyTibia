import numpy as np
import pathlib
from src.repositories.radar.extractors import getRadarImage
from src.utils.image import loadFromRGBToGray


def test_should_get_radar_img():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = loadFromRGBToGray(f'{currentPath}/screenshot.png')
    expectedRadarImg = loadFromRGBToGray(f'{currentPath}/radarImg.png')
    radarToolsPos = (1870, 78, 20, 60)
    radarImg = getRadarImage(screenshot, radarToolsPos)
    np.testing.assert_array_equal(radarImg, expectedRadarImg)
