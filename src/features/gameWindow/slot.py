import pyautogui


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getSlotPos(slot, gameWindowPos):
    (gameWindowPosX, gameWindowPosY, gameWindowWidth, gameWindowHeight) = gameWindowPos
    (slotX, slotY) = slot
    slotHeight = gameWindowHeight // 11
    slotWidth = gameWindowWidth // 15
    slotXCoordinate = gameWindowPosX + (slotX * slotWidth)
    slotYCoordinate = gameWindowPosY + (slotY * slotHeight)
    return (slotXCoordinate, slotYCoordinate)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def moveToSlot(slot, gameWindowPos):
    slotXCoordinate, slotYCoordinate = getSlotPos(slot, gameWindowPos)
    pyautogui.moveTo(slotXCoordinate, slotYCoordinate)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def clickSlot(slot, gameWindowPos):
    moveToSlot(slot, gameWindowPos)
    pyautogui.click()


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def rightClickSlot(slot, gameWindowPos):
    moveToSlot(slot, gameWindowPos)
    pyautogui.rightClick()

