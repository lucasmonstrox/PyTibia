from .tasks.groupOfDepositItems import GroupOfDepositItemsTasks
from .tasks.groupOfRefillChecker import GroupOfRefillCheckerTasks
from .tasks.groupOfRefillTasks import GroupOfRefillTasks
from .tasks.groupOfSingleWalk import GroupOfSingleWalkTasks
from .tasks.groupOfMoveDown import GroupOfMoveDown
from .tasks.groupOfUseRope import GroupOfUseRopeTasks
from .tasks.groupOfUseShovel import GroupOfUseShovelTasks
from .tasks.groupOfWalk import GroupOfWalkTasks


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'depositItems':
        return GroupOfDepositItemsTasks(context, waypoint)
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfMoveDown(context, context['cavebot']['waypoints']['state']['checkInCoordinate'])
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
