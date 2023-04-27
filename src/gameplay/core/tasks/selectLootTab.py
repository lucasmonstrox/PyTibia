import numpy as np
import pyautogui
from src.repositories.chat.core import getLootTabPosition
from ..typings import Task
from ..factories.makeSay import makeSayTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from .baseTask import BaseTask
from .groupTask import GroupTask


class SelectLootTabTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayOfTimeout = 1
        self.name = 'selectLootTab'

    def do(self, context):
        lootTabPosition = getLootTabPosition(context['screenshot'])
        if lootTabPosition is not None:
            pyautogui.click(lootTabPosition[0], lootTabPosition[1])
        return context


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
            ('selectLootTab', SelectLootTabTask()),
        ], dtype=Task)
