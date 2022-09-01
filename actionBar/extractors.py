import actionBar.locators


def getCooldownsImg(screenshot):
    leftSideArrowsPos = actionBar.locators.getLeftSideArrowsPos(screenshot)
    cannotGetLeftSideArrowsPos = leftSideArrowsPos is None
    if cannotGetLeftSideArrowsPos:
        return None
    (x0, y0, _, _) = leftSideArrowsPos
    rightSideArrowsPos = actionBar.locators.getRightSideArrowsPos(screenshot)
    cannotGetRightSideArrowsPos = rightSideArrowsPos is None
    if cannotGetRightSideArrowsPos:
        return None
    (x1, _, _, _) = rightSideArrowsPos
    cooldownsImg = screenshot[y0 + 37: y0 + 37 + 22, x0:x1]
    return cooldownsImg
