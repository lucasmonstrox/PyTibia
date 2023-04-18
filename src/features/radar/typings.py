import numpy as np


Coordinate = np.dtype([('x', np.uint16), ('y', np.uint16), ('z', np.uint16)])
CoordinateHash = np.dtype([('hash', str, 16), ('coordinate', np.uint16, (3,))])
# TODO: fix
FloorLevel = int
WaypointDistance = np.dtype([('index', np.uint16), ('distance', np.float32)])
Waypoint = np.dtype([
    ('label', np.str_, 64),
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('options', object),
])
