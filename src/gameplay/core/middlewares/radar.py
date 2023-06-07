from src.repositories.radar.core import getClosestWaypointIndexFromCoordinate, getCoordinate
from ...typings import Context


# TODO: add unit tests
def setRadarMiddleware(context: Context) -> Context:
    context['radar']['coordinate'] = getCoordinate(
        context['screenshot'], previousCoordinate=context['radar']['previousCoordinate'])
    return context


# TODO: add unit tests
def setWaypointIndexMiddleware(context: Context) -> Context:
    if context['cavebot']['waypoints']['currentIndex'] == None:
        context['cavebot']['waypoints']['currentIndex'] = getClosestWaypointIndexFromCoordinate(
            context['radar']['coordinate'], context['cavebot']['waypoints']['points'])
    return context
