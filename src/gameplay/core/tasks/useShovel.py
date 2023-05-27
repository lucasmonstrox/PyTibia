import pyautogui
from src.repositories.gameWindow.core import getSlotFromCoordinate, images, isHoleOpen
from src.repositories.gameWindow.slot import clickSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .common.base import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.value = waypoint

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        holeOpenImage = images[context['resolution']]['holeOpen']
        shouldIgnoreTask = isHoleOpen(
            context['gameWindow']['img'], holeOpenImage, context['radar']['coordinate'], self.value['coordinate'])
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        holeOpenImage = images[context['resolution']]['holeOpen']
        didTask = isHoleOpen(
            context['gameWindow']['img'], holeOpenImage, context['radar']['coordinate'], self.value['coordinate'])
        return didTask
