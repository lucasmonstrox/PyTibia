from .tasks.depositItems import DepositItemsTask
from .tasks.refillCheckerWaypoint import RefillCheckerWaypointTask
from .tasks.refillWaypointTask import RefillWaypointTask
from .tasks.groupOfSingleWalk import GroupOfSingleWalkTasks
from .tasks.useRopeWaypoint import UseRopeWaypointTask
from .tasks.useShovelWaypoint import UseShovelWaypointTask
from .tasks.groupOfWalk import GroupOfWalkTasks


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'depositItems':
        return DepositItemsTask(context, waypoint)
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'refill':
        return RefillWaypointTask(context, waypoint)
    elif waypoint['type'] == 'refillChecker':
        return RefillCheckerWaypointTask(waypoint)
    elif waypoint['type'] == 'useRope':
        return UseRopeWaypointTask(context, waypoint)
    elif waypoint['type'] == 'useShovel':
        return UseShovelWaypointTask(context, waypoint)
    elif waypoint['type'] == 'walk':
        return GroupOfWalkTasks(context, waypoint['coordinate'])
