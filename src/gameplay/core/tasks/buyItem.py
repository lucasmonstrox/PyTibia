from src.repositories.refill.core import buyItem
from ...typings import Context
from .common.base import BaseTask


# TODO: check if item was bought
class BuyItemTask(BaseTask):
    # TODO: add types
    def __init__(self, itemNameWithQuantity):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'buyItem'
        self.value = itemNameWithQuantity

    # TODO: add unit tests
    def shouldIgnore(self, _: Context) -> bool:
        _, itemQuantity = self.value
        shouldIgnoreTask = itemQuantity <= 0
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        buyItem(context['screenshot'], self.value)
        return context
