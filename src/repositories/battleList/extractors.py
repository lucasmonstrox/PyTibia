from numba import njit
import numpy as np
from typing import Union
from src.shared.typings import GrayImage
from .locators import getContainerBottomBarPosition, getBattleListIconPosition


# PERF: [0.05485419999999941, 4.39999999990448e-06]
def getContent(screenshot: GrayImage) -> Union[GrayImage, None]:
    battleListIconPosition = getBattleListIconPosition(screenshot)
    if battleListIconPosition is None:
        return None
    content = screenshot[battleListIconPosition[1] + battleListIconPosition[3] +
                         1:, battleListIconPosition[0] - 1:battleListIconPosition[0] - 1 + 156]
    containerBottomBarPos = getContainerBottomBarPosition(content)
    if containerBottomBarPos is None:
        return None
    return content[:containerBottomBarPos[1] - 11, :]


# PERF: [0.8151709999999994, 1.1999999999900979e-05]
# TODO: add unit tests
@njit(cache=True, fastmath=True, boundscheck=False)
def getCreaturesNamesImages(content: GrayImage, filledSlotsCount: int) -> GrayImage:
    creaturesNamesImages = np.zeros((filledSlotsCount, 115), dtype=np.uint8)
    for i in range(filledSlotsCount):
        y = 11 + (i * 22)
        creatureNameImage = content[y:y + 1, 23:138][0]
        for j in range(creatureNameImage.shape[0]):
            if creatureNameImage[j] == 192 or creatureNameImage[j] == 247:
                creaturesNamesImages[i, j] = 192
    return creaturesNamesImages
