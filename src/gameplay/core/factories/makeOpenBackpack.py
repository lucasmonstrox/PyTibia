from typing import Tuple
from ..tasks.openBackpack import OpenBackpackTask


# TODO: add unit tests
def makeOpenBackpackTask(backpack: str) -> Tuple[str, OpenBackpackTask]:
    task = OpenBackpackTask(backpack)
    return ('openBackpack', task)
