import pyautogui
from time import time
from refill.core import getTradeTopPos


class CloseNpcTradeBoxTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.delayOfTimeout = None
        self.name = 'closeNpcTradeBox'
        self.status = 'notStarted'
        self.value = None

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        tradeTopPos = getTradeTopPos(context['screenshot'])
        if tradeTopPos is None:
            return context
        (x, y, _, _) = tradeTopPos
        closeIconX = x + 165
        closeIconY = y + 7
        pyautogui.click(closeIconX, closeIconY)
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
