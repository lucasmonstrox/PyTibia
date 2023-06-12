from src.utils.array import getNextArrayIndex


def test_should_return_1_when_current_array_index_is_0():
    items = [0, 1, 2]
    currentIndex = 0
    assert getNextArrayIndex(items, currentIndex) == 1

def test_should_return_2_when_current_array_index_is_1():
    items = [0, 1, 2]
    currentIndex = 1
    assert getNextArrayIndex(items, currentIndex) == 2

def test_should_return_0_when_current_array_index_is_last_index():
    items = [0, 1, 2]
    currentIndex = 2
    assert getNextArrayIndex(items, currentIndex) == 0
