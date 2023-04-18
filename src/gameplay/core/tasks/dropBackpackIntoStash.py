from src.features.inventory.core import images
from src.utils.core import locate
from src.utils.mouse import mouseDrag
from ...typings import Context
from .baseTask import BaseTask


# TODO: there is not way to check if items was moved to stash. try it soon
class DropBackpackIntoStashTask(BaseTask):
    def __init__(self, backpack):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'dropBackpackIntoStash'
        self.value = backpack

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackPosition = locate(context['screenshot'], images['slots'][self.value], confidence=0.8)
        stashPosition = locate(context['screenshot'], images['slots']['stash'])
        mouseDrag(backpackPosition[0], backpackPosition[1], stashPosition[0], stashPosition[1])
        return context
