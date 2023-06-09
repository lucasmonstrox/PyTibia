import pathlib
import cv2
import numpy as np
import pytest

from src.repositories.gameWindow.core import getLeftArrowPosition, getRightArrowPosition

from tests.utils import result_pos_draw


currentPath = pathlib.Path(__file__).parent.resolve()
img01 = f'{currentPath}/screenshot01.png'
img02_gray = f'{currentPath}/screenshot02_gray.png'
img03 = f'{currentPath}/screenshot03.png'
img04 = f'{currentPath}/screenshot04.png'


def rgb_to_gray(img_path: str, is_gray=False):
    img = cv2.imread(img_path)
    if is_gray:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    else:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)


@pytest.mark.parametrize("img, is_gray", [
    (img01, False),
    (img02_gray, True),
    (img03, False),
    (img04, False),
])
def test_getLeftArrowPosition(mocker, img, is_gray):
    # clean preview test
    this_gameWindowCache = {
        'left': {'arrow': None, 'position': None},
        'right': {'arrow': None, 'position': None},
        }
    mocker.patch('src.repositories.gameWindow.core.get_global_game_cache_window_cache', return_value=this_gameWindowCache)
    # ----------------------------------
    img_gray = rgb_to_gray(img, is_gray)
    result = getLeftArrowPosition(img_gray)
    assert result is not None
    assert result == (2, 23, 7, 54)


@pytest.mark.parametrize("img, is_gray", [
    (img01, False),
    (img02_gray, True),
    (img03, False),
])
def test_getRightArrowPosition(mocker, img, is_gray):
    # clean preview test
    this_gameWindowCache = {
        'left': {'arrow': None, 'position': None},
        'right': {'arrow': None, 'position': None},
        }
    mocker.patch('src.repositories.gameWindow.core.get_global_game_cache_window_cache', return_value=this_gameWindowCache)
    # ----------------------------------
    img_gray = rgb_to_gray(img, is_gray)
    result = getRightArrowPosition(img_gray)
    # result == x, y, width, height
    assert result is not None
    # img04 should be differrent
    result_pos_draw(img_gray,result,f"test_getRightArrowPosition__{img[-15:]}")
    assert result == (1561, 23, 7, 54)

def test_getRightArrowPosition_04(mocker, img=img04, is_gray=False):
    # clean preview test
    this_gameWindowCache = {
        'left': {'arrow': None, 'position': None},
        'right': {'arrow': None, 'position': None},
        }
    mocker.patch('src.repositories.gameWindow.core.get_global_game_cache_window_cache', return_value=this_gameWindowCache)
    # ----------------------------------

    from src.repositories.gameWindow.config import gameWindowCache

    img_gray = rgb_to_gray(img, is_gray)
    result = getRightArrowPosition(img_gray)
    # result == x, y, width, height
    assert result is not None
    # img04 should be differrent
    result_pos_draw(img_gray,result,"test_getRightArrowPosition__04.png")
    assert result == (1385, 23, 7, 54)