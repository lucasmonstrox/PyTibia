import numpy as np
from scipy.spatial import distance
from time import time
from ..factories.makeLootCorpse import makeLootCorpseTask
from ..factories.makeWalkTask import makeWalkTask
from ..typings import taskType
from ..waypoint import generateFloorWalkpoints
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfLootCorpseTasks(GroupTaskExecutor):
    def __init__(self, context, corpose):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfLootCorpse'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, corpose)
        self.value = corpose

    def generateTasks(self, context, corpose):
        tasks = np.array([], dtype=taskType)
        walkpoints = generateFloorWalkpoints(
            context['coordinate'], corpose['coordinate'], nonWalkableCoordinates=context['cavebot']['holesOrStairs'])
        hasWalkpoints = len(walkpoints) > 0
        if hasWalkpoints:
            walkpoints.pop()
        targetWaypoint = None
        if len(walkpoints) == 1:
            targetWaypoint = walkpoints[0]
        elif len(walkpoints) >= 2:
            targetWaypoint = walkpoints[1]
        if targetWaypoint:
            dist = distance.cdist([context['coordinate']], [targetWaypoint]).flatten()[0]
            if dist < 1.42:
                walkpoints.pop()
        for walkpoint in walkpoints:
            walkpointTask = makeWalkTask(context, walkpoint)
            taskToAppend = np.array([walkpointTask], dtype=taskType)
            tasks = np.append(tasks, [taskToAppend])
        lootCorpseTasks = makeLootCorpseTask(corpose)
        lootCorpseTaskToAppend = np.array([lootCorpseTasks], dtype=taskType)
        tasks = np.append(tasks, [lootCorpseTaskToAppend])
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
