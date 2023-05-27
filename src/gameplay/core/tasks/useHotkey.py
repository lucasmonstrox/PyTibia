import pyautogui
from ...typings import Context
from .common.base import BaseTask
from .common.vector import VectorTask


class UseHotkeyVectorTask(VectorTask):
    def __init__(self, hotkey: str, delayAfterComplete: int=0):
        super().__init__()
        self.name = 'useHotkeyGroup'
        self.value = hotkey
        self.tasks = self.makeTasks(hotkey, delayAfterComplete)

    # TODO: add unit tests
    # TODO: add typings
    def makeTasks(self, hotkey, delayAfterComplete: int):
        return [
            UseHotkeyTask(hotkey, delayAfterComplete=delayAfterComplete),
        ]


class UseHotkeyTask(BaseTask):
    def __init__(self, hotkey: str, delayAfterComplete: int=0):
        super().__init__()
        self.delayAfterComplete = delayAfterComplete
        self.name = 'usePotionTask'
        self.value = hotkey

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        pyautogui.press(self.value)
        return context
