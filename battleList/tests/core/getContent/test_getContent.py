import numpy as np
from battleList.core import getContent
import utils.image


def test_should_assert_content():
    screenshot = utils.image.loadAsArray(
        'battleList/tests/core/getContent/screenshot.png')
    emptyContent = utils.image.loadAsArray(
        'battleList/tests/core/getContent/emptyContent.png')
    content = getContent(screenshot)
    np.testing.assert_allclose(content, emptyContent, atol=1)
