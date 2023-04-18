from src.features.radar.core import getClosestWaypointIndexFromCoordinate, getCoordinate


def setRadarMiddleware(gameContext):
    gameContext['radar']['coordinate'] = getCoordinate(
        gameContext['screenshot'], previousCoordinate=gameContext['radar']['previousCoordinate'])
    return gameContext


def setWaypointIndex(gameContext):
    if gameContext['cavebot']['waypoints']['currentIndex'] == None:
        gameContext['cavebot']['waypoints']['currentIndex'] = getClosestWaypointIndexFromCoordinate(
            gameContext['radar']['coordinate'], gameContext['cavebot']['waypoints']['points'])
    return gameContext
