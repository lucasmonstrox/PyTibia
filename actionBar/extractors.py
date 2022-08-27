from .locators import getLeftSideArrowsPos, getRightSideArrowsPos


def getCooldownsImg(screenshot):
    (x0, y0, _, _) = getLeftSideArrowsPos(screenshot)
    (x1, _, _, _) = getRightSideArrowsPos(screenshot)
    cooldownsImg = screenshot[y0 + 37:y0 + 37 + 22, x0:x1]
    return cooldownsImg
