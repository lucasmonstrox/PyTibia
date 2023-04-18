from ...typings import Context
from .baseTask import BaseTask


class CloseProcessTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'loseProcess'
        self.value = None

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        exit()
        return context
