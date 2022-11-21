import numpy as np

coordinateHashType = np.dtype([('hash', str, 16), ('coordinate', np.uint16, (3,))])
coordinateType = np.dtype([
    ('x', np.uint16),
    ('y', np.uint16),
    ('z', np.uint16),
])
waypointDistanceType = np.dtype(
    [('index', np.uint16), ('distance', np.float32)])
waypointType = np.dtype([
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('tolerance', np.uint8),
    ('options', object),
])
