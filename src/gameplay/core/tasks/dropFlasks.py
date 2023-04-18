import numpy as np
from src.features.inventory.core import images
from ..factories.makeDropEachFlask import makeDropEachFlaskTask
from ..factories.makeExpandBackpack import makeExpandBackpackTask
from ..factories.makeOpenBackpack import makeOpenBackpackTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class DropFlasksTask(GroupTaskExecutor):
    def __init__(self, context):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'dropFlasks'
        self.tasks = self.generateTasks(context)

    def generateTasks(self, context):
        return np.array([
            makeOpenBackpackTask(context['backpacks']['main']),
            makeExpandBackpackTask(images['containersBars'][context['backpacks']['main']]),
            makeDropEachFlaskTask(context['backpacks']['main']),
            makeSetNextWaypointTask(),
        ], dtype=Task)
