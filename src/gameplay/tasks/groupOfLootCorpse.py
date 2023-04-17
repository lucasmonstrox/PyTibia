import numpy as np
from scipy.spatial import distance
from src.features.radar.types import coordinateType
from ..factories.makeLootCorpse import makeLootCorpseTask
from ..factories.makeWalk import makeWalkTask
from ..typings import taskType
from ..waypoint import generateFloorWalkpoints
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfLootCorpseTasks(GroupTaskExecutor):
    def __init__(self, context, corpose):
        super().__init__()
        self.name = 'groupOfLootCorpse'
        self.tasks = self.generateTasks(context, corpose)
        self.value = corpose

    def generateTasks(self, context, corpose):
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([], dtype=taskType)
        tasks = np.append(tasks, [tasksToAppend])
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        for monster in context['monsters']:
            monsterCoordinateTuple = (monster['coordinate'][0], monster['coordinate'][1], monster['coordinate'][2])
            coordinatesToAppend = np.array([monsterCoordinateTuple], dtype=coordinateType)
            nonWalkableCoordinates = np.append(nonWalkableCoordinates, coordinatesToAppend)
        hudHeight, hudWidth  = context['hud']['img'].shape
        hudCenter = (hudWidth // 2, hudHeight // 2)
        monsterHudCoordinate = context['cavebot']['closestCreature']['hudCoordinate']
        moduleX = abs(hudCenter[0] - monsterHudCoordinate[0])
        moduleY = abs(hudCenter[1] - monsterHudCoordinate[1])
        dist = distance.cdist([context['radar']['coordinate']], [context['cavebot']['closestCreature']['coordinate']]).flatten()[0]
        walkpoints = []
        if dist < 2:
            if moduleX > 64 or moduleY > 64:
                walkpoints.append(context['cavebot']['closestCreature']['coordinate'])
        else:
            walkpoints = generateFloorWalkpoints(
                context['radar']['coordinate'], context['cavebot']['closestCreature']['coordinate'], nonWalkableCoordinates=nonWalkableCoordinates)
            hasWalkpoints = len(walkpoints) > 0
            if hasWalkpoints:
                walkpoints.pop()
        for walkpoint in walkpoints:
            walkpointTask = makeWalkTask(context, walkpoint)
            taskToAppend = np.array([walkpointTask], dtype=taskType)
            tasks = np.append(tasks, [taskToAppend])
        lootCorpseTasks = makeLootCorpseTask(corpose)
        lootCorpseTaskToAppend = np.array([lootCorpseTasks], dtype=taskType)
        tasks = np.append(tasks, [lootCorpseTaskToAppend])
        return tasks
