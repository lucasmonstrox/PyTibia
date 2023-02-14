import numpy as np
from scipy.spatial import distance
from time import time
from gameplay.factories.makeAttackClosestCreature import makeAttackClosestCreatureTask
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType
from gameplay.waypoint import generateFloorWalkpoints
from radar.types import coordinateType


class GroupOfAttackClosestCreatureTasks(GroupTaskExecutor):
    def __init__(self, context, closestCreature):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfAttackClosestCreature'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, closestCreature)
        self.value = closestCreature

    def generateTasks(self, context, closestCreature):
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([
            makeAttackClosestCreatureTask(closestCreature),
        ], dtype=taskType)
        tasks = np.append(tasks, [tasksToAppend])
        nonWalkableCoordinates = context['cavebot']['holesOrStairs'].copy()
        for monster in context['monsters']:
            if np.array_equal(monster['coordinate'], closestCreature['coordinate']) == False:
                monsterCoordinateTuple = (monster['coordinate'][0], monster['coordinate'][1], monster['coordinate'][2])
                coordinatesToAppend = np.array([monsterCoordinateTuple], dtype=coordinateType)
                nonWalkableCoordinates = np.append(nonWalkableCoordinates, coordinatesToAppend)
        hudHeight, hudWidth  = context['hudImg'].shape
        hudCenter = (hudWidth // 2, hudHeight // 2)
        monsterHudCoordinate = closestCreature['hudCoordinate']
        moduleX = abs(hudCenter[0] - monsterHudCoordinate[0])
        moduleY = abs(hudCenter[1] - monsterHudCoordinate[1])
        dist = distance.cdist([context['coordinate']], [closestCreature['coordinate']]).flatten()[0]
        walkpoints = []
        if dist < 2:
            if moduleX > 64 or moduleY > 64:
                walkpoints.append(closestCreature['coordinate'])
        else:
            walkpoints = generateFloorWalkpoints(
                context['coordinate'], closestCreature['coordinate'], nonWalkableCoordinates=nonWalkableCoordinates)
            hasWalkpoints = len(walkpoints) > 0
            if hasWalkpoints:
                walkpoints.pop()
        for walkpoint in walkpoints:
            walkpointTask = makeWalkTask(context, walkpoint)
            taskToAppend = np.array([walkpointTask], dtype=taskType)
            tasks = np.append(tasks, [taskToAppend])
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
