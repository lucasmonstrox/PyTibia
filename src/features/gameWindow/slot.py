from src.shared.typings import BBox, Slot
import pyautogui


# TODO: add unit tests
# TODO: add perf
def getSlotPosition(slot: Slot, gameWindowPosition: BBox) -> Slot:
    (gameWindowPositionX, gameWindowPositionY, gameWindowWidth, gameWindowHeight) = gameWindowPosition
    (slotX, slotY) = slot
    slotHeight = gameWindowHeight // 11
    slotWidth = gameWindowWidth // 15
    slotXCoordinate = gameWindowPositionX + (slotX * slotWidth)
    slotYCoordinate = gameWindowPositionY + (slotY * slotHeight)
    return (slotXCoordinate, slotYCoordinate)


# TODO: add unit tests
# TODO: add perf
def moveToSlot(slot: Slot, gameWindowPosition: BBox):
    slotXCoordinate, slotYCoordinate = getSlotPosition(slot, gameWindowPosition)
    pyautogui.moveTo(slotXCoordinate, slotYCoordinate)


# TODO: add unit tests
# TODO: add perf
def clickSlot(slot: Slot, gameWindowPosition: BBox):
    moveToSlot(slot, gameWindowPosition)
    pyautogui.click()


# TODO: add unit tests
# TODO: add perf
def rightClickSlot(slot: Slot, gameWindowPosition: BBox):
    moveToSlot(slot, gameWindowPosition)
    pyautogui.rightClick()

