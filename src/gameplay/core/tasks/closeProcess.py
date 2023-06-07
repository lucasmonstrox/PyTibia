from ...typings import Context
from .common.base import BaseTask


class CloseProcessTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'closeProcess'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        exit()
        return context
