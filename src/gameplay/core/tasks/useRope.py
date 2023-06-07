from src.repositories.gameWindow.core import getSlotFromCoordinate
from src.repositories.gameWindow.slot import clickSlot
from src.shared.typings import Waypoint
from src.utils.keyboard import press
from ...typings import Context
from .common.base import BaseTask


# TODO: implement did method checking coordinate change to up floor
class UseRopeTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useRope'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.waypoint = waypoint

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        press(context['hotkeys']['rope'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context
