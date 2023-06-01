from src.repositories.radar.typings import Coordinate
from ...typings import Context
from .common.vector import VectorTask
from .setNextWaypoint import SetNextWaypointTask
from .walkToCoordinate import WalkToCoordinate


class WalkToWaypoint(VectorTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'walkToWaypoint'
        self.coordinate = coordinate

    # TODO: add return type
    # TODO: add unit tests
    def initialize(self, context: Context):
        self.tasks = [
            WalkToCoordinate(context, self.coordinate).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        return self
