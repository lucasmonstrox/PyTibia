from typing_extensions import TypedDict
from src.shared.typings import Coordinate


Checkpoint = TypedDict(
    'Checkpoint', {'goalCoordinate': Coordinate, 'checkInCoordinate': Coordinate})
