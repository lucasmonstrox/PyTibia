import pyautogui
from src.features.inventory.config import images
from src.features.inventory.core import isBackpackOpen
from src.utils.core import locate
from .baseTask import BaseTask


class OpenBackpackTask(BaseTask):
    def __init__(self, backpack):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'openBackpack'
        self.value = backpack

    def shouldIgnore(self, context):
        shouldIgnore = isBackpackOpen(context['screenshot'], self.value)
        return shouldIgnore

    def do(self, context):
        backpackImg = images['backpacks'][self.value]
        backpackPos = locate(context['screenshot'], backpackImg, confidence=0.8)
        if backpackPos is None:
            return context
        (x, y, _, __) = backpackPos
        backpackX = x + 5
        backpackY = y + 5
        pyautogui.rightClick(backpackX, backpackY)
        return context
    
    def did(self, context):
        did = isBackpackOpen(context['screenshot'], self.value)
        return did
