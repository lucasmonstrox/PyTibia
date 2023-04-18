import pyautogui
from src.features.gameWindow.core import getSlotFromCoordinate
from src.features.gameWindow.slot import clickSlot
from .baseTask import BaseTask


# TODO: implement did method checking coordinate change to up floor
class UseRopeTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'useRope'
        self.value = value

    def do(self, context):
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['rope'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context
