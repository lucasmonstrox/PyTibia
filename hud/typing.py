import numpy as np


creatureType = np.dtype([
    ('name', np.str_, 64),
    ('type', np.str_, 64),
    ('isBeingAttacked', np.bool_),
    ('slot', np.uint8, (2,)),
    ('coordinate', np.uint16, (3,)),
    ('windowCoordinate', np.uint32, (2,)),
    ('hudCoordinate', np.uint32, (2,)),
])