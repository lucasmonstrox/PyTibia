import numpy as np
import unittest
from battleList.core import getContent
import utils.image


class TestGetContent(unittest.TestCase):
    def test_should_assert_content(self):
        screenshot = utils.image.loadAsArray(
            'battleList/tests/core/getContent/screenshot.png')
        emptyContent = utils.image.loadAsArray(
            'battleList/tests/core/getContent/emptyContent.png')
        content = getContent(screenshot)
        np.testing.assert_allclose(emptyContent, content, atol=1)


if __name__ == '__main__':
    unittest.main()
