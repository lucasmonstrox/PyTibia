from ..tasks.closeNpcTradeBox import CloseNpcTradeBoxTask


def makeCloseNpcTradeBoxTask():
    task = CloseNpcTradeBoxTask()
    return ('closeNpcTradeBox', task)
