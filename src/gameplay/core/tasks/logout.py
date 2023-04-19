import numpy as np
from ...typings import Context
from ..tasks.closeProcess import CloseProcessTask
from ..tasks.pauseBot import PauseBotTask
from ..tasks.pressLogoutKeys import PressLogoutKeys
from ..typings import Task
from .groupTask import GroupTask


class LogoutTask(GroupTask):
    def __init__(self, context: Context):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'logout'
        self.tasks = self.generateTasks(context)

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, context: Context):
        return np.array([
            # ('pauseBot', PauseBotTask()),
            ('pressKeys', PressLogoutKeys(['ctrl', 'q'])),
            ('closeProcess', CloseProcessTask())
        ], dtype=Task)
