import numpy as np
from src.features.hud.core import getSlotFromCoordinate
from src.features.hud.slot import clickSlot
from .baseTask import BaseTask


class ClickInCoordinateTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'clickInCoordinate'
        self.value = value

    def do(self, context):
        slot = getSlotFromCoordinate(
            context['radar']['coordinate'], self.value['coordinate'])
        clickSlot(slot, context['hud']['coordinate'])
        return context
    
    def did(self, context):
        res = context['radar']['coordinate'] == context['cavebot']['waypoints']['state']['checkInCoordinate']
        did = np.all(res) == True
        return did
