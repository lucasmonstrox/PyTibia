from typing import Tuple
from src.shared.typings import Waypoint
from ...typings import Context
from ..tasks.singleWalkPress import SingleWalkPressTask


# TODO: add unit tests
def makeSingleWalkPress(context: Context, waypoint: Waypoint) -> Tuple[str, SingleWalkPressTask]:
    task = SingleWalkPressTask(context, waypoint)
    return ('singleWalkPress', task)