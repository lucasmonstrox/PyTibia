from typing import Tuple
from src.shared.typings import Waypoint
from ...typings import Context
from ..tasks.walk import WalkTask


# TODO: add unit tests
def makeWalkTask(context: Context, waypoint: Waypoint) -> Tuple[str, WalkTask]:
    task = WalkTask(context, waypoint)
    return ('walk', task)