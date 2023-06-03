from src.repositories.gameWindow.core import getSlotFromCoordinate
from src.repositories.gameWindow.slot import rightClickSlot
from src.repositories.inventory.core import isLockerOpen
from ...typings import Context
from .common.base import BaseTask


class OpenLockerTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'openLockerTask'

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        isOpen = isLockerOpen(context['screenshot'])
        return isOpen

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(context['radar']['coordinate'], context['deposit']['lockerCoordinate'])
        rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = isLockerOpen(context['screenshot'])
        return didTask
