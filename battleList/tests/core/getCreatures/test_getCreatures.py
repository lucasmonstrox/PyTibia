import numpy as np
from battleList.core import getCreatures
from battleList.typing import creatureType


def test_should_return_None_when_cannot_get_content(mocker):
    mocker.patch('battleList.extractors.getContent', return_value=None)
    screenshot = np.array([], dtype=np.uint8)
    creatures = getCreatures(screenshot)
    assert creatures == None


def test_should_return_an_empty_array_when_filled_slots_count_is_zero(mocker):
    content = np.array([], dtype=np.uint8)
    mocker.patch('battleList.extractors.getContent', return_value=content)
    mocker.patch('battleList.extractors.getFilledSlotsCount', return_value=0)
    screenshot = np.array([], dtype=np.uint8)
    creatures = getCreatures(screenshot)
    emptyArrayOfCreatures = np.array([], dtype=creatureType)
    np.testing.assert_array_equal(creatures, emptyArrayOfCreatures)


def test_should_return_an_array_of_creatures_when_filled_slots_count_is_greater_than_zero(mocker):
    content = np.array([], dtype=np.uint8)
    creature = ('Rat', True)
    mocker.patch('battleList.extractors.getContent', return_value=content)
    mocker.patch('battleList.extractors.getFilledSlotsCount', return_value=1)
    mocker.patch('battleList.core.getCreatureFromSlot',
                 return_value=creature)
    screenshot = np.array([], dtype=np.uint8)
    creatures = getCreatures(screenshot)
    arrayOfCreatures = np.array([creature], dtype=creatureType)
    np.testing.assert_array_equal(creatures, arrayOfCreatures)
