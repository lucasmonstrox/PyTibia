from .tasks.depositGold import DepositGoldTask
from .tasks.depositItems import DepositItemsTask
from .tasks.dropFlasks import DropFlasksTask
from .tasks.groupOfRefillChecker import GroupOfRefillCheckerTasks
from .tasks.groupOfRefillTasks import GroupOfRefillTasks
from .tasks.groupOfSingleWalk import GroupOfSingleWalkTasks
from .tasks.groupOfWalk import GroupOfWalkTasks
from .tasks.logout import LogoutTask
from .tasks.lureCreatures import LureCreaturesTask
from .tasks.useRopeWaypoint import UseRopeWaypointTask
from .tasks.useShovelWaypoint import UseShovelWaypointTask


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'depositGold':
        return DepositGoldTask()
    elif waypoint['type'] == 'depositItems':
        return DepositItemsTask(context, waypoint)
    elif waypoint['type'] == 'dropFlasks':
        return DropFlasksTask(context)
    elif waypoint['type'] == 'lure':
        return LureCreaturesTask(waypoint['coordinate'])
    elif waypoint['type'] == 'logout':
        return LogoutTask(context)
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'refill':
        return GroupOfRefillTasks(context, waypoint)
    elif waypoint['type'] == 'refillChecker':
        return GroupOfRefillCheckerTasks(waypoint)
    elif waypoint['type'] == 'useRope':
        return UseRopeWaypointTask(context, waypoint)
    elif waypoint['type'] == 'useShovel':
        return UseShovelWaypointTask(context, waypoint)
    elif waypoint['type'] == 'walk':
        return GroupOfWalkTasks(context, waypoint['coordinate'])
