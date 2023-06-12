from src.repositories.inventory.config import images
from src.repositories.inventory.core import isBackpackOpen
from src.utils.core import locate
from src.utils.mouse import rightClick
from ...typings import Context
from .common.base import BaseTask


class OpenBackpackTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.name = 'openBackpack'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.backpack = backpack

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = isBackpackOpen(context['screenshot'], self.backpack)
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackPosition = locate(context['screenshot'], images['slots'][self.backpack], confidence=0.8)
        if backpackPosition is None:
            return context
        # TODO: click in random BBOX coordinate
        rightClick((backpackPosition[0] + 5, backpackPosition[1] + 5))
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        return isBackpackOpen(context['screenshot'], self.backpack)
