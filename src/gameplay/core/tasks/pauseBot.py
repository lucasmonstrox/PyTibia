from ...typings import Context
from .common.base import BaseTask


class PauseBotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'pauseBot'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        context['cavebot']['enabled'] = False
        return context

    # TODO: add unit tests
    # TODO: check if cavebot['enabled'] is False
    def did(self, _: Context) -> bool:
        return True
