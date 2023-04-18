from src.features.chat.core import sendMessage
from ...typings import Context
from .baseTask import BaseTask


# TODO: implement did method checking if phrase was spelled into chat
class SayTask(BaseTask):
    def __init__(self, phrase: str):
        super().__init__()
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'say'
        self.value = phrase

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        sendMessage(context['screenshot'], self.value)
        return context
