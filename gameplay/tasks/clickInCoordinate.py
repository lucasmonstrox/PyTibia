import numpy as np
from time import time
import hud.core
import hud.slot


class ClickInCoordinateTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'clickInCoordinate'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['radarCoordinate'], self.value['coordinate'])
        hud.slot.clickSlot(slot, context['hudCoordinate'])
        return context

    def did(self, context):
        res = context['radarCoordinate'] == context['waypoints']['state']['checkInCoordinate'] 
        did = np.all(res) == True
        return did

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
