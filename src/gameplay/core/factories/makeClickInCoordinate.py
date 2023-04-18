from typing import Tuple
from src.shared.typings import Coordinate
from ..tasks.clickInCoordinate import ClickInCoordinateTask


# TODO: add unit tests
def makeClickInCoordinateTask(coordinate: Coordinate) -> Tuple[str, ClickInCoordinateTask]:
    task = ClickInCoordinateTask(coordinate)
    return ('clickInCoordinate', task)
