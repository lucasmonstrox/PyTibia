from gameplay.tasks.setChatOff import SetChatOffTask


def makeSetChatOffTask():
    task = SetChatOffTask()
    return ('setChatOff', task)
