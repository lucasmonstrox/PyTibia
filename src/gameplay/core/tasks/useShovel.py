import pyautogui
from src.features.gameWindow.core import getSlotFromCoordinate, images, isHoleOpen
from src.features.gameWindow.slot import clickSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .baseTask import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.value = waypoint

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        holeOpenImg = images[context['resolution']]['holeOpen']
        ignore = isHoleOpen(
            context['gameWindow']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return ignore

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        holeOpenImg = images[context['resolution']]['holeOpen']
        did = isHoleOpen(
            context['gameWindow']['img'], holeOpenImg, context['radar']['coordinate'], self.value['coordinate'])
        return did
