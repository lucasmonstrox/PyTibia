from player import player
from radar import radar
from utils import utils


def goToWaypoint(screenshot, waypoint, currentPlayerCoordinate):
    isFloorWaypoint = waypoint['type'] == 'floor'
    if isFloorWaypoint:
        radar.goToCoordinateByRadarClick(screenshot, currentPlayerCoordinate, waypoint['coordinate'])
        return
    isRampWaypoint = waypoint['type'] == 'ramp'
    if isRampWaypoint:
        (currentPlayerCoordinateX, currentPlayerCoordinateY, _) = currentPlayerCoordinate
        (waypointCoordinateX, waypointCoordinateY, _) = waypoint['coordinate']
        xDifference = currentPlayerCoordinateX - waypointCoordinateX
        shouldWalkToLeft = xDifference > 0
        if shouldWalkToLeft:
            utils.press('left')
            return
        shouldWalkToRight = xDifference < 0
        if shouldWalkToRight:
            utils.press('right')
            return
        yDifference = currentPlayerCoordinateY - waypointCoordinateY
        if yDifference < 0:
            utils.press('down')
            return
        if yDifference > 0:
            utils.press('up')
            return


def waypointObserver(screenshot, coordinate, waypoints, waypointIndex):
    currentWaypoint = waypoints[waypointIndex]
    if radar.isNearToCoordinate(
            coordinate, waypoints[waypointIndex]['coordinate'],
            tolerance=currentWaypoint['tolerance']):
        waypointIndex = 0 if waypointIndex == len(
            waypoints) - 1 else waypointIndex + 1
        player.stop(0.5)
        goToWaypoint(screenshot, waypoints[waypointIndex], coordinate)
        return waypointIndex
    # if souldRetrySameWaypoint:
    #     print('retrying same waypoint', currentWaypoint['coordinate'])
    #     # souldRetrySameWaypoint = False
    #     player.stop(0.5)
    #     goToWaypoint(screenshot, currentWaypoint, coordinate)
