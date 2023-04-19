from typing import Tuple
from src.shared.typings import Waypoint
from ..tasks.useHole import UseHoleTask


# TODO: add unit tests
def makeUseHoleTask(waypoint: Waypoint) -> Tuple[str, UseHoleTask]:
    task = UseHoleTask(waypoint)
    return ('useHole', task)
