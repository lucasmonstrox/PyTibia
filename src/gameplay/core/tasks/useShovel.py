from src.repositories.gameWindow.core import getSlotFromCoordinate, images, isHoleOpen
from src.repositories.gameWindow.slot import clickSlot
from src.shared.typings import Waypoint
from src.utils.keyboard import press
from ...typings import Context
from .common.base import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useShovel'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.waypoint = waypoint

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = isHoleOpen(
            context['gameWindow']['image'], images[context['resolution']]['holeOpen'], context['radar']['coordinate'], self.waypoint['coordinate'])
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        press(context['hotkeys']['shovel'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = isHoleOpen(
            context['gameWindow']['image'], images[context['resolution']]['holeOpen'], context['radar']['coordinate'], self.waypoint['coordinate'])
        return didTask
