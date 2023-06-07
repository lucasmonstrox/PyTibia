from src.gameplay.typings import Context
from src.utils.keyboard import press, write
from ...typings import Context
from .common.base import BaseTask


class SayTask(BaseTask):
    def __init__(self, phrase: str):
        super().__init__()
        self.name = 'say'
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.phrase = phrase

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        write(self.phrase)
        press('enter')
        return context

    # TODO: add way to check if phrase is spelled into the chat
    def did(self, _: Context) -> bool:
        return True
