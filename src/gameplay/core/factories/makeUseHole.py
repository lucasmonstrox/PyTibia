from typing import Tuple
from ..tasks.useHole import UseHoleTask


# TODO: add unit tests
# TODO: add typings
def makeUseHoleTask(waypoint) -> Tuple[str, UseHoleTask]:
    task = UseHoleTask(waypoint)
    return ('useHole', task)
