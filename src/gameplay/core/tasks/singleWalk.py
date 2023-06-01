from src.shared.typings import Coordinate
from ...typings import Context
from .setNextWaypoint import SetNextWaypointTask
from .walk import WalkTask
from .common.vector import VectorTask


class SingleWalkTask(VectorTask):
    def __init__(self, checkInCoordinate: Coordinate):
        super().__init__()
        self.delayAfterComplete = 2
        self.name = 'singleWalk'
        self.checkInCoordinate = checkInCoordinate

    # TODO: add unit tests
    # TODO: add typings
    def initialize(self, context: Context):
        self.tasks = [
            WalkTask(context, self.checkInCoordinate).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
