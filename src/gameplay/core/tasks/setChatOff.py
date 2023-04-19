from src.repositories.chat.core import enableChatOff
from ...typings import Context
from .baseTask import BaseTask


# TODO: implement did method
class SetChatOffTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'setChatOff'

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        enableChatOff(context['screenshot'])
        return context
