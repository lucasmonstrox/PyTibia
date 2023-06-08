from src.repositories.inventory.core import images
from src.utils.core import locate
from src.utils.mouse import drag
from ...typings import Context
from .common.base import BaseTask


# TODO: there is not way to check if items was moved to stash. try it soon
class DropBackpackIntoStashTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.name = 'dropBackpackIntoStash'
        self.delayAfterComplete = 1
        self.backpack = backpack

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackPosition = locate(context['screenshot'], images['slots'][self.backpack], confidence=0.8)
        stashPosition = locate(context['screenshot'], images['slots']['stash'])
        drag((backpackPosition[0], backpackPosition[1]), (stashPosition[0], stashPosition[1]))
        return context
