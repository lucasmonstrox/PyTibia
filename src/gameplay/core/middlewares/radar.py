from src.repositories.radar.core import getClosestWaypointIndexFromCoordinate, getCoordinate
from ...typings import Context


# TODO: add unit tests
def setRadarMiddleware(gameContext: Context) -> Context:
    gameContext['radar']['coordinate'] = getCoordinate(
        gameContext['screenshot'], previousCoordinate=gameContext['radar']['previousCoordinate'])
    return gameContext


# TODO: add unit tests
def setWaypointIndex(gameContext: Context) -> Context:
    if gameContext['cavebot']['waypoints']['currentIndex'] == None:
        gameContext['cavebot']['waypoints']['currentIndex'] = getClosestWaypointIndexFromCoordinate(
            gameContext['radar']['coordinate'], gameContext['cavebot']['waypoints']['points'])
    return gameContext
