import numpy as np
from ..typings import Task
from ..factories.makeSay import makeSayTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from .groupTask import GroupTask


# TODO: check if gold was deposited successfully
class DepositGoldTask(GroupTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'depositGold'
        self.tasks = self.makeTasks()

    # TODO: add unit tests
    # TODO: add typings
    def makeTasks(self):
        return np.array([
            makeSayTask('hi'),
            makeSayTask('deposit all'),
            makeSayTask('yes'),
            makeSetNextWaypointTask(),
        ], dtype=Task)
