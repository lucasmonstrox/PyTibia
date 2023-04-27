import numpy as np
from ..typings import Task
from ..factories.makeSelectChatTab import makeSelectChatTabTask
from .groupTask import GroupTask


class GroupOfSelectLootTabTasks(GroupTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfSelectLootTab'
        self.tasks = self.makeTasks()

    # TODO: add unit tests
    # TODO: add typings
    def makeTasks(self):
        return np.array([
            makeSelectChatTabTask('loot'),
        ], dtype=Task)
