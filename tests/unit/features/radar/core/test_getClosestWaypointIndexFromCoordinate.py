import numpy as np
from src.features.radar.core import getClosestWaypointIndexFromCoordinate
from src.features.radar.types import waypointType


def test_should_return_2_when_closest_waypoint_is_in_index_2():
    currentCoordinate = (33094, 32790, 7)
    closestWaypoint = ('walk', (33099, 32790, 7), 0)
    closestDiagonalWaypoint = ('walk', (33098, 32794, 7), 0)
    closestWaypointFromAnotherFloor = ('walk', (33099, 32790, 6), 0)
    furthestWaypoint = ('walk', (33082, 32790, 7), 0)
    waypoints = np.array(
        [furthestWaypoint, closestWaypointFromAnotherFloor, closestWaypoint, closestDiagonalWaypoint], dtype=waypointType)
    result = getClosestWaypointIndexFromCoordinate(
        currentCoordinate, waypoints)
    assert result == 2
