from src.gameplay.typings import Context
from src.repositories.inventory.core import images
from src.shared.typings import GrayImage
from src.utils.core import locate
from src.utils.mouse import drag
from ...typings import Context
from .common.base import BaseTask


class ExpandBackpackTask(BaseTask):
    def __init__(self, backpackBarImage: GrayImage):
        super().__init__()
        self.name = 'expandBackpack'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.terminable = False
        self.backpackBarImage = backpackBarImage

    # TODO: ignore if backpack already expanded
    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        return super().shouldIgnore(context)

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        # TODO: locate should be done in right content position to avoid calculation in whole screen
        backpackBarPosition = locate(context['screenshot'], self.backpackBarImage, confidence=0.8)
        croppedImage = context['screenshot'][backpackBarPosition[1]:, backpackBarPosition[0]:]
        backpackBottomBarPosition = locate(croppedImage, images['containersBars']['backpack bottom'], confidence=0.8)
        backpackBottomBarPositionX = backpackBottomBarPosition[0] + backpackBarPosition[0]
        backpackBottomBarPositionY = backpackBottomBarPosition[1] + backpackBarPosition[1]
        yDifference = backpackBottomBarPositionY - backpackBarPosition[1]
        scrollY = 208 - yDifference
        if scrollY <= 0:
            self.terminable = True
            return context
        drag((backpackBottomBarPositionX, backpackBottomBarPositionY), (backpackBottomBarPositionX, backpackBottomBarPositionY + scrollY))
        return context

    # TODO: check if backpack is expanded
    # TODO: add unit tests
    def did(self, _: Context) -> bool:
        return True
