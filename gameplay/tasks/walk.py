import numpy as np
import pyautogui
from time import time
import gameplay.typings
import gameplay.waypoint
import utils.coordinate
import utils.array


class WalkTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'walk'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: improve clever code
        isStartingFromLastCoordinate = (context['lastCoordinateVisited'] is None or np.any(
            context['coordinate'] == context['lastCoordinateVisited']) == True) == False
        return isStartingFromLastCoordinate

    def do(self, context):
        walkpoint = self.value
        hasMoreWalkpointTasks = len(
            context['currentGroupTask'].tasks) > 1 and context['currentGroupTask'].tasks[1]['type'] == 'walk'
        direction = utils.coordinate.getDirectionBetweenCoordinates(
            context['coordinate'], walkpoint)
        hasNoNewDirection = direction is None
        if hasNoNewDirection:
            return context
        futureDirection = None
        if hasMoreWalkpointTasks:
            _, nextTask = context['currentGroupTask'].tasks[1]
            futureDirection = utils.coordinate.getDirectionBetweenCoordinates(
                walkpoint, nextTask.value)
        if direction != futureDirection:
            if context['lastPressedKey'] is not None:
                pyautogui.keyUp(context['lastPressedKey'])
                context['lastPressedKey'] = None
            else:
                pyautogui.press(direction)
            return context
        else:
            filterByWalkTasks = context['currentGroupTask'].tasks['type'] == 'walk'
            walkTasks = context['currentGroupTask'].tasks[filterByWalkTasks]
            walkTasksLength = len(walkTasks)
            if direction != context['lastPressedKey']:
                if walkTasksLength > 2:
                    pyautogui.keyDown(direction)
                    context['lastPressedKey'] = direction
                else:
                    pyautogui.press(direction)
            elif walkTasksLength == 1:
                if context['lastPressedKey'] is not None:
                    pyautogui.keyUp(context['lastPressedKey'])
                    context['lastPressedKey'] = None
        return context

    def did(self, context):
        nextwalkpoint = self.value
        response = np.all(context['coordinate'] == nextwalkpoint)
        did = response == True
        return did

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        if context['way'] == 'cavebot':
            return context
        result = context['coordinate'] == context['waypoints']['state']['checkInCoordinate']
        didReachWaypoint = np.all(result) == True
        if didReachWaypoint:
            context['waypoints']['state'] = None
            context['tasks'] = np.array([], dtype=gameplay.typings.taskType)
        return context
