from .groupTasks.groupOfDepositItemsTasks import GroupOfDepositItemsTasks
from .groupTasks.groupOfRefillCheckerTasks import GroupOfRefillCheckerTasks
from .groupTasks.groupOfRefillTasks import GroupOfRefillTasks
from .groupTasks.groupOfSingleWalkTasks import GroupOfSingleWalkTasks
from .groupTasks.groupOfUseRopeTasks import GroupOfUseRopeTasks
from .groupTasks.groupOfUseShovelTasks import GroupOfUseShovelTasks
from .groupTasks.groupOfWalkTasks import GroupOfWalkTasks


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'depositItems':
        return GroupOfDepositItemsTasks(context, waypoint)
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        return GroupOfSingleWalkTasks(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'refill':
        return GroupOfRefillTasks(context, waypoint)
    elif waypoint['type'] == 'refillChecker':
        return GroupOfRefillCheckerTasks(waypoint)
    elif waypoint['type'] == 'useRope':
        return GroupOfUseRopeTasks(context, waypoint)
    elif waypoint['type'] == 'useShovel':
        return GroupOfUseShovelTasks(context, waypoint)
    elif waypoint['type'] == 'walk':
        return GroupOfWalkTasks(context, waypoint['coordinate'])
