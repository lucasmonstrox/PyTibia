import numpy as np
from radar.core import getClosestWaypointIndexFromCoordinate
from radar.types import waypointType


def test_should_return_2_when_closest_waypoint_is_in_index_2():
    currentCoordinate = (33094, 32790, 7)
    closestWaypoint = ('floor', (33099, 32790, 7), 0)
    closestDiagonalWaypoint = ('floor', (33098, 32794, 7), 0)
    closestWaypointFromAnotherFloor = ('floor', (33099, 32790, 6), 0)
    furthestWaypoint = ('floor', (33082, 32790, 7), 0)
    waypoints = np.array(
        [furthestWaypoint, closestWaypointFromAnotherFloor, closestWaypoint, closestDiagonalWaypoint], dtype=waypointType)
    result = getClosestWaypointIndexFromCoordinate(
        currentCoordinate, waypoints)
    assert result == 2
