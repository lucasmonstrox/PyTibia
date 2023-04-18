from typing import Tuple
from ..tasks.useShovel import UseShovelTask


# TODO: add unit tests
# TODO: add typings
def makeUseShovelTask(waypoint) -> Tuple[str, UseShovelTask]:
    task = UseShovelTask(waypoint)
    return ('useShovel', task)
