from .locators import getLeftSideArrowsPos, getRightSideArrowsPos


def getCooldownsImg(screenshot):
    leftSideArrowsPos = getLeftSideArrowsPos(screenshot)
    cannotGetLeftSideArrowsPos = leftSideArrowsPos is None
    if cannotGetLeftSideArrowsPos:
        return None
    (x0, y0, _, _) = leftSideArrowsPos
    rightSideArrowsPos = getRightSideArrowsPos(screenshot)
    cannotGetRightSideArrowsPos = rightSideArrowsPos is None
    if cannotGetRightSideArrowsPos:
        return None
    (x1, _, _, _) = rightSideArrowsPos
    cooldownsImg = screenshot[y0 + 37: y0 + 37 + 22, x0:x1]
    return cooldownsImg
