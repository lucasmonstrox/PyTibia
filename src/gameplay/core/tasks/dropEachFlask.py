import time
from src.repositories.gameWindow.slot import getSlotPosition
from src.repositories.inventory.config import slotsImagesHashes
from src.repositories.inventory.core import images
from src.shared.typings import Slot
from src.utils.core import hashit, locate
from src.utils.mouse import drag
from ...typings import Context
from .common.base import BaseTask


class DropEachFlaskTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.name = 'dropEachFlask'
        self.delayOfTimeout = 1
        self.terminable = False
        self.slotIndex = 0
        self.backpack = backpack

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        (item, position) = self.getSlot(context, self.slotIndex)
        # TODO: also check if item is next backpack
        if item is None:
            self.slotIndex += 1
            return context
        if item == 'empty slot':
            self.terminable = True
            return context
        slotPosition = getSlotPosition((7, 5), context['gameWindow']['coordinate'])
        drag((position[0], position[1]), slotPosition)
        time.sleep(1)
        return context

    # TODO: add unit tests
    def getSlot(self, context: Context, slotIndex: int) -> Slot:
        backpackBarPosition = locate(context['screenshot'], images['containersBars'][self.backpack], confidence=0.8)
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
