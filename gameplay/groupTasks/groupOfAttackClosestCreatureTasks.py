import numpy as np
from scipy.spatial import distance
from time import time
from gameplay.factories.makeAttackClosestCreature import makeAttackClosestCreatureTask
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType
from gameplay.waypoint import generateFloorWalkpoints


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
        walkpoints = generateFloorWalkpoints(
            context['coordinate'], closestCreature['coordinate'])
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
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
