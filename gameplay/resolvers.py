import gameplay.baseTasks
import gameplay.tasks.check
import gameplay.tasks.moveDownNorth
import gameplay.tasks.moveDownSouth
import gameplay.tasks.moveDownWest
import gameplay.tasks.moveUpNorth
import gameplay.tasks.moveUpSouth
import gameplay.tasks.refillPotionsChecker
import gameplay.tasks.useRope
import gameplay.tasks.useShovel


def resolveTasksByWaypointType(context, waypoint):
    if waypoint['type'] == 'check':
        tasks = gameplay.tasks.check.makeCheckTasks(waypoint)
        return tasks
    elif waypoint['type'] == 'floor':
        tasks = gameplay.baseTasks.makeWalkpointTasks(
            context, waypoint['coordinate'])
        return tasks
    elif waypoint['type'] == 'moveDownEast':
        tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
            context)
        return tasks
    elif waypoint['type'] == 'moveDownNorth':
        tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
            context)
        return tasks
    elif waypoint['type'] == 'moveDownSouth':
        tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
            context)
        return tasks
    elif waypoint['type'] == 'moveDownWest':
        tasks = gameplay.baseTasks.makeWalkpointsTasksBetweenGoalAndCheckinCoordinates(
            context)
        return tasks
    elif waypoint['type'] == 'moveUpNorth':
        tasks = gameplay.tasks.moveUpNorth.makeMoveUpNorthTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint['coordinate'])
        return tasks
    elif waypoint['type'] == 'moveUpSouth':
        tasks = gameplay.tasks.moveUpSouth.makeMoveUpSouthTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint['coordinate'])
        return tasks
    elif waypoint['type'] == 'refill':
        tasks = gameplay.tasks.refillPotionsChecker.makeRefillTasks(
            context, waypoint)
        return tasks
    elif waypoint['type'] == 'refillPotionsChecker':
        tasks = gameplay.tasks.refillPotionsChecker.makeRefillPotionsCheckerTasks(
            waypoint)
        return tasks
    elif waypoint['type'] == 'useRope':
        tasks = gameplay.tasks.useRope.makeUseRopeTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint)
        return tasks
    elif waypoint['type'] == 'useShovel':
        tasks = gameplay.tasks.useShovel.makeUseShovelTasks(
            context, context['waypoints']['state']['goalCoordinate'], waypoint)
        return tasks
