from .baseTask import BaseTask


class CloseProcessTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'loseProcess'
        self.value = None

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        exit()
        return context
