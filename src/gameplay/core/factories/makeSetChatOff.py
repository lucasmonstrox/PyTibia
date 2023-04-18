from typing import Tuple
from ..tasks.setChatOff import SetChatOffTask


# TODO: add unit tests
def makeSetChatOffTask() -> Tuple[str, SetChatOffTask]:
    task = SetChatOffTask()
    return ('setChatOff', task)
