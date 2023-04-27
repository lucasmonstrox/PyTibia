from typing import Tuple
from ..tasks.selectChatTab import SelectChatTabTask


# TODO: add unit tests
def makeSelectChatTabTask(tabName: str) -> Tuple[str, SelectChatTabTask]:
    task = SelectChatTabTask(tabName)
    return ('selectChatTab', task)