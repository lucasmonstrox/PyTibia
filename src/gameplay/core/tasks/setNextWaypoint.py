from src.utils.array import getNextArrayIndex
from ...typings import Context
from ..waypoint import resolveGoalCoordinate
from .common.base import BaseTask


class SetNextWaypointTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'setNextWaypoint'

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        nextWaypointIndex = getNextArrayIndex(
            context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        currentWaypoint = context['cavebot']['waypoints']['points'][context['cavebot']['waypoints']['currentIndex']]
        context['cavebot']['waypoints']['state'] = resolveGoalCoordinate(context['radar']['coordinate'], currentWaypoint)
        return context
