from typing import Tuple
from ...typings import Context
from ..tasks.walk import WalkTask


# TODO: add unit tests
# TODO: add typings
def makeWalkTask(context: Context, waypoint) -> Tuple[str, WalkTask]:
    task = WalkTask(context, waypoint)
    return ('walk', task)