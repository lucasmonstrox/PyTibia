import pyautogui
import hud.core
import hud.slot
from .base.baseTask import BaseTask


class UseRopeTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'useRope'
        self.value = value

    def exec(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['rope'])
        hud.slot.clickSlot(slot, context['hud']['coordinate'])
        return context
