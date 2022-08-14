import numpy as np
from nptyping import Int8, NDArray, Shape, Structure
from typing import Any


creatureType = np.dtype([('name', np.str_, 64), ('isBeingAttacked', np.bool_)])
CREATURE = Structure["name: Str, isBeingAttacked: Bool"]
CREATURE_LIST = NDArray[Any, CREATURE]
UINT8_VECTOR = NDArray[Any, Int8]
CREATURE_NAME_IMG = NDArray[Shape["11, 131"], Int8]
SLOT_IMG = NDArray[Shape["20, 156"], Int8]
