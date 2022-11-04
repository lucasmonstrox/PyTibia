from gameplay.groupTasks.groupOfDepositItemsTasks import GroupOfDepositItemsTasks
from gameplay.groupTasks.groupOfRefillCheckerTasks import GroupOfRefillCheckerTasks
from gameplay.groupTasks.groupOfRefillTasks import GroupOfRefillTasks
from gameplay.groupTasks.groupOfSingleWalkTasks import GroupOfSingleWalkTasks
from gameplay.groupTasks.groupOfUseRopeTasks import GroupOfUseRopeTasks
from gameplay.groupTasks.groupOfUseShovelTasks import GroupOfUseShovelTasks
from gameplay.groupTasks.groupOfWalkTasks import GroupOfWalkTasks


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'depositItems':
        return GroupOfDepositItemsTasks(context, waypoint)
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfSingleWalkTasks(context, context['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        return GroupOfSingleWalkTasks(context, context['waypoints']['state']['checkInCoordinate'])
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
