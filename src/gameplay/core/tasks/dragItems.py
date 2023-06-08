import time
from src.gameplay.typings import Context
from src.gameplay.typings import Context
from src.repositories.inventory.core import images
from src.shared.typings import GrayImage
from src.utils.core import locate
from src.utils.mouse import drag, rightClick
from ...typings import Context
from .common.base import BaseTask


# TODO: check if item was moved on did. Is possible to check it by cap
class DragItemsTask(BaseTask):
    def __init__(self, containerBarImage: GrayImage, targetContainerImage: GrayImage):
        super().__init__()
        self.name = 'dragItems'
        self.terminable = False
        self.containerBarImage = containerBarImage
        self.targetContainerImage = targetContainerImage

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        containerBarPosition = locate(context['screenshot'], self.containerBarImage, confidence=0.8)
        firstSlotImage = context['screenshot'][containerBarPosition[1] + 18:containerBarPosition[1] + 18 + 32, containerBarPosition[0] + 10:containerBarPosition[0] + 10 + 32]
        isLootBackpackItem = locate(firstSlotImage, images['slots'][context['backpacks']['loot']], confidence=0.8) is not None
        if isLootBackpackItem:
            rightClick((containerBarPosition[0] + 12, containerBarPosition[1] + 20))
            return context
        isNotEmptySlot = locate(firstSlotImage, images['slots']['empty']) is None
        if isNotEmptySlot:
            targetContainerPosition = locate(context['screenshot'], self.targetContainerImage, confidence=0.8)
            fromX, fromY = containerBarPosition[0] + 12, containerBarPosition[1] + 20
            toX, toY = targetContainerPosition[0] + 2, targetContainerPosition[1] + 2
            drag((fromX, fromY), (toX, toY))
            time.sleep(0.2)
            return context
        self.terminable = True
        return context
