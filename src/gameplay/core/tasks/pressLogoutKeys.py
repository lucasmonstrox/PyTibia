import pyautogui
from .baseTask import BaseTask


class PressLogoutKeys(BaseTask):
    def __init__(self, keys):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'pressKeys'
        self.value = keys

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        with pyautogui.hold('ctrl'):
            pyautogui.press(['q'])
        return context
