from src.shared.typings import Waypoint
from ..factories.makeRefillChecker import makeRefillCheckerTask
from .common.vector import VectorTask


class GroupOfRefillCheckerTasks(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefillChecker'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, waypoint: Waypoint):
        return [makeRefillCheckerTask(waypoint)]
