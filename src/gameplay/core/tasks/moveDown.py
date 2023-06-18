from src.utils.keyboard import press
from ...typings import Context
from .common.base import BaseTask


class MoveDown(BaseTask):
    def __init__(self, context, direction: str):
        super().__init__()
        self.name = 'moveDown'
        self.isRootTask = True
        self.direction = direction
        self.floorLevel = context['radar']['coordinate'][2] + 1

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
        press(direction)
        return context

    # TODO: add unit tests
    def did(self, context: Context) -> bool:
        return context['radar']['coordinate'][2] == self.floorLevel
