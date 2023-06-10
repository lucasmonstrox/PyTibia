import numpy as np
from time import time
from src.shared.typings import Coordinate
from src.utils.coordinate import getDirectionBetweenCoordinates
from src.utils.keyboard import press
from ...typings import Context
from .common.base import BaseTask


class SingleWalkPressTask(BaseTask):
    def __init__(self, context: Context, coordinate: Coordinate):
        super().__init__()
        self.name = 'singleWalkPress'
        self.delayOfTimeout = (context['skills']['movementSpeed'] * 2) / 1000
        self.coordinate = coordinate

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        # TODO: improve clever code
        isStartingFromLastCoordinate = (context['radar']['lastCoordinateVisited'] is None or np.any(
            context['radar']['coordinate'] == context['radar']['lastCoordinateVisited']) == True) == False
        return isStartingFromLastCoordinate

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        direction = getDirectionBetweenCoordinates(context['radar']['coordinate'], self.coordinate)
        press(direction)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = np.all(context['radar']['coordinate'] == self.coordinate) == True
        return didTask

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        self.parentTask.status = 'completed'
        self.parentTask.finishedAt = time()
        return context
