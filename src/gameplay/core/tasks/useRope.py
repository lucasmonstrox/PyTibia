import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
import src.utils.keyboard as keyboard
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

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        keyboard.press('o')
        gameWindowSlot.clickSlot(slot, context['gameWindow']['coordinate'])
        return context
