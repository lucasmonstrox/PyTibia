import numpy as np
import pyautogui
from time import time
from src.repositories.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.repositories.skills.core import getSpeed
from src.shared.typings import Coordinate
from src.utils.coordinate import getDirectionBetweenCoordinates
from ...typings import Context
from .baseTask import BaseTask


class WalkTask(BaseTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(coordinate)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.name = 'walk'
        self.value = coordinate

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        # TODO: improve clever code
        if context['radar']['lastCoordinateVisited'] is None:
            return True
        isStartingFromLastCoordinate = context['radar']['coordinate'][0] != context['radar']['lastCoordinateVisited'][0] and context['radar']['coordinate'][1] != context['radar']['lastCoordinateVisited'][1] and context['radar']['coordinate'][2] != context['radar']['lastCoordinateVisited'][2]
        return isStartingFromLastCoordinate

    # TODO: add unit tests
    def do(self, context: Context) -> bool:
        walkpoint = self.value
        direction = getDirectionBetweenCoordinates(context['radar']['coordinate'], walkpoint)
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

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        nextWalkpoint = self.value
        didTask = np.all(context['radar']['coordinate'] == nextWalkpoint) == True
        return didTask

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        context['currentTask'].status = 'completed'
        context['currentTask'].finishedAt = time()
        return context
