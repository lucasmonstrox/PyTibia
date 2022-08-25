import numpy as np


coordinateType = np.dtype([('hash', np.str, 16), ('coordinate', np.uint16, (3,))])
waypointDistanceType = np.dtype([('index', np.uint16), ('distance', np.float32)])
waypointType = np.dtype([
    ('type', np.str_, 64),
    ('coordinate', np.uint32, (3,)),
    ('tolerance', np.uint8)
])