from nptyping import NDArray
from typing import Any, List, Tuple, Union


BBox = Tuple[int, int, int, int]
Coordinate = Tuple[int, int, int]
CoordinateList = List[Coordinate]
CreatureCategory = str
CreatureCategoryOrUnknown = Union[CreatureCategory, 'unknown']
Direction = Union['up', Union['down', Union['left', 'right']]]
# TODO: fix it
GrayImage = NDArray[Any, Any]
GrayPixel = int
# TODO: fix it
GrayVector = NDArray[Any, Any]
Slot = Tuple[int, int]
SlotWidth = 32 | 64
Waypoint = Any
WaypointList = List[Waypoint]
XYCoordinate = Tuple[int, int]
XYCoordinateList = List[Coordinate]