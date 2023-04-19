from typing_extensions import TypedDict
from src.shared.typings import Coordinate
import numpy as np


Checkpoint = TypedDict('Checkpoint', {'goalCoordinate': Coordinate, 'checkInCoordinate': Coordinate})
Task = np.dtype([
    ('type', np.str_, 64),
    ('data', np.object_),
])