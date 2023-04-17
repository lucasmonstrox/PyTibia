import pyautogui


def getSlotPos(slot, hudPos):
    (hudPosX, hudPosY, hudWidth, hudHeight) = hudPos
    (slotX, slotY) = slot
    slotHeight = hudHeight // 11
    slotWidth = hudWidth // 15
    slotXCoordinate = hudPosX + (slotX * slotWidth)
    slotYCoordinate = hudPosY + (slotY * slotHeight)
    return (slotXCoordinate, slotYCoordinate)


def moveToSlot(slot, hudPos):
    slotXCoordinate, slotYCoordinate = getSlotPos(slot, hudPos)
    pyautogui.moveTo(slotXCoordinate, slotYCoordinate)


def clickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.click()


def rightClickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.rightClick()

