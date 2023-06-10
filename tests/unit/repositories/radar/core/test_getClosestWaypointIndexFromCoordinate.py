import numpy as np
from src.repositories.radar.core import getClosestWaypointIndexFromCoordinate
from src.repositories.radar.typings import Waypoint


def test_should_return_2_when_closest_waypoint_is_in_index_2():
    currentCoordinate = (33094, 32790, 7)
    closestWaypoint = ('', 'walk', (33099, 32790, 7), {})
    closestDiagonalWaypoint = ('', 'walk', (33098, 32794, 7), {})
    closestWaypointFromAnotherFloor = ('', 'walk', (33099, 32790, 6), {})
    furthestWaypoint = ('', 'walk', (33082, 32790, 7), {})
    waypoints = np.array(
        [furthestWaypoint, closestWaypointFromAnotherFloor, closestWaypoint, closestDiagonalWaypoint], dtype=Waypoint)
    result = getClosestWaypointIndexFromCoordinate(
        currentCoordinate, waypoints)
    assert result == 2
