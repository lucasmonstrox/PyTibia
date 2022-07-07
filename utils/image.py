import numpy as np


def graysToBlack(arr):
    return np.where(np.logical_and(arr >= 50, arr <= 100), 0, arr)
