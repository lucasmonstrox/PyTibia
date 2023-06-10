from src.gameplay.core.waypoint import resolveGoalCoordinate
from src.gameplay.typings import Context
import src.repositories.gameWindow.creatures as gameWindowCreatures
from ...typings import Context
from .common.vector import VectorTask
from .walkToCoordinate import WalkToCoordinateTask


# Tarefas:
# - Se algum bicho parar perto da coordenada, ligar o target
# - Se levar trap, ligar o target
class LureWaypointTask(VectorTask):
    # TODO: add types
    def __init__(self, waypoint):
        super().__init__()
        self.name = 'lureWaypoint'
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.manuallyTerminable = True
        self.waypoint = waypoint

    def shouldManuallyComplete(self, context: Context) -> bool:
        return len(context['battleList']['creatures']) == 0

    # def ping(self, context: Context) -> Context:
    #     if gameWindowCreatures.isTrappedByCreatures(context['gameWindow']['monsters'], context['radar']['coordinate']):
    #         context['targeting']['enabled'] = True
    #     return context

    def onBeforeStart(self, context: Context) -> Context:
        context['targeting']['enabled'] = False
        self.tasks = [
            WalkToCoordinateTask(self.waypoint['coordinate']).setParentTask(self).setRootTask(self),
        ]
        return context

    def onComplete(self, context: Context) -> Context:
        # nextWaypointIndex = getNextArrayIndex(
        #     context['cavebot']['waypoints']['points'], context['cavebot']['waypoints']['currentIndex'])
        # context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
        # currentWaypoint = context['cavebot']['waypoints']['points'][context['cavebot']['waypoints']['currentIndex']]
        # context['cavebot']['waypoints']['state'] = resolveGoalCoordinate(context['radar']['coordinate'], currentWaypoint)
        return context