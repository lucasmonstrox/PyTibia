from typing import Tuple
from ..tasks.openLocker import OpenLockerTask


# TODO: add unit tests
def makeOpenLockerTask() -> Tuple[str, OpenLockerTask]:
    task = OpenLockerTask()
    return ('openLockerTask', task)
