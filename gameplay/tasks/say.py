import chat.core
from .base.baseTask import BaseTask


class SayTask(BaseTask):
    def __init__(self, phrase):
        super().__init__()
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'say'
        self.value = phrase

    def exec(self, context):
        chat.core.sendMessage(context['screenshot'], self.value)
        return context
