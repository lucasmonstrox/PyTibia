import numpy as np
from nptyping import NDArray
from typing import Any


Creature = np.dtype([('name', np.str_, 64), ('isBeingAttacked', np.bool_)])
# TODO: fix it
CreatureList = NDArray[Any, Any]
