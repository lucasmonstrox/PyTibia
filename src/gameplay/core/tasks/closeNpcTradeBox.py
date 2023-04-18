from src.features.refill.core import getTradeTopPos
from src.utils.mouse import leftClick
from ...typings import Context
from .baseTask import BaseTask


# TODO: check if npc tradebox was closed
class CloseNpcTradeBoxTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'closeNpcTradeBox'
        self.value = None

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        tradeTopPos = getTradeTopPos(context['screenshot'])
        if tradeTopPos is None:
            return context
        (x, y, _, _) = tradeTopPos
        closeIconX = x + 165
        closeIconY = y + 7
        leftClick(closeIconX, closeIconY)
        return context
