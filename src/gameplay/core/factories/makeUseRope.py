from typing import Tuple
from ..tasks.useRope import UseRopeTask


# TODO: add unit tests
# TODO: add typings
def makeUseRopeTask(waypoint) -> Tuple[str, UseRopeTask]:
    task = UseRopeTask(waypoint)
    return ('useRope', task)
