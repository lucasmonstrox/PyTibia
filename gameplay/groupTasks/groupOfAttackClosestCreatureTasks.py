import numpy as np
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
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
