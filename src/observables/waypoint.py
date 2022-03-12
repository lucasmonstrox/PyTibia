import numpy as np
from player import player
from radar import radar
from utils import utils
from scipy.spatial import distance

waypointType = np.dtype([
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('tolerance', np.uint8)
])
waypoints = np.array([
    # ('floor', (33085, 32788, 7), 0),
    # ('ramp', (33085, 32786, 6), 0),
    # ('floor', (33085, 32785, 6), 0),
    # ('ramp', (33085, 32783, 7), 0),
    # ('floor', (33038, 32810, 7), 0),
    # ('ramp', (33038, 32808, 6), 0),
    # ('floor', (33033, 32801, 6), 0),
    # ('ramp', (33033, 32799, 5), 0),
    # ('floor', (33032, 32779, 5), 0),
    # ('ramp', (33032, 32777, 4), 0),
    # ('floor', (33032, 32786, 4), 0),
    # ('ramp', (33032, 32788, 3), 0),
    # ('floor', (33031, 32788, 3), 0),
    # ('ramp', (33029, 32788, 2), 0),
    # ('floor', (33029, 32781, 2), 0),
    # ('ramp', (33029, 32779, 1), 0),
    # ('floor', (33029, 32776, 1), 0),
    # ('ramp', (33029, 32774, 0), 0),
    # ('floor', (33030, 32756, 0), 0),
    # ('ramp', (33032, 32756, 1), 0),
    # ('floor', (33021, 32746, 1), 0),
    # ('ramp', (33019, 32746, 2), 0),
    # ('floor', (33016, 32745, 2), 0),
    # ('ramp', (33016, 32743, 3), 0),
    # ('floor', (33010, 32727, 3), 0),
    # ('ramp', (33010, 32725, 4), 0),
    # ('floor', (32999, 32703, 4), 0),
    # ('ramp', (32999, 32705, 5), 0),
    # ('floor', (32998, 32709, 5), 0),
    # ('ramp', (32998, 32711, 6), 0),
    # ('floor', (32982, 32715, 6), 0),
    # ('ramp', (32982, 32717, 7), 0),
    # ('floor', (32953, 32769, 7), 0),
    # ('floor', (33004, 32750, 7), 0),
    # ('ramp', (33006, 32750, 6), 0),
    # ('floor', (33015, 32749, 6), 0),
    # ('ramp', (33015, 32751, 5), 0),
    # ('ramp', (33015, 32753, 4), 0),
    # ('floor', (33009, 32770, 4), 0),
    # ('ramp', (33009, 32772, 5), 0),
    # ('floor', (33004, 32765, 5), 0),
    # ('ramp', (33004, 32767, 6), 0),
    # ('floor', (33004, 32770, 6), 0),
    # ('ramp', (33004, 32772, 7), 0),
    ('floor', (33004, 32772, 7), 10),
    ('floor', (32994, 32815, 7), 10),
    ('floor', (33003, 32831, 7), 10),
    ('floor', (32975, 32802, 7), 10),
    ('floor', (32957, 32824, 7), 10),
    ('floor', (32978, 32832, 7), 10),
    ('floor', (32981, 32857, 7), 10),
    ('floor', (32961, 32861, 7), 10),
    ('floor', (32958, 32834, 7), 10),
    ('floor', (32987, 32799, 7), 10),
    # ('floor', (32981, 32795, 7)),
    # ('floor', (32962, 32814, 7)),
    # ('floor', (32996, 32805, 7)),
    # ('floor', (33005, 32783, 7)),
], dtype=waypointType)


def getWaypointIndexFromClosestCoordinate(coordinate):
    (_, _, floorLevel) = coordinate
    waypointsIndexes = np.nonzero(waypoints['coordinate'][:, 2] == floorLevel)[0]
    hasNoWaypointsIndexes = len(waypointsIndexes) == 0
    if hasNoWaypointsIndexes:
        return
    waypointDistanceType = np.dtype([('index', np.uint16), ('distance', np.float32)])
    possibleWaypoints = np.array([(waypointIndex, distance.euclidean(waypoints[waypointIndex]['coordinate'], coordinate))
                                for waypointIndex in waypointsIndexes], dtype=waypointDistanceType)
    sortedWaypoints = np.sort(possibleWaypoints, order='distance')
    return sortedWaypoints[0]['index']


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


def waypoint(value):
    print('value', value)
    return
    (screenshot, currentCoordinate) = value
    currentWaypointIndex = getWaypointIndexFromClosestCoordinate(currentCoordinate)
    # souldRetrySameWaypoint = True
    currentWaypoint = waypoints[currentWaypointIndex]
    if radar.isNearToCoordinate(
            currentCoordinate, waypoints[currentWaypointIndex]['coordinate'],
            tolerance=currentWaypoint['tolerance']):
        # souldRetrySameWaypoint = False
        currentWaypointIndex = 0 if currentWaypointIndex == len(
            waypoints) - 1 else currentWaypointIndex + 1
        player.stop(0.5)
        goToWaypoint(screenshot, waypoints[currentWaypointIndex], currentCoordinate)
        # return
    # if souldRetrySameWaypoint:
    #     print('retrying same waypoint', currentWaypoint['coordinate'])
    #     souldRetrySameWaypoint = False
    #     player.stop(0.5)
    #     goToWaypoint(screenshot, currentWaypoint, currentCoordinate)
