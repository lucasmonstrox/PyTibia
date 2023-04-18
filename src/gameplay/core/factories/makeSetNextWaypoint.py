from typing import Tuple
from ..tasks.setNextWaypoint import SetNextWaypointTask


# TODO: add unit tests
def makeSetNextWaypointTask() -> Tuple[str, SetNextWaypointTask]:
    task = SetNextWaypointTask()
    return ('setNextWaypoint', task)