import pyautogui
from src.repositories.inventory.config import images
from src.repositories.inventory.core import isBackpackOpen
from src.utils.core import locate
from src.utils.image import save
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
        shouldIgnoreTask = isBackpackOpen(context['screenshot'], self.value)
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        backpackImage = images['slots'][self.value]
        backpackPosition = locate(context['screenshot'], backpackImage, confidence=0.8)
        if backpackPosition is None:
            return context
        (x, y, _, __) = backpackPosition
        backpackX = x + 5
        backpackY = y + 5
        pyautogui.rightClick(backpackX, backpackY)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = isBackpackOpen(context['screenshot'], self.value)
        return didTask
