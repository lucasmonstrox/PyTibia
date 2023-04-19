from src.repositories.gameWindow.core import getSlotFromCoordinate
from src.repositories.gameWindow.slot import rightClickSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .baseTask import BaseTask


class UseHoleTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'useHole'
        self.value = waypoint

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context
