from src.gameplay.typings import Context
import src.repositories.chat.core as chatCore
import src.utils.keyboard as keyboard
from ...typings import Context
from .common.base import BaseTask


# TODO: check if chat is off on did
class EnableChatTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'enableChat'
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2

    def shouldIgnore(self, context: Context) -> bool:
        (_, chatIsOn) = chatCore.getChatStatus(context['screenshot'])
        shouldIgnoreTask = chatIsOn == True
        return shouldIgnoreTask

    def do(self, context: Context) -> Context:
        keyboard.press('enter')
        return context
