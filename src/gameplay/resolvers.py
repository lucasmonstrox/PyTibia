from typing import Union
from src.shared.typings import Waypoint
from .core.tasks.baseTask import BaseTask
from .core.tasks.depositGold import DepositGoldTask
from .core.tasks.depositItems import DepositItemsTask
from .core.tasks.dropFlasks import DropFlasksTask
from .core.tasks.groupOfRefillChecker import GroupOfRefillCheckerTasks
from .core.tasks.groupOfRefillTasks import GroupOfRefillTasks
from .core.tasks.groupOfSingleWalk import GroupOfSingleWalkTasks
from .core.tasks.groupOfWalk import GroupOfWalkTasks
from .core.tasks.groupTaskExecutor import GroupTask
from .core.tasks.logout import LogoutTask
from .core.tasks.lureCreatures import LureCreaturesTask
from .core.tasks.useRopeWaypoint import UseRopeWaypointTask
from .core.tasks.useShovelWaypoint import UseShovelWaypointTask
from .typings import Context


# TODO: add unit tests
def resolveTasksByWaypoint(context: Context, waypoint: Waypoint) -> Union[BaseTask, GroupTask]:
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
