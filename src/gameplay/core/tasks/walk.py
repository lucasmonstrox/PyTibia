import numpy as np
from time import time
from src.repositories.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.repositories.skills.core import getSpeed
from src.shared.typings import Coordinate
from src.utils.coordinate import getDirectionBetweenCoordinates
from src.utils.keyboard import keyDown, keyUp, press
from ...typings import Context
from .common.base import BaseTask


class WalkTask(BaseTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        self.name = 'walk'
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(coordinate)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.walkpoint = coordinate

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
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
        if self.parentTask and len(self.parentTask.tasks) > 1:
            if self.parentTask.currentTaskIndex + 1 < len(self.parentTask.tasks):
                nextTask = self.parentTask.tasks[self.parentTask.currentTaskIndex + 1]
                futureDirection = getDirectionBetweenCoordinates(self.walkpoint, nextTask.walkpoint)
        if direction != futureDirection:
            if context['lastPressedKey'] is not None:
                keyUp(context['lastPressedKey'])
                context['lastPressedKey'] = None
            else:
                press(direction)
            return context
        walkTasksLength = len(self.parentTask.tasks)
        if direction != context['lastPressedKey']:
            if walkTasksLength > 2:
                keyDown(direction)
                context['lastPressedKey'] = direction
            else:
                press(direction)
            return context
        if walkTasksLength == 1 and context['lastPressedKey'] is not None:
            keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        # TODO: numbait
        didTask = np.all(context['radar']['coordinate'] == self.walkpoint) == True
        return didTask

    # TODO: add unit tests
    def onInterrupt(self, context: Context) -> Context:
        if context['lastPressedKey'] is not None:
            keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        return context

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        if context['lastPressedKey'] is not None:
            keyUp(context['lastPressedKey'])
            context['lastPressedKey'] = None
        # TODO: avoid this, tree should not be reseted manually
        context['tasksOrchestrator'].reset()
        return context
    
