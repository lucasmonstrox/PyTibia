from src.gameplay.typings import Context
from src.repositories.radar.typings import Coordinate
from src.utils.keyboard import keyUp
from ...typings import Context
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class WalkToCoordinate(VectorTask):
    def __init__(self, coordinate: Coordinate):
        super().__init__()
        self.name = 'walkToCoordinate'
        self.coordinate = coordinate

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        self.calculateWalkpoint(context)
        return context

    # TODO: add unit tests
    def onBeforeRestart(self, context: Context) -> Context:
        self.calculateWalkpoint(context)
        return context

    def onComplete(self, context: Context):
        if context['lastPressedKey'] is not None:
            keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context

    def shouldRestartAfterAllChildrensComplete(self, context: Context) -> bool:
        if len(self.tasks) == 0:
            return True
        if context['radar']['coordinate'][0] != self.coordinate[0]:
            return True
        if context['radar']['coordinate'][1] != self.coordinate[1]:
            return True
        if context['radar']['coordinate'][2] != self.coordinate[2]:
            return True
        return False

    def calculateWalkpoint(self, context: Context):
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        for monster in context['gameWindow']['monsters']:
            nonWalkableCoordinates.append(monster['coordinate'])
        self.tasks = []
        # TODO: make it yield
        for walkpoint in generateFloorWalkpoints(
            context['radar']['coordinate'], self.coordinate, nonWalkableCoordinates=nonWalkableCoordinates):
            self.tasks.append(WalkTask(context, walkpoint).setParentTask(self).setRootTask(self.rootTask))
