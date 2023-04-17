import pyautogui
from src.features.hud.core import getSlotFromCoordinate, images, isHoleOpen
from src.features.hud.slot import clickSlot
from .baseTask import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.value = value

    def shouldIgnore(self, context):
        holeOpenImg = images[context['resolution']]['holeOpen']
        ignore = isHoleOpen(
            context['hud']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return ignore

    def do(self, context):
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        clickSlot(slot, context['hud']['coordinate'])
        return context

    def did(self, context):
        holeOpenImg = images[context['resolution']]['holeOpen']
        did = isHoleOpen(
            context['hud']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return did
