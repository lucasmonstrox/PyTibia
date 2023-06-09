import src.gameplay.utils as gameplayUtils
import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .common.base import BaseTask


class ClickInCoordinateTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'clickInCoordinate'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.waypoint = waypoint

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        gameWindowSlot.clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    def did(self, context: Context) -> bool:
        didTask = gameplayUtils.coordinatesAreEqual(context['radar']['coordinate'], context['cavebot']['waypoints']['state']['checkInCoordinate'])
        return didTask
