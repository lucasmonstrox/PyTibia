from src.shared.typings import Coordinate
from ...typings import Context
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..factories.makeWalk import makeWalkTask
from .common.vector import VectorTask


class GroupOfSingleWalkTasks(VectorTask):
    def __init__(self, context: Context, checkInCoordinate: Coordinate):
        super().__init__()
        self.delayAfterComplete = 2
        self.name = 'groupOfSingleWalk'
        self.tasks = self.generateTasks(context, checkInCoordinate)
        self.value = checkInCoordinate

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, context: Context, checkInCoordinate: Coordinate):
        return [
            makeWalkTask(context, checkInCoordinate),
            makeSetNextWaypointTask(),
        ]
