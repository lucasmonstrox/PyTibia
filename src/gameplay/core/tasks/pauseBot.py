from ...typings import Context
from .baseTask import BaseTask


class PauseBotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'pauseBot'

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        context['cavebot']['enabled'] = False
        return context

    # TODO: add unit tests
    # TODO: check if cavebot['enabled'] is False
    def did(self, context: Context) -> bool:
        return True
