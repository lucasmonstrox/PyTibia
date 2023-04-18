import numpy as np
from src.features.inventory.core import images
from src.shared.typings import Waypoint
from ...typings import Context
from ..factories.makeCloseContainer import makeCloseContainerTask
from ..factories.makeDragItems import makeDragItemsTask
from ..factories.makeDropBackpackIntoStash import makeDropBackpackIntoStashTask
from ..factories.makeGoToFreeDepot import makeGoToFreeDepotTask
from ..factories.makeOpenBackpack import makeOpenBackpackTask
from ..factories.makeOpenDepot import makeOpenDepotTask
from ..factories.makeOpenLocker import makeOpenLockerTask
from ..factories.makeScrollToItem import makeScrollToItemTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class DepositItemsTask(GroupTaskExecutor):
    def __init__(self, context, waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'depositItems'
        self.tasks = self.generateTasks(context, waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, context: Context, waypoint: Waypoint):
        return np.array([
            makeGoToFreeDepotTask(context, waypoint),
            makeOpenLockerTask(),
            makeOpenBackpackTask(context['backpacks']['main']),
            makeScrollToItemTask(images['containersBars'][context['backpacks']['main']], images['slots'][context['backpacks']['loot']]),
            makeDropBackpackIntoStashTask(context['backpacks']['loot']),
            makeOpenDepotTask(),
            makeOpenBackpackTask(context['backpacks']['loot']),
            makeDragItemsTask(images['containersBars'][context['backpacks']['loot']], images['slots']['depot chest 2']),
            makeCloseContainerTask(images['containersBars'][context['backpacks']['loot']]),
            makeSetNextWaypointTask(),
        ], dtype=Task)
