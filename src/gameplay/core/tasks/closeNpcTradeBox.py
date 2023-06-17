import src.repositories.refill.core as refillCore
import src.utils.mouse as mouse
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
        tradeTopPosition = refillCore.getTradeTopPosition(
            context['screenshot'])
        if tradeTopPosition is None:
            return context
        mouse.leftClick((tradeTopPosition[0] + 165, tradeTopPosition[1] + 7))
        return context
