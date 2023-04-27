import pyautogui
from src.repositories.chat.core import getChatStatus
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
        (_, chatIsOn) = getChatStatus(context['screenshot'])
        if chatIsOn:
            pyautogui.press('enter')
        return context
