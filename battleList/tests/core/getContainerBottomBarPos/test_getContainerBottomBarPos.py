import unittest
from battleList.core import getContainerBottomBarPos
import utils.image


class TestGetContainerBottomBarPos(unittest.TestCase):
    def test_should_assert_content(self):
        screenshot = utils.image.loadAsArray(
            'battleList/tests/core/getContainerBottomBarPos/screenshot.png')
        containerBottomBarPos = getContainerBottomBarPos(screenshot)
        self.assertEqual(containerBottomBarPos, (1748, 584, 156, 4))


if __name__ == '__main__':
    unittest.main()
