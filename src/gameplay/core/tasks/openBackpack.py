from src.repositories.inventory.config import images
import src.repositories.inventory.core as inventoryCore
import src.utils.core as utilsCore
import src.utils.mouse as utilsMouse
from ...typings import Context
from .common.base import BaseTask


class OpenBackpackTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.name = 'openBackpack'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.backpack = backpack

    def shouldIgnore(self, context: Context) -> bool:
        return inventoryCore.isContainerOpen(context['screenshot'], self.backpack)

    def do(self, context: Context) -> Context:
        backpackPosition = utilsCore.locate(
            context['screenshot'], images['slots'][self.backpack], confidence=0.75)
        if backpackPosition is None:
            return context
        # TODO: click in random BBOX coordinate
        utilsMouse.rightClick(
            (backpackPosition[0] + 5, backpackPosition[1] + 5))
        return context

    def did(self, context: Context) -> bool:
        return self.shouldIgnore(context)
