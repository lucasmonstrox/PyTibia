from src.gameplay.typings import Context
from src.repositories.refill.core import buyItem
from ...typings import Context
from .common.base import BaseTask


class BuyItemTask(BaseTask):
    def __init__(self, itemName: str, itemQuantity: str):
        super().__init__()
        self.name = 'buyItem'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.itemName = itemName
        self.itemQuantity = itemQuantity

    # TODO: add unit tests
    def shouldIgnore(self, _: Context) -> bool:
        shouldIgnoreTask = self.itemQuantity <= 0
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        # TODO: split into multiple tasks
        buyItem(context['screenshot'], self.itemName, self.itemQuantity)
        return context

    # TODO: check if item was bought checking gold difference
    def did(self, _: Context) -> bool:
        return True
