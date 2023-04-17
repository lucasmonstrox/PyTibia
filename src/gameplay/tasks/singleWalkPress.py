import numpy as np
import pyautogui
from time import time
from src.features.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.features.skills.core import getSpeed
from src.utils.coordinate import getDirectionBetweenCoordinates
from .baseTask import BaseTask


class SingleWalkPressTask(BaseTask):
    def __init__(self, context, value):
        super().__init__()
        charSpeed = getSpeed(context['screenshot'])
        tileFriction = getTileFrictionByCoordinate(value)
        movementSpeed = getBreakpointTileMovementSpeed(
            charSpeed, tileFriction)
        self.delayOfTimeout = (movementSpeed * 2) / 1000
        self.name = 'singleWalkPress'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: improve clever code
        isStartingFromLastCoordinate = (context['lastCoordinateVisited'] is None or np.any(
            context['radar']['coordinate'] == context['lastCoordinateVisited']) == True) == False
        return isStartingFromLastCoordinate

    def do(self, context):
        direction = getDirectionBetweenCoordinates(context['radar']['coordinate'], self.value)
        pyautogui.press(direction)
        return context

    def did(self, context):
        nextWalkpoint = self.value
        did = np.all(context['radar']['coordinate'] == nextWalkpoint) == True
        return did

    def onDidTimeout(self, context):
        context['currentTask'].status = 'completed'
        context['currentTask'].finishedAt = time()
        return context
