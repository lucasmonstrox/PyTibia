from typing import Tuple
from ..tasks.expandBackpack import ExpandBackpackTask


# TODO: add unit tests
def makeExpandBackpackTask(backpack: str) -> Tuple[str, ExpandBackpackTask]:
    task = ExpandBackpackTask(backpack)
    return ('expandBackpack', task)
