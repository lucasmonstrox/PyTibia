from src.repositories.refill.core import getTradeTopPos
from src.utils.mouse import leftClick
from ...typings import Context
from .common.base import BaseTask


# TODO: check if npc tradebox was closed
class CloseNpcTradeBoxTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'closeNpcTradeBox'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        tradeTopPos = getTradeTopPos(context['screenshot'])
        if tradeTopPos is None:
            return context
        leftClick((tradeTopPos[0] + 165, tradeTopPos[1] + 7))
        return context
