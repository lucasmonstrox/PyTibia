from gameplay.groupTasks.groupOfRefillCheckerTasks import GroupOfRefillCheckerTasks
from gameplay.groupTasks.groupOfSingleWalkTasks import GroupOfSingleWalkTasks
from gameplay.groupTasks.groupOfUseRopeTasks import GroupOfUseRopeTasks
from gameplay.groupTasks.groupOfUseShovelTasks import GroupOfUseShovelTasks
from gameplay.groupTasks.groupOfWalkTasks import GroupOfWalkTasks


def resolveTasksByWaypointType(context, waypoint):
    # if waypoint['type'] == 'depositItems':
    #     tasks = makeGroupOfDepositItemsTasks(waypoint)
    #     return tasks
    if waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        return GroupOfSingleWalkTasks(context, context['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        return GroupOfSingleWalkTasks(context, context['waypoints']['state']['checkInCoordinate'])
    elif waypoint['type'] == 'walk':
        return GroupOfWalkTasks(context, waypoint['coordinate'])
    # elif waypoint['type'] == 'refill':
    #     tasks = gameplay.tasks.refillChecker.makeRefillTasks(
    #         context, waypoint)
    #     return tasks
    elif waypoint['type'] == 'refillChecker':
        return GroupOfRefillCheckerTasks(waypoint)
    # elif waypoint['type'] == 'useHole':
    #     tasks = makeGroupOfUseHoleTasks(
    #         context, context['waypoints']['state']['goalCoordinate'], waypoint)
    #     return tasks
    elif waypoint['type'] == 'useRope':
        return GroupOfUseRopeTasks(context, waypoint)
    elif waypoint['type'] == 'useShovel':
        return GroupOfUseShovelTasks(context, waypoint)
