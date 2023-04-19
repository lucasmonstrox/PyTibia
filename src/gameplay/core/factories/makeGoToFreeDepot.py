from typing import Tuple
from src.shared.typings import Waypoint
from ...typings import Context
from ..tasks.goToFreeDepot import GoToFreeDepotTask


# TODO: add unit tests
def makeGoToFreeDepotTask(context: Context, waypoint: Waypoint) -> Tuple[str, GoToFreeDepotTask]:
    task = GoToFreeDepotTask(context, waypoint)
    return ('goToFreeDepot', task)
