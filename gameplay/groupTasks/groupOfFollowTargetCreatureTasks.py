import numpy as np
from scipy.spatial import distance
from time import time
from ..factories.makeWalkTask import makeWalkTask
from ..groupTasks.groupTaskExecutor import GroupTaskExecutor
from ..typings import taskType
from ..waypoint import generateFloorWalkpoints


class GroupOfFollowTargetCreatureTasks(GroupTaskExecutor):
    def __init__(self, context, targetCreature):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfFollowTargetCreature'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, targetCreature)
        self.value = targetCreature

    def generateTasks(self, context, targetCreature):
        tasks = np.array([], dtype=taskType)
        walkpoints = generateFloorWalkpoints(
            context['coordinate'], targetCreature['coordinate'], nonWalkableCoordinates=context['cavebot']['holesOrStairs'])
        hasWalkpoints = len(walkpoints) > 0
        if hasWalkpoints:
            walkpoints.pop()
        targetWaypoint = None
        if len(walkpoints) == 1:
            targetWaypoint = walkpoints[0]
        elif len(walkpoints) == 2:
            targetWaypoint = walkpoints[1]
        if targetWaypoint:
            dist = distance.cdist([context['coordinate']], [targetWaypoint]).flatten()[0]
            if dist < 1.42:
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
