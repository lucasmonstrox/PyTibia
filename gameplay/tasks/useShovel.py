import pyautogui
import hud.core
import hud.slot
from .baseTask import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.value = value

    def shouldIgnore(self, context):
        holeOpenImg = hud.core.images[context['resolution']]['holeOpen']
        isHoleOpen = hud.core.isHoleOpen(
            context['hudImg'], holeOpenImg, context['coordinate'], self.value['coordinate'])
        return isHoleOpen

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        hud.slot.clickSlot(slot, context['hud']['coordinate'])
        return context

    def did(self, context):
        holeOpenImg = hud.core.images[context['resolution']]['holeOpen']
        did = hud.core.isHoleOpen(
            context['hudImg'], holeOpenImg, context['coordinate'], self.value['coordinate'])
        return did
