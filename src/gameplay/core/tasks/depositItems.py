from src.repositories.inventory.core import images
from src.shared.typings import Waypoint
from ...typings import Context
from .common.vector import VectorTask
from .closeContainer import CloseContainerTask
from .dragItems import DragItemsTask
from .dropBackpackIntoStash import DropBackpackIntoStashTask
from .goToFreeDepot import GoToFreeDepotTask
from .openBackpack import OpenBackpackTask
from .openDepot import OpenDepotTask
from .openLocker import OpenLockerTask
from .scrollToItem import ScrollToItemTask
from .setNextWaypoint import SetNextWaypointTask


class DepositItemsTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'depositItems'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.waypoint = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def initialize(self, context: Context):
        self.tasks = [
            GoToFreeDepotTask(context, self.waypoint).setParentTask(self),
            OpenLockerTask().setParentTask(self),
            OpenBackpackTask(context['backpacks']['main']).setParentTask(self),
            ScrollToItemTask(images['containersBars'][context['backpacks']['main']], images['slots'][context['backpacks']['loot']]).setParentTask(self),
            DropBackpackIntoStashTask(context['backpacks']['loot']).setParentTask(self),
            OpenDepotTask().setParentTask(self),
            OpenBackpackTask(context['backpacks']['loot']).setParentTask(self),
            DragItemsTask(images['containersBars'][context['backpacks']['loot']], images['slots']['depot chest 2']).setParentTask(self),
            CloseContainerTask(images['containersBars'][context['backpacks']['loot']]).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
