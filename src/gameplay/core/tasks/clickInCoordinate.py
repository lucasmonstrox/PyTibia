import numpy as np
from src.repositories.gameWindow.core import getSlotFromCoordinate
from src.repositories.gameWindow.slot import clickSlot
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

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        res = context['radar']['coordinate'] == context['cavebot']['waypoints']['state']['checkInCoordinate']
        # TODO: numbait
        didTask = np.all(res) == True
        return didTask
