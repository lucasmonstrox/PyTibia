import numpy as np
from ..tasks.closeProcess import CloseProcessTask
from ..tasks.pauseBot import PauseBotTask
from ..tasks.pressLogoutKeys import PressLogoutKeys
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class LogoutTask(GroupTaskExecutor):
    def __init__(self, context):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'logout'
        self.tasks = self.generateTasks(context)

    def generateTasks(self, context):
        print('vou iniciarrrr LogoutTask')
        return np.array([
            # ('pauseBot', PauseBotTask()),
            ('pressKeys', PressLogoutKeys(['ctrl', 'q'])),
            ('closeProcess', CloseProcessTask())
        ], dtype=taskType)
