from typing import Tuple
from ...typings import Context
from ..tasks.goToFreeDepot import GoToFreeDepotTask


# TODO: add unit tests
# TODO: add typings
def makeGoToFreeDepotTask(context: Context, waypoint) -> Tuple[str, GoToFreeDepotTask]:
    task = GoToFreeDepotTask(context, waypoint)
    return ('goToFreeDepot', task)
