import numpy as np
import pyautogui
from time import time
import utils.coordinate


class WalkTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'walk'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: improve clever code
        isStartingFromLastCoordinate = (context['lastCoordinateVisited'] is None or np.any(
            context['radarCoordinate'] == context['lastCoordinateVisited']) == True) == False
        return isStartingFromLastCoordinate

    def do(self, context):
        copyOfContext = context.copy()
        walkpoint = self.value
        hasMoreWalkpointTasks = len(
            copyOfContext['tasks']) > 1 and copyOfContext['tasks'][1]['type'] == 'walk'
        direction = utils.coordinate.getDirectionBetweenRadarCoordinates(
            copyOfContext['radarCoordinate'], walkpoint)
        hasNoNewDirection = direction is None
        if hasNoNewDirection:
            return copyOfContext
        futureDirection = None
        if hasMoreWalkpointTasks:
            _, nextTask = copyOfContext['tasks'][1]
            futureDirection = utils.coordinate.getDirectionBetweenRadarCoordinates(
                walkpoint, nextTask.value)
        print('hasMoreWalkpointTasks', hasMoreWalkpointTasks)
        print('direction', direction)
        print('futureDirection', futureDirection)
        if direction != futureDirection:
            if copyOfContext['lastPressedKey'] is not None:
                print('keyUp')
                pyautogui.keyUp(copyOfContext['lastPressedKey'])
                copyOfContext['lastPressedKey'] = None
            else:
                print('press 1')
                pyautogui.press(direction)
            return copyOfContext
        else:
            filterByWalkTasks = copyOfContext['tasks']['type'] == 'walk'
            walkTasks = copyOfContext['tasks'][filterByWalkTasks]
            walkTasksLength = len(walkTasks)
            if direction != copyOfContext['lastPressedKey']:
                if walkTasksLength > 2:
                    print('keyDown 1')
                    pyautogui.keyDown(direction)
                    copyOfContext['lastPressedKey'] = direction
                else:
                    print('press 2')
                    pyautogui.press(direction)
            elif walkTasksLength == 1:
                if copyOfContext['lastPressedKey'] is not None:
                    pyautogui.keyUp(copyOfContext['lastPressedKey'])
                    print('keyUp 2')
                    copyOfContext['lastPressedKey'] = None
        return copyOfContext

    def did(self, context):
        nextwalkpoint = self.value
        response = np.all(context['radarCoordinate'] == nextwalkpoint)
        did = response == True
        return did

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
