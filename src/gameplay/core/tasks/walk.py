import numpy as np
import pyautogui
from time import time
from src.repositories.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.repositories.skills.core import getSpeed
from src.shared.typings import Coordinate
from src.utils.coordinate import getDirectionBetweenCoordinates
from ...typings import Context
from .common.base import BaseTask


class WalkTask(BaseTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(coordinate)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.name = 'walk'
        self.walkpoint = coordinate

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        # TODO: improve clever code
        if context['radar']['lastCoordinateVisited'] is None:
            return True
        isStartingFromLastCoordinate = context['radar']['coordinate'][0] != context['radar']['lastCoordinateVisited'][0] and context['radar']['coordinate'][1] != context['radar']['lastCoordinateVisited'][1] and context['radar']['coordinate'][2] != context['radar']['lastCoordinateVisited'][2]
        return isStartingFromLastCoordinate

    # TODO: add unit tests
    def do(self, context: Context) -> bool:
        direction = getDirectionBetweenCoordinates(context['radar']['coordinate'], self.walkpoint)
        if direction is None:
            return context
        futureDirection = None
        if len(self.parentTask.tasks) > 1:
            freeTaskIndex = None
            for taskIndex, possibleFreeTask in enumerate(self.parentTask.tasks):
                if possibleFreeTask.status != 'completed':
                    freeTaskIndex = taskIndex
                    break
            if freeTaskIndex != None and (freeTaskIndex + 1) < len(self.parentTask.tasks):
                nextTask = self.parentTask.tasks[freeTaskIndex + 1]
                futureDirection = getDirectionBetweenCoordinates(self.walkpoint, nextTask.walkpoint)
        if direction != futureDirection:
            if context['lastPressedKey'] is not None:
                pyautogui.keyUp(context['lastPressedKey'])
                context['lastPressedKey'] = None
            else:
                pyautogui.press(direction)
            return context
        walkTasksLength = len(self.parentTask.tasks)
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
        # TODO: numbait
        didTask = np.all(context['radar']['coordinate'] == self.value) == True
        return didTask

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        context['taskOrchestrator'].getCurrentTask(context).status = 'completed'
        context['taskOrchestrator'].getCurrentTask(context).finishedAt = time()
        return context
