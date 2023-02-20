from time import time
from refill import core
from .baseTask import BaseTask


class BuyItemTask(BaseTask):
    def __init__(self, itemNameWithQuantity):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'buyItem'
        self.value = itemNameWithQuantity

    def do(self, context):
        core.buyItem(context['screenshot'], self.value)
        return context
