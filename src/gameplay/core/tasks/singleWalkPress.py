import numpy as np
import pyautogui
from time import time
from src.features.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.features.skills.core import getSpeed
from src.utils.coordinate import getDirectionBetweenCoordinates
from ...typings import Context
from .baseTask import BaseTask


class SingleWalkPressTask(BaseTask):
    # TODO: add types
    def __init__(self, context: Context, value):
        super().__init__()
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(value)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.name = 'singleWalkPress'
        self.value = value

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        # TODO: improve clever code
        isStartingFromLastCoordinate = (context['radar']['lastCoordinateVisited'] is None or np.any(
            context['radar']['coordinate'] == context['radar']['lastCoordinateVisited']) == True) == False
        return isStartingFromLastCoordinate

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        direction = getDirectionBetweenCoordinates(context['radar']['coordinate'], self.value)
        pyautogui.press(direction)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        nextWalkpoint = self.value
        did = np.all(context['radar']['coordinate'] == nextWalkpoint) == True
        return did

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        context['currentTask'].status = 'completed'
        context['currentTask'].finishedAt = time()
        return context
