from src.features.chat.core import sendMessage
from .baseTask import BaseTask


# TODO: implement did method checking if phrase was spelled into chat
class SayTask(BaseTask):
    def __init__(self, phrase):
        super().__init__()
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'say'
        self.value = phrase

    def do(self, context):
        sendMessage(context['screenshot'], self.value)
        return context
