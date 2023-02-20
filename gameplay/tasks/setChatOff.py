from chat.core import enableChatOff
from .baseTask import BaseTask


class SetChatOffTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'setChatOff'

    def do(self, context):
        enableChatOff(context['screenshot'])
        return context
    