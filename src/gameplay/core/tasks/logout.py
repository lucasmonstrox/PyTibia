from ...typings import Context
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
    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            PressLogoutKeys().setParentTask(self).setRootTask(self),
            CloseProcessTask().setParentTask(self).setRootTask(self)
        ]
        return context
