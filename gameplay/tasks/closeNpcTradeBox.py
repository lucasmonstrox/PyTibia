import pyautogui
from refill.core import getTradeTopPos
from utils.mouse import leftClick
from .baseTask import BaseTask


class CloseNpcTradeBoxTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'closeNpcTradeBox'
        self.value = None

    def do(self, context):
        tradeTopPos = getTradeTopPos(context['screenshot'])
        if tradeTopPos is None:
            return context
        (x, y, _, _) = tradeTopPos
        closeIconX = x + 165
        closeIconY = y + 7
        leftClick(closeIconX, closeIconY)
        return context
