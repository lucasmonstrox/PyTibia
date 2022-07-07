import pyautogui


def moveToSlot(slot, hudPos):
    (hudPosX, hudPosY, hudWidth, hudHeight) = hudPos
    (slotX, slotY) = slot
    slotHeight = hudHeight // 11
    slotWidth = hudWidth // 15
    slotXCoordinate = hudPosX + (slotX * slotWidth)
    slotYCoordinate = hudPosY + (slotY * slotHeight)
    pyautogui.moveTo(slotXCoordinate, slotYCoordinate, duration=0.1)


def clickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.click()


def rightClickSlot(slot, hudPos):
    moveToSlot(slot, hudPos)
    pyautogui.rightClick()

