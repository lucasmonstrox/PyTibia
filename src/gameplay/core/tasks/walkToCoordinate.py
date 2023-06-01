from src.gameplay.typings import Context
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

    # TODO: add return type
    # TODO: add unit tests
    def initialize(self, context: Context):
        # nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        # for monster in context['gameWindow']['monsters']:
        #     monsterCoordinateTuple = (monster['coordinate'][0], monster['coordinate'][1], monster['coordinate'][2])
        #     coordinatesToAppend = np.array([monsterCoordinateTuple], dtype=Coordinate)
        #     nonWalkableCoordinates = np.append(nonWalkableCoordinates, coordinatesToAppend)
        self.tasks = []
        # TODO: make it yield
        walkpoints = generateFloorWalkpoints(
            context['radar']['coordinate'], self.value, nonWalkableCoordinates=None)
        for walkpoint in walkpoints:
            self.tasks.append(WalkTask(context, walkpoint).setParentTask(self))
        return self
    
    def shouldRestart(self, _: Context) -> bool:
        # check if creature is moving
        return False
    
    def onBeforeRestart(self, context: Context):
        if context['lastPressedKey'] is not None:
            # pyautogui.keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context
