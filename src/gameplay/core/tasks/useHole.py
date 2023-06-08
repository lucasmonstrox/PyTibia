import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .common.base import BaseTask


class UseHoleTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useHole'
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.waypoint = waypoint

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        gameWindowSlot.rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context
