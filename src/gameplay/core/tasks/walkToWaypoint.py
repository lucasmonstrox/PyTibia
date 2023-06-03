from src.repositories.radar.typings import Coordinate
from ...typings import Context
from .common.vector import VectorTask
from .setNextWaypoint import SetNextWaypointTask
from .walkToCoordinate import WalkToCoordinate


class WalkToWaypoint(VectorTask):
    def __init__(self, coordinate: Coordinate):
        super().__init__()
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.name = 'walkToWaypoint'
        self.coordinate = coordinate

    # TODO: add return type
    # TODO: add unit tests
    def initialize(self, _: Context):
        self.tasks = [
            WalkToCoordinate(self.coordinate).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
