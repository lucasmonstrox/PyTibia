import time
from src.features.gameWindow.slot import getSlotPosition
from src.features.inventory.config import slotsImagesHashes
from src.features.inventory.core import images
from src.shared.typings import Slot
from src.utils.core import hashit, locate
from src.utils.mouse import mouseDrag
from ...typings import Context
from .baseTask import BaseTask


class DropEachFlaskTask(BaseTask):
    def __init__(self, backpack):
        super().__init__()
        self.delayOfTimeout = 1
        self.name = 'dropEachFlask'
        self.terminable = False
        self.value = backpack
        self.slotIndex = 0

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        (item, position) = self.getSlot(context, self.slotIndex)
        if item is None:
            self.slotIndex += 1
            return context
        if item == 'empty slot':
            self.terminable = True
            return context
        slotPosX, slotPosY = getSlotPosition((7, 5), context['gameWindow']['coordinate'])
        mouseDrag(position[0], position[1], slotPosX, slotPosY)
        time.sleep(1)
        return context

    # TODO: add unit tests
    def getSlot(self, context: Context, slotIndex: int) -> Slot:
        backpackBarPosition = locate(context['screenshot'], images['containersBars'][self.value], confidence=0.8)
        if backpackBarPosition is None:
            return (None, (0, 0))
        slotXIndex = slotIndex % 4
        slotYIndex = slotIndex // 4
        containerPositionX, containerPositionY = backpackBarPosition[1] + 18, backpackBarPosition[0] + 10
        y0 = containerPositionX + slotYIndex * 32 + slotYIndex * 5
        y1 = y0 + 21 
        x0 = containerPositionY + slotXIndex * 32 + slotXIndex * 5
        x1 = x0 + 32
        firstSlotImage = context['screenshot'][y0:y1, x0:x1]
        firstSlotImageHash = hashit(firstSlotImage)
        item = slotsImagesHashes.get(firstSlotImageHash, None)
        return (item, (x0 + 16, y0 + 16))
