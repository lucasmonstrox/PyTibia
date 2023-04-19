import numpy as np
import pyautogui
from ...typings import Context
from ..typings import Task
from .baseTask import BaseTask
from .groupTask import GroupTask


class UseHotkeyGroupTask(GroupTask):
    def __init__(self, hotkey: str, delayAfterComplete: int=0):
        super().__init__()
        self.name = 'useHotkeyGroup'
        self.value = hotkey
        self.tasks = self.makeTasks(hotkey, delayAfterComplete)

    # TODO: add unit tests
    # TODO: add typings
    def makeTasks(self, hotkey, delayAfterComplete: int):
        return np.array([
            UseHotkeyTask(hotkey, delayAfterComplete=delayAfterComplete),
        ], dtype=Task)


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
