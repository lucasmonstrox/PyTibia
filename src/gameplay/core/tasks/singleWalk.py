from ...typings import Context
from .common.vector import VectorTask
from .moveDown import MoveDown
from .setNextWaypoint import SetNextWaypointTask


class SingleWalkTask(VectorTask):
    # TODO: add types
    def __init__(self, direction: str):
        super().__init__()
        self.name = 'singleWalk'
        self.delayAfterComplete = 2
        self.isRootTask = True
        self.direction = direction

    # TODO: add unit tests
    # TODO: add typings
    def initialize(self, context: Context):
        self.tasks = [
            MoveDown(context, self.direction).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
