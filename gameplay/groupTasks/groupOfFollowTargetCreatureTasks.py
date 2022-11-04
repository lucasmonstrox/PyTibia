import numpy as np
from time import time
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType
from gameplay.waypoint import generateFloorWalkpoints


class GroupOfFollowTargetCreatureTasks(GroupTaskExecutor):
    def __init__(self, context, targetCreature):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfFollowTargetCreature'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, targetCreature)
        self.value = targetCreature

    def generateTasks(self, context, targetCreature):
        tasks = np.array([], dtype=taskType)
        walkpoints = generateFloorWalkpoints(
            context['coordinate'], targetCreature['coordinate'])
        hasWalkpoints = len(walkpoints) > 0
        if hasWalkpoints:
            walkpoints.pop()
        for walkpoint in walkpoints:
            walkpointTask = makeWalkTask(walkpoint)
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
