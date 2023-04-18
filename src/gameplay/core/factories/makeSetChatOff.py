from ..tasks.setChatOff import SetChatOffTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeSetChatOffTask():
    task = SetChatOffTask()
    return ('setChatOff', task)
