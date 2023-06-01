import numpy as np
import pyautogui
from scipy.spatial import distance
from src.gameplay.typings import Context
from ...typings import Context
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class WalkToTargetCreature(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'WalkToTargetCreature'

    # TODO: add return type
    # TODO: add unit tests
    def initialize(self, context: Context):
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        for monster in context['gameWindow']['monsters']:
            if np.array_equal(monster['coordinate'], context['cavebot']['closestCreature']['coordinate']) == False:
                monsterCoordinateTuple = (monster['coordinate'][0], monster['coordinate'][1], monster['coordinate'][2])
                coordinatesToAppend = [monsterCoordinateTuple]
                nonWalkableCoordinates = np.append(nonWalkableCoordinates, coordinatesToAppend)
        dist = distance.cdist([context['radar']['coordinate']], [context['cavebot']['closestCreature']['coordinate']]).flatten()[0]
        walkpoints = []
        if dist < 2:
            gameWindowHeight, gameWindowWidth  = context['gameWindow']['img'].shape
            gameWindowCenter = (gameWindowWidth // 2, gameWindowHeight // 2)
            monsterGameWindowCoordinate = context['cavebot']['closestCreature']['gameWindowCoordinate']
            moduleX = abs(gameWindowCenter[0] - monsterGameWindowCoordinate[0])
            moduleY = abs(gameWindowCenter[1] - monsterGameWindowCoordinate[1])
            if moduleX > 64 or moduleY > 64:
                walkpoints.append(context['cavebot']['closestCreature']['coordinate'])
        else:
            walkpoints = generateFloorWalkpoints(
                context['radar']['coordinate'], context['cavebot']['closestCreature']['coordinate'], nonWalkableCoordinates=nonWalkableCoordinates)
            if len(walkpoints) > 0:
                walkpoints.pop()
        for walkpoint in walkpoints:
            self.tasks.append(WalkTask(context, walkpoint).setParentTask(self))
        return self

    def shouldRestart(self, _: Context) -> bool:
        # check if creature is moving
        return False

    def onBeforeRestart(self, context: Context) -> Context:
        if context['lastPressedKey'] is not None:
            pyautogui.keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context
