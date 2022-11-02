import numpy as np
from time import time


class SetNextWaypointTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'setNextWaypoint'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        # TODO: fix this
        context['waypoints']['currentIndex'] += 1
        context['waypoints']['state'] = None
        return context

    def did(self, context):
        waypoint = self.value
        response = np.all(context['radarCoordinate'] == waypoint['coordinate'])
        did = response == True
        return True

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
