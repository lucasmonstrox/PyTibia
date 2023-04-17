import numpy as np
from src.features.inventory.core import backpacksBarsImages, backpacksImages, depotChest2Image
from ..factories.makeCloseContainer import makeCloseContainerTask
from ..factories.makeDragItems import makeDragItemsTask
from ..factories.makeDropBackpackIntoStash import makeDropBackpackIntoStashTask
from ..factories.makeGoToFreeDepot import makeGoToFreeDepotTask
from ..factories.makeOpenBackpack import makeOpenBackpackTask
from ..factories.makeOpenDepot import makeOpenDepotTask
from ..factories.makeOpenLocker import makeOpenLockerTask
from ..factories.makeScrollToItem import makeScrollToItemTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class DepositItemsTask(GroupTaskExecutor):
    def __init__(self, context, waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'depositItems'
        self.tasks = self.generateTasks(context, waypoint)
        self.value = waypoint

    def generateTasks(self, context, waypoint):
        return np.array([
            makeGoToFreeDepotTask(context, waypoint),
            makeOpenLockerTask(),
            makeOpenBackpackTask(context['backpacks']['main']),
            makeScrollToItemTask(backpacksBarsImages[context['backpacks']['main']], backpacksImages[context['backpacks']['loot']]),
            makeDropBackpackIntoStashTask(context['backpacks']['loot']),
            makeOpenDepotTask(),
            makeOpenBackpackTask(context['backpacks']['loot']),
            makeDragItemsTask(backpacksBarsImages[context['backpacks']['loot']], depotChest2Image),
            makeCloseContainerTask(backpacksBarsImages[context['backpacks']['loot']]),
            makeSetNextWaypointTask(),
        ], dtype=taskType)
