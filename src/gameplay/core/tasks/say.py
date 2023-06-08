from src.gameplay.typings import Context
import src.utils.keyboard as keyboard
from ...typings import Context
from .common.base import BaseTask


# TODO: add way to check if phrase is spelled into the chat when did
class SayTask(BaseTask):
    def __init__(self, phrase: str):
        super().__init__()
        self.name = 'say'
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.phrase = phrase

    def do(self, context: Context) -> Context:
        keyboard.write(self.phrase)
        keyboard.press('enter')
        return context
