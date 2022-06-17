import numpy as np


coordinateType = np.dtype([('hash', np.str, 16), ('coordinate', np.uint16, (3,))])
waypointDistanceType = np.dtype([('index', np.uint16), ('distance', np.float32)])