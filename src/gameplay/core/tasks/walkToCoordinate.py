from src.gameplay.typings import Context
import src.gameplay.utils as gameplayUtils
from src.repositories.radar.typings import Coordinate
from ...typings import Context
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class WalkToCoordinateTask(VectorTask):
    def __init__(self, coordinate: Coordinate):
        super().__init__()
        self.name = 'walkToCoordinate'
        self.coordinate = coordinate

    def onBeforeStart(self, context: Context) -> Context:
        self.calculateWalkpoint(context)
        return context

    def onBeforeRestart(self, context: Context) -> Context:
        return self.onBeforeStart(context)

    def onComplete(self, context: Context):
        return gameplayUtils.releaseKeys(context)

    def shouldRestartAfterAllChildrensComplete(self, context: Context) -> bool:
        if len(self.tasks) == 0:
            return True
        if not gameplayUtils.coordinatesAreEqual(context['radar']['coordinate'], self.coordinate):
            return True
        return False

    # TODO: add unit tests
    def calculateWalkpoint(self, context: Context):
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        for monster in context['gameWindow']['monsters']:
            nonWalkableCoordinates.append(monster['coordinate'])
        self.tasks = []
        for walkpoint in generateFloorWalkpoints(
            context['radar']['coordinate'], self.coordinate, nonWalkableCoordinates=nonWalkableCoordinates):
            self.tasks.append(WalkTask(context, walkpoint).setParentTask(self).setRootTask(self.rootTask))
