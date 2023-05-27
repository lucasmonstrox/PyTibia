from src.repositories.inventory.core import images
from ...typings import Context
from ..factories.makeDropEachFlask import makeDropEachFlaskTask
from ..factories.makeExpandBackpack import makeExpandBackpackTask
from ..factories.makeOpenBackpack import makeOpenBackpackTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from .common.vector import VectorTask


class DropFlasksTask(VectorTask):
    def __init__(self, context: Context):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'dropFlasks'
        self.tasks = self.generateTasks(context)

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, context: Context):
        return [
            makeOpenBackpackTask(context['backpacks']['main']),
            makeExpandBackpackTask(images['containersBars'][context['backpacks']['main']]),
            makeDropEachFlaskTask(context['backpacks']['main']),
            makeSetNextWaypointTask(),
        ]
