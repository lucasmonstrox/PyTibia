import src.gameplay.utils as gameplayUtils
from src.repositories.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.repositories.skills.core import getSpeed
from src.shared.typings import Coordinate
from src.utils.coordinate import getDirectionBetweenCoordinates
from src.utils.keyboard import keyDown, press
from ...typings import Context
from ...utils import releaseKeys
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
        self.shouldTimeoutTreeWhenTimeout = True
        self.walkpoint = coordinate

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        if context['radar']['lastCoordinateVisited'] is None:
            return True
        return not gameplayUtils.coordinatesAreEqual(context['radar']['coordinate'], context['radar']['lastCoordinateVisited'])

    # TODO: add unit tests
    def do(self, context: Context) -> bool:
        direction = getDirectionBetweenCoordinates(
            context['radar']['coordinate'], self.walkpoint)
        if direction is None:
            return context
        futureDirection = None
        if self.parentTask and len(self.parentTask.tasks) > 1:
            if self.parentTask.currentTaskIndex + 1 < len(self.parentTask.tasks):
                futureDirection = getDirectionBetweenCoordinates(
                    self.walkpoint, self.parentTask.tasks[self.parentTask.currentTaskIndex + 1].walkpoint)
        if direction != futureDirection:
            if context['lastPressedKey'] is not None:
                context = releaseKeys(context)
            else:
                press(direction)
            return context
        if direction != context['lastPressedKey']:
            if len(self.parentTask.tasks) > 2:
                keyDown(direction)
                context['lastPressedKey'] = direction
            else:
                press(direction)
            return context
        if len(self.parentTask.tasks) == 1 and context['lastPressedKey'] is not None:
            context = releaseKeys(context)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        return gameplayUtils.coordinatesAreEqual(context['radar']['coordinate'], self.walkpoint)

    # TODO: add unit tests
    def onInterrupt(self, context: Context) -> Context:
        return releaseKeys(context)

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        return releaseKeys(context)
