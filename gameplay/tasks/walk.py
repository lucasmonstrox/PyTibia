import numpy as np
import pyautogui
from time import time
from radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from skills.core import getSpeed
from utils.coordinate import getDirectionBetweenCoordinates
from .baseTask import BaseTask


class WalkTask(BaseTask):
    def __init__(self, context, value):
        super().__init__()
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(value)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.name = 'walk'
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
        hasMoreTasks = len(context['currentTask'].tasks) > 1
        if hasMoreTasks:
            freeTaskIndex = None
            for taskIndex, taskWithName in enumerate(context['currentTask'].tasks):
                _, possibleFreeTask = taskWithName
                if possibleFreeTask.status != 'completed':
                    freeTaskIndex = taskIndex
                    break
            if freeTaskIndex != None and (freeTaskIndex + 1) < len(context['currentTask'].tasks):
                hasMoreWalkpointTasks = context['currentTask'].tasks[freeTaskIndex + 1]['type'] == 'walk'
                if hasMoreWalkpointTasks:
                    _, nextTask = context['currentTask'].tasks[freeTaskIndex + 1]
                    futureDirection = getDirectionBetweenCoordinates(walkpoint, nextTask.value)
        if direction != futureDirection:
            if context['lastPressedKey'] is not None:
                pyautogui.keyUp(context['lastPressedKey'])
                context['lastPressedKey'] = None
            else:
                pyautogui.press(direction)
            return context
        filterByWalkTasks = context['currentTask'].tasks['type'] == 'walk'
        walkTasks = context['currentTask'].tasks[filterByWalkTasks]
        walkTasksLength = len(walkTasks)
        if direction != context['lastPressedKey']:
            if walkTasksLength > 2:
                pyautogui.keyDown(direction)
                context['lastPressedKey'] = direction
            else:
                pyautogui.press(direction)
            return context
        if walkTasksLength == 1 and context['lastPressedKey'] is not None:
            pyautogui.keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context

    def did(self, context):
        nextWalkpoint = self.value
        did = np.all(context['coordinate'] == nextWalkpoint) == True
        return did

    def onDidTimeout(self, context):
        context['currentTask'].status = 'completed'
        context['currentTask'].finishedAt = time()
        return context
