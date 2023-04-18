import pyautogui
from src.features.gameWindow.core import getSlotFromCoordinate, images, isHoleOpen
from src.features.gameWindow.slot import clickSlot
from .baseTask import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.value = value

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def shouldIgnore(self, context):
        holeOpenImg = images[context['resolution']]['holeOpen']
        ignore = isHoleOpen(
            context['gameWindow']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return ignore

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def did(self, context):
        holeOpenImg = images[context['resolution']]['holeOpen']
        did = isHoleOpen(
            context['gameWindow']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return did
