from typing import Tuple
from ...typings import Context
from ..tasks.singleWalkPress import SingleWalkPressTask


# TODO: add unit tests
# TODO: add typings
def makeSingleWalkPress(context: Context, waypoint) -> Tuple[str, SingleWalkPressTask]:
    task = SingleWalkPressTask(context, waypoint)
    return ('singleWalkPress', task)