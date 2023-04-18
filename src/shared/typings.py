from nptyping import NDArray
from typing import Any, List, Tuple


BBox = Tuple[int, int, int, int]
Coordinate = Tuple[int, int, int]
CoordinateList = List[Coordinate]
# TODO: fix it
GrayImage = NDArray[Any, Any]
# TODO: fix it
GrayVector = NDArray[Any, Any]
Slot = Tuple[int, int]
Waypoint = Any
WaypointList = List[Waypoint]
XYCoordinate = Tuple[int, int]
XYCoordinateList = List[Coordinate]