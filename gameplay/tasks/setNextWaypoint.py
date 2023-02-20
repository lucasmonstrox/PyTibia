from utils.array import getNextArrayIndex
from ..waypoint import resolveGoalCoordinate
from .baseTask import BaseTask


class SetNextWaypointTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'setNextWaypoint'

    def do(self, context):
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        currentWaypoint = context['cavebot']['waypoints']['points'][context['cavebot']['waypoints']['currentIndex']]
        context['cavebot']['waypoints']['state'] = resolveGoalCoordinate(context['coordinate'], currentWaypoint)
        return context
