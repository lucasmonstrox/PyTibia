from typing import Tuple
from ..tasks.openDepot import OpenDepotTask


# TODO: add unit tests
def makeOpenDepotTask() -> Tuple[str, OpenDepotTask]:
    task = OpenDepotTask()
    return ('openDepot', task)
