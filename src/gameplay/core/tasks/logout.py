from ...typings import Context
# from .pauseBot import PauseBotTask
from .common.vector import VectorTask
from .closeProcess import CloseProcessTask
from .pressLogoutKeys import PressLogoutKeys


class LogoutTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'logout'
        self.isRootTask = True
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    # TODO: add unit tests
    # TODO: add typings
    def onBeforeStart(self, _: Context):
        self.tasks = [
            PressLogoutKeys(['ctrl', 'q']).setParentTask(self),
            CloseProcessTask().setParentTask(self)
        ]
        self.initialized = True
        return self
