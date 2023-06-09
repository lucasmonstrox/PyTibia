from src.repositories.inventory.core import images
import src.utils.core as coreUtils
import src.utils.mouse as mouseUtils
from ...typings import Context
from .common.base import BaseTask


# TODO: by cap, is possible to detect if task was did. But it can happen that the backpack is empty.
class DropBackpackIntoStashTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.name = 'dropBackpackIntoStash'
        self.delayAfterComplete = 1
        self.backpack = backpack

    def do(self, context: Context) -> Context:
        backpackPosition = coreUtils.locate(context['screenshot'], images['slots'][self.backpack], confidence=0.8)
        stashPosition = coreUtils.locate(context['screenshot'], images['slots']['stash'])
        mouseUtils.drag((backpackPosition[0], backpackPosition[1]), (stashPosition[0], stashPosition[1]))
        return context
