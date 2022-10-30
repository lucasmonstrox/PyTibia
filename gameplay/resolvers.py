from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks
from gameplay.groupTasks.makeWalkpointsBetweenTwoCoordinatesTasks import makeWalkpointsBetweenTwoCoordinatesTasks
import gameplay.tasks.refillChecker
import gameplay.tasks.useRope
import gameplay.tasks.useShovel


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'floor':
        tasks = makeGroupOfWalkpointTasks(context, waypoint['coordinate'])
        return tasks
    # elif waypoint['type'] == 'moveDownEast':
    #     tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
    #         context)
    #     return tasks
    # elif waypoint['type'] == 'moveDownNorth':
    #     tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
    #         context)
    #     return tasks
    # elif waypoint['type'] == 'moveDownSouth':
    #     tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
    #         context)
    #     return tasks
    # elif waypoint['type'] == 'moveDownWest':
    #     tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
    #         context)
    #     return tasks
    elif waypoint['type'] == 'moveUpNorth':
        print('gerando moveUpNorth')
        tasks = makeWalkpointsBetweenTwoCoordinatesTasks(waypoint['coordinate'])
        return tasks
    # elif waypoint['type'] == 'refill':
    #     tasks = gameplay.tasks.refillChecker.makeRefillTasks(
    #         context, waypoint)
    #     return tasks
    # elif waypoint['type'] == 'refillChecker':
    #     tasks = makerefillCheckerTasks(waypoint)
    #     return tasks
    # elif waypoint['type'] == 'useRope':
    #     tasks = gameplay.tasks.useRope.makeUseRopeTasks(
    #         context, context['waypoints']['state']['goalCoordinate'], waypoint)
    #     return tasks
    # elif waypoint['type'] == 'useShovel':
    #     tasks = gameplay.tasks.useShovel.makeUseShovelTasks(
    #         context, context['waypoints']['state']['goalCoordinate'], waypoint)
    #     return tasks
