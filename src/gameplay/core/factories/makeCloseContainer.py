from typing import Tuple
from ..tasks.closeContainer import CloseContainerTask


# TODO: add unit tests
def makeCloseContainerTask(containerBarImage) -> Tuple[str, CloseContainerTask]:
    task = CloseContainerTask(containerBarImage)
    return ('closeContainer', task)
