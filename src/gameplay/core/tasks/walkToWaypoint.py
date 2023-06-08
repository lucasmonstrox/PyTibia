from src.repositories.radar.typings import Coordinate
from ...typings import Context
from .common.vector import VectorTask
from .setNextWaypoint import SetNextWaypointTask
from .walkToCoordinate import WalkToCoordinateTask


class WalkToWaypointTask(VectorTask):
    def __init__(self, coordinate: Coordinate):
        super().__init__()
        self.name = 'walkToWaypoint'
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.coordinate = coordinate

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            WalkToCoordinateTask(self.coordinate).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
