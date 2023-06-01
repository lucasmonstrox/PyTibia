from src.repositories.inventory.core import images
from ...typings import Context
from .common.vector import VectorTask
from .dropEachFlask import DropEachFlaskTask
from .expandBackpack import ExpandBackpackTask
from .openBackpack import OpenBackpackTask
from .setNextWaypoint import SetNextWaypointTask


class DropFlasksTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'dropFlasks'

    # TODO: add unit tests
    # TODO: add typings
    def initialize(self, context: Context):
        self.tasks = [
            DropEachFlaskTask(context['backpacks']['main']).setParentTask(self),
            ExpandBackpackTask(images['containersBars'][context['backpacks']['main']]).setParentTask(self),
            OpenBackpackTask(context['backpacks']['main']).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
