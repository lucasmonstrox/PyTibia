import numpy as np
import pathlib
from battleList.extractors import getCreatureNameImg
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()


def getImages(creatureName: str):
    slotImg = utils.image.loadAsArray(
        f'{currentPath}/slotsImgs/{creatureName}.png')
    nameImg = utils.image.loadAsArray(
        f'battleList/images/monsters/{creatureName}.png')
    creatureNameImg = getCreatureNameImg(slotImg)
    return creatureNameImg, nameImg


def test_should_assert_A_Greedy_Eye():
    creatureNameImg, nameImg = getImages('A Greedy Eye')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_A_Shielded_Astral_Glyph():
    creatureNameImg, nameImg = getImages('A Shielded Astral Glyph')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Abyssador():
    creatureNameImg, nameImg = getImages('Abyssador')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Achad():
    creatureNameImg, nameImg = getImages('Achad')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Acid_Blob():
    creatureNameImg, nameImg = getImages('Acid Blob')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Acolyte_Of_Darkness():
    creatureNameImg, nameImg = getImages('Acolyte Of Darkness')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Acolyte_Of_The_Cult():
    creatureNameImg, nameImg = getImages('Acolyte Of The Cult')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Adept_Of_The_Cult():
    creatureNameImg, nameImg = getImages('Adept Of The Cult')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Adult_Goanna():
    creatureNameImg, nameImg = getImages('Adult Goanna')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Adventurer():
    creatureNameImg, nameImg = getImages('Adventurer')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Aftershock():
    creatureNameImg, nameImg = getImages('Aftershock')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Aggressive_Lava():
    creatureNameImg, nameImg = getImages('Aggressive Lava')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Aggressive_Matter():
    creatureNameImg, nameImg = getImages('Aggressive Matter')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Agrestic_Chicken():
    creatureNameImg, nameImg = getImages('Agrestic Chicken')
    np.testing.assert_array_equal(creatureNameImg, nameImg)
