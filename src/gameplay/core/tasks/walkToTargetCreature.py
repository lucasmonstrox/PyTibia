import numpy as np
from scipy.spatial import distance
from src.gameplay.typings import Context
import src.gameplay.utils as gameplayUtils
from ...typings import Context
from ...utils import releaseKeys
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class WalkToTargetCreatureTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'walkToTargetCreature'
        self.manuallyTerminable = True
        self.targetCreatureCoordinateSinceLastRestart = None

    def onBeforeStart(self, context: Context) -> Context:
        self.calculatePathToTargetCreature(context)
        return context

    def onBeforeRestart(self, context: Context) -> Context:
        context = releaseKeys(context)
        return self.onBeforeStart(context)

    def onInterrupt(self, context: Context) -> Context:
        return releaseKeys(context)

    def onComplete(self, context: Context) -> Context:
        return releaseKeys(context)

    # TODO: if there are no more creatures, it should only recalculate when it gets close to the creature to avoid recalculating each SQM move
    def shouldRestart(self, context: Context) -> bool:
        if not self.tasks:
            return True
        if context['cavebot']['targetCreature'] is None:
            return True
        return not gameplayUtils.coordinatesAreEqual(context['cavebot']['targetCreature']['coordinate'], self.targetCreatureCoordinateSinceLastRestart)

    def shouldManuallyComplete(self, context: Context) -> bool:
        if context['cavebot']['isAttackingSomeCreature'] == False:
            return True
        return False

    def calculatePathToTargetCreature(self, context: Context):
        self.tasks = []
        if context['cavebot']['targetCreature'] is None:
            return
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        # TODO: also, detect players
        for monster in context['gameWindow']['monsters']:
            if np.array_equal(monster['coordinate'], context['cavebot']['targetCreature']['coordinate']) == False:
                nonWalkableCoordinates.append(monster['coordinate'])
        walkpoints = []
        dist = distance.cdist([context['radar']['coordinate']], [
                              context['cavebot']['targetCreature']['coordinate']]).flatten()[0]
        if dist < 2:
            gameWindowHeight, gameWindowWidth = context['gameWindow']['image'].shape
            gameWindowCenter = (gameWindowWidth // 2, gameWindowHeight // 2)
            monsterGameWindowCoordinate = context['cavebot']['targetCreature']['gameWindowCoordinate']
            moduleX = abs(gameWindowCenter[0] - monsterGameWindowCoordinate[0])
            moduleY = abs(gameWindowCenter[1] - monsterGameWindowCoordinate[1])
            if moduleX > 64 or moduleY > 64:
                walkpoints.append(context['cavebot']
                                  ['targetCreature']['coordinate'])
        else:
            walkpoints = generateFloorWalkpoints(
                context['radar']['coordinate'], context['cavebot']['targetCreature']['coordinate'], nonWalkableCoordinates=nonWalkableCoordinates)
            if walkpoints:
                walkpoints.pop()
        for walkpoint in walkpoints:
            self.tasks.append(WalkTask(context, walkpoint).setParentTask(
                self).setRootTask(self.rootTask))
        self.targetCreatureCoordinateSinceLastRestart = context['cavebot']['targetCreature']['coordinate'].copy(
        )
