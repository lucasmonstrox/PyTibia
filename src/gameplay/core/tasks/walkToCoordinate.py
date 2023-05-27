from src.repositories.radar.typings import Coordinate
from ...typings import Context
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class WalkToCoordinate(VectorTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'walkToCoordinate'
        self.value = coordinate
        self.tasks = self.generateTasks(context, self.value)

    # TODO: add return type
    # TODO: add unit tests
    def generateTasks(self, context: Context, waypointCoordinate: Coordinate):
        # nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        # for monster in context['gameWindow']['monsters']:
        #     monsterCoordinateTuple = (monster['coordinate'][0], monster['coordinate'][1], monster['coordinate'][2])
        #     coordinatesToAppend = np.array([monsterCoordinateTuple], dtype=Coordinate)
        #     nonWalkableCoordinates = np.append(nonWalkableCoordinates, coordinatesToAppend)
        tasks = []
        # TODO: make it yield
        for walkpoint in generateFloorWalkpoints(
            context['radar']['coordinate'], waypointCoordinate, nonWalkableCoordinates=None):
            tasks.append(WalkTask(context, walkpoint))
        return tasks
