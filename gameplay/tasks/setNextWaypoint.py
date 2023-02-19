from time import time
from utils.array import getNextArrayIndex
from ..waypoint import resolveGoalCoordinate


class SetNextWaypointTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = None
        self.name = 'setNextWaypoint'
        self.status = 'notStarted'
        self.value = None

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        currentWaypoint = context['cavebot']['waypoints']['points'][context['cavebot']['waypoints']['currentIndex']]
        context['cavebot']['waypoints']['state'] = resolveGoalCoordinate(context['coordinate'], currentWaypoint)
        return context
    
    def ping(self, context):
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
