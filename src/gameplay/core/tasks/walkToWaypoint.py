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
        self.value = coordinate
        self.tasks = self.generateTasks(context, self.value)

    # TODO: add return type
    # TODO: add unit tests
    def generateTasks(self, context: Context, waypointCoordinate: Coordinate):
        return [
            WalkToCoordinate(context, waypointCoordinate),
            SetNextWaypointTask(),
        ]
