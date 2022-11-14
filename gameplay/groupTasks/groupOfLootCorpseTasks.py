import numpy as np
from time import time
from gameplay.factories.makeLootCorpse import makeLootCorpseTask
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType
from gameplay.waypoint import generateFloorWalkpoints


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
            context['coordinate'], corpose['coordinate'])
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

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
