import numpy as np


Coordinate = np.dtype([('x', np.uint16), ('y', np.uint16), ('z', np.uint16)])
CoordinateHash = np.dtype([('hash', str, 16), ('coordinate', np.uint16, (3,))])
# TODO: fix
FloorLevel = int
TileFriction = 70 | 90 | 95 | 100 | 110 | 125 | 140 | 150 | 160 | 200 | 250
WaypointDistance = np.dtype([('index', np.uint16), ('distance', np.float32)])
Waypoint = np.dtype([
    ('label', np.str_, 64),
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('options', object),
])
