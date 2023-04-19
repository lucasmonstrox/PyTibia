from typing import Tuple
from src.shared.typings import Waypoint
from ..tasks.useShovel import UseShovelTask


# TODO: add unit tests
def makeUseShovelTask(waypoint: Waypoint) -> Tuple[str, UseShovelTask]:
    task = UseShovelTask(waypoint)
    return ('useShovel', task)
