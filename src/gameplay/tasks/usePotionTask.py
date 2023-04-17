import numpy as np
import pyautogui
from ..typings import taskType
from .baseTask import BaseTask
from .groupTaskExecutor import GroupTaskExecutor


class UsePotionGroupTask(GroupTaskExecutor):
    def __init__(self, hotkey, delayAfterComplete=0):
        super().__init__()
        self.name = 'usePotionGroup'
        self.value = hotkey
        self.tasks = self.makeTasks(hotkey, delayAfterComplete)

    def makeTasks(self, hotkey, delayAfterComplete):
        return np.array([
            UsePotionTask(hotkey, delayAfterComplete=delayAfterComplete),
        ], dtype=taskType)


class UsePotionTask(BaseTask):
    def __init__(self, hotkey, delayAfterComplete=0):
        super().__init__()
        self.delayAfterComplete = delayAfterComplete
        self.name = 'usePotionTask'
        self.value = hotkey

    def do(self, context):
        pyautogui.press(self.value)
        return context
    
    