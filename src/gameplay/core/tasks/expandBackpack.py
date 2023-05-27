from src.repositories.inventory.core import images
from src.shared.typings import GrayImage
from src.utils.core import locate
from src.utils.mouse import mouseDrag
from ...typings import Context
from .common.base import BaseTask


class ExpandBackpackTask(BaseTask):
    def __init__(self, backpackBarImage: GrayImage):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.terminable = False
        self.name = 'expandBackpack'
        self.value = backpackBarImage

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackBarPosition = locate(context['screenshot'], self.value, confidence=0.8)
        y0 = backpackBarPosition[1]
        croppedImage = context['screenshot'][y0:, backpackBarPosition[0]:]
        backpackBottomBarPosition = locate(croppedImage, images['containersBars']['backpack bottom'], confidence=0.8)
        backpackBottomBarPositionX = backpackBottomBarPosition[0] + backpackBarPosition[0]
        backpackBottomBarPositionY = backpackBottomBarPosition[1] + backpackBarPosition[1]
        yDifference = backpackBottomBarPositionY - backpackBarPosition[1]
        scrollY = 208 - yDifference
        if scrollY <= 0:
            self.terminable = True
            return context
        mouseDrag(backpackBottomBarPositionX, backpackBottomBarPositionY, backpackBottomBarPositionX, backpackBottomBarPositionY + scrollY)
        return context

    # TODO: add unit tests
    # TODO: check if backpack is expanded
    def did(self, context: Context) -> bool:
        return True
