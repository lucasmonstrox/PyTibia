from typing import Tuple
from src.shared.typings import Waypoint
from ..tasks.useRope import UseRopeTask


# TODO: add unit tests
def makeUseRopeTask(waypoint: Waypoint) -> Tuple[str, UseRopeTask]:
    task = UseRopeTask(waypoint)
    return ('useRope', task)
