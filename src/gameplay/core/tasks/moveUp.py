import pyautogui
from time import time
from ...typings import Context
from .common.base import BaseTask


class MoveUp(BaseTask):
    def __init__(self, context, direction: str):
        super().__init__()
        self.name = 'moveUp'
        self.isRootTask = True
        self.direction = direction
        self.floorLevel = context['radar']['coordinate'][2] - 1

    # TODO: add unit tests
    # TODO: improve this code
    def do(self, context: Context) -> bool:
        direction = None
        if self.direction == 'north':
            direction = 'up'
        if self.direction == 'south':
            direction = 'down'
        if self.direction == 'west':
            direction = 'left'
        if self.direction == 'east':
            direction = 'right'
        pyautogui.press(direction)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        didTask = context['radar']['coordinate'][2] == self.floorLevel
        return didTask

    # TODO: add unit tests
    def onDidTimeout(self, context: Context) -> Context:
        self.parentTask.status = 'completed'
        self.parentTask.status.finishedAt = time()
        return context
