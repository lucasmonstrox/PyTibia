from .baseTask import BaseTask


class PauseBotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'pauseBot'

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        context['cavebot']['enabled'] = False
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    # TODO: check if cavebot['enabled'] is False
    def did(self, context):
        return True
