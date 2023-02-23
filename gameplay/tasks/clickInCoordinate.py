import numpy as np
import hud.core
import hud.slot
from .base.baseTask import BaseTask


class ClickInCoordinateTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'clickInCoordinate'
        self.value = value

    def exec(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        hud.slot.clickSlot(slot, context['hud']['coordinate'])
        return context
    
    def did(self, context):
        res = context['coordinate'] == context['cavebot']['waypoints']['state']['checkInCoordinate']
        did = np.all(res) == True
        return did
