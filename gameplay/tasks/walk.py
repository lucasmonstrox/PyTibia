import numpy as np
import pyautogui
from time import time
from radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from skills.core import getSpeed
from utils.coordinate import getDirectionBetweenCoordinates


class WalkTask:
    def __init__(self, context, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(value)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
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
        direction = getDirectionBetweenCoordinates(context['coordinate'], walkpoint)
        hasNoNewDirection = direction is None
        if hasNoNewDirection:
            return context
        futureDirection = None
        hasMoreTasks = len(context['currentGroupTask'].tasks) > 1
        if hasMoreTasks:
            tasks = context['currentGroupTask'].tasks['type']
            freeTaskIndex = None
            for taskIndex, taskWithName in enumerate(context['currentGroupTask'].tasks):
                _, possibleFreeTask = taskWithName
                if possibleFreeTask.status != 'completed':
                    freeTaskIndex = taskIndex
                    break
            if freeTaskIndex != None and (freeTaskIndex + 1) < len(context['currentGroupTask'].tasks):
                hasMoreWalkpointTasks = context['currentGroupTask'].tasks[freeTaskIndex + 1]['type'] == 'walk'
                if hasMoreWalkpointTasks:
                    _, nextTask = context['currentGroupTask'].tasks[freeTaskIndex + 1]
                    futureDirection = getDirectionBetweenCoordinates(walkpoint, nextTask.value)
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

    def ping(self, context):
        return context

    def did(self, context):
        nextWalkpoint = self.value
        response = np.all(context['coordinate'] == nextWalkpoint)
        did = response == True
        return did

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        context['currentGroupTask'].status = 'completed'
        context['currentGroupTask'].finishedAt = time()
        return context
