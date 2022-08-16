import numpy as np
import pathlib
from battleList.extractors import getContent
import utils.image


def test_should_get_content():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshot = utils.image.loadAsGrey(f'{currentPath}/screenshot.png')
    emptyContent = utils.image.loadAsGrey(f'{currentPath}/emptyContent.png')
    content = getContent(screenshot)
    np.testing.assert_allclose(content, emptyContent, atol=1)
