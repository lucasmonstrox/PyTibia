import numpy as np
from time import time
from wiki import cities
from gameplay.typings import taskType
# from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks


class DepositItemsTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.delayOfTimeout = None
        self.name = 'depositItems'
        self.status = 'notStarted'
        self.value = None

    def shouldIgnore(self, _):
        # getBackpackSlotImg(0)
        return False

    def do(self, context):
        # players = context['players']
        # playersCoordinates = players['coordinate']
        # currentCity = 'ankrahmun'
        # depotCoordinates = cities.cities[currentCity]['depotCoordinates'].copy(
        # )
        # occupiedDepositCoordinatesIndexes = np.nonzero(np.all(
        #     depotCoordinates == playersCoordinates, axis=1))[0]
        # freeDepositCoordinates = np.delete(
        #     depotCoordinates, occupiedDepositCoordinatesIndexes, axis=0)
        # # TODO: get closest coordinate
        # freeCoordinate = freeDepositCoordinates[0]
        # context['freeDepotCoordinates'] = freeCoordinate
        # floorTasks = makeGroupOfWalkpointTasks(context, freeCoordinate)
        # for floorTask in floorTasks:
        #     taskToAppend = np.array([floorTask], dtype=taskType)
        #     context['tasks'] = np.append(context['tasks'], [taskToAppend])
        return context

    def shouldRestart(self, _):
        return False

    def did(self, _):
        return True

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
