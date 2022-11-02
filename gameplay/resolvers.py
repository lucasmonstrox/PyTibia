from gameplay.groupTasks.makeGroupOfRefillCheckerTasks import makeGroupOfRefillCheckerTasks
from gameplay.groupTasks.makeGroupOfUseRopeTasks import makeGroupOfUseRopeTasks
from gameplay.groupTasks.makeGroupOfUseShovelTasks import makeGroupOfUseShovelTasks
from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks
from gameplay.groupTasks.makeWalkpointsBetweenTwoCoordinatesTasks import makeWalkpointsBetweenTwoCoordinatesTasks


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'floor':
        tasks = makeGroupOfWalkpointTasks(context, waypoint['coordinate'])
        return tasks
    elif waypoint['type'] == 'moveDownEast' or waypoint['type'] == 'moveDownNorth' or waypoint['type'] == 'moveDownSouth' or waypoint['type'] == 'moveDownWest':
        tasks = makeWalkpointsBetweenTwoCoordinatesTasks(
            context['waypoints']['state']['checkInCoordinate'])
        return tasks
    elif waypoint['type'] == 'moveUpNorth' or waypoint['type'] == 'moveUpSouth' or waypoint['type'] == 'moveUpWest' or waypoint['type'] == 'moveUpEast':
        tasks = makeWalkpointsBetweenTwoCoordinatesTasks(
            context['waypoints']['state']['checkInCoordinate'])
        return tasks
    # elif waypoint['type'] == 'refill':
    #     tasks = gameplay.tasks.refillChecker.makeRefillTasks(
    #         context, waypoint)
    #     return tasks
    elif waypoint['type'] == 'refillChecker':
        tasks = makeGroupOfRefillCheckerTasks(waypoint)
        return tasks
    elif waypoint['type'] == 'useRope':
        tasks = makeGroupOfUseRopeTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint)
        return tasks
    elif waypoint['type'] == 'useShovel':
        tasks = makeGroupOfUseShovelTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint)
        return tasks
