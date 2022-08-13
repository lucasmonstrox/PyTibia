import unittest
from battleList.core import getContainerTopBarPos
import utils.image


class TestGetContainerTopBarPos(unittest.TestCase):
    def test_should_assert_content(self):
        screenshot = utils.image.loadAsArray(
            'battleList/tests/core/getContainerTopBarPos/screenshot.png')
        containerTopBarPos = getContainerTopBarPos(screenshot)
        self.assertEqual(containerTopBarPos, (1572, 25, 81, 13))


if __name__ == '__main__':
    unittest.main()
