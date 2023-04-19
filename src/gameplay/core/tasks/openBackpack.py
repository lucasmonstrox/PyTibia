import pyautogui
from src.repositories.inventory.config import images
from src.repositories.inventory.core import isBackpackOpen
from src.utils.core import locate
from ...typings import Context
from .baseTask import BaseTask


class OpenBackpackTask(BaseTask):
    def __init__(self, backpack: str):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'openBackpack'
        self.value = backpack

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnore = isBackpackOpen(context['screenshot'], self.value)
        return shouldIgnore

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackImg = images['backpacks'][self.value]
        backpackPos = locate(context['screenshot'], backpackImg, confidence=0.8)
        if backpackPos is None:
            return context
        (x, y, _, __) = backpackPos
        backpackX = x + 5
        backpackY = y + 5
        pyautogui.rightClick(backpackX, backpackY)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        did = isBackpackOpen(context['screenshot'], self.value)
        return did
