from src.utils.keyboard import keyDown, keyUp, press
from ...typings import Context
from .common.base import BaseTask


class PressLogoutKeys(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'pressKeys'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        keyDown('ctrl')
        press(['q'])
        keyUp('ctrl')
        return context
