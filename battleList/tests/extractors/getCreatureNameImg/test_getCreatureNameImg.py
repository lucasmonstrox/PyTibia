import numpy as np
import pathlib
from battleList.extractors import getCreatureNameImg
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()


def getImages(creatureName: str):
    slotImg = utils.image.loadAsGrey(
        f'{currentPath}/slotsImgs/{creatureName}.png')
    nameImg = utils.image.loadAsGrey(
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


def test_should_assert_Alptramun():
    creatureNameImg, nameImg = getImages('Alptramun')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Amazon():
    creatureNameImg, nameImg = getImages('Amazon')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_An_Astral_Glyph():
    creatureNameImg, nameImg = getImages('An Astral Glyph')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_An_Observer_Eye():
    creatureNameImg, nameImg = getImages('An Observer Eye')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ancient_Lion_Archer():
    creatureNameImg, nameImg = getImages('Ancient Lion Archer')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ancient_Lion_Knight():
    creatureNameImg, nameImg = getImages('Ancient Lion Knight')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ancient_Lion_Warlock():
    creatureNameImg, nameImg = getImages('Ancient Lion Warlock')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ancient_Scarab():
    creatureNameImg, nameImg = getImages('Ancient Scarab')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ancient_Spawn_Of_Morgathla():
    creatureNameImg, nameImg = getImages('Ancient Spawn Of Morgathla')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Angry_Adventurer():
    creatureNameImg, nameImg = getImages('Angry Adventurer')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Angry_Demon():
    creatureNameImg, nameImg = getImages('Angry Demon')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Angry_Plant():
    creatureNameImg, nameImg = getImages('Angry Plant')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Clomp():
    creatureNameImg, nameImg = getImages('Animated Clomp')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Cyclops():
    creatureNameImg, nameImg = getImages('Animated Cyclops')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Feather():
    creatureNameImg, nameImg = getImages('Animated Feather')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Guzzlemaw():
    creatureNameImg, nameImg = getImages('Animated Guzzlemaw')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Moohtant():
    creatureNameImg, nameImg = getImages('Animated Moohtant')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Mummy():
    creatureNameImg, nameImg = getImages('Animated Mummy')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Ogre_Brute():
    creatureNameImg, nameImg = getImages('Animated Ogre Brute')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Ogre_Savage():
    creatureNameImg, nameImg = getImages('Animated Ogre Savage')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Ogre_Savage():
    creatureNameImg, nameImg = getImages('Animated Ogre Savage')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Ogre_Shaman():
    creatureNameImg, nameImg = getImages('Animated Ogre Shaman')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Rotworm():
    creatureNameImg, nameImg = getImages('Animated Rotworm')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Skunk():
    creatureNameImg, nameImg = getImages('Animated Skunk')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Snowman():
    creatureNameImg, nameImg = getImages('Animated Snowman')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Animated_Sword():
    creatureNameImg, nameImg = getImages('Animated Sword')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Annihilon():
    creatureNameImg, nameImg = getImages('Annihilon')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Anomaly():
    creatureNameImg, nameImg = getImages('Anomaly')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Apprentice_Sheng():
    creatureNameImg, nameImg = getImages('Apprentice Sheng')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Arachir_The_Ancient_One():
    creatureNameImg, nameImg = getImages('Arachir The Ancient One')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Arachnophobica():
    creatureNameImg, nameImg = getImages('Arachnophobica')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Arctic_Faun():
    creatureNameImg, nameImg = getImages('Arctic Faun')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Armadile():
    creatureNameImg, nameImg = getImages('Armadile')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Armenius():
    creatureNameImg, nameImg = getImages('Armenius')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ascending_Ferumbras():
    creatureNameImg, nameImg = getImages('Ascending Ferumbras')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Ashmunrah():
    creatureNameImg, nameImg = getImages('Ashmunrah')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Askarak_Demon():
    creatureNameImg, nameImg = getImages('Askarak Demon')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Askarak_Lord():
    creatureNameImg, nameImg = getImages('Askarak Lord')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Askarak_Prince():
    creatureNameImg, nameImg = getImages('Askarak Prince')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Assassin():
    creatureNameImg, nameImg = getImages('Assassin')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Avalanche():
    creatureNameImg, nameImg = getImages('Avalanche')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Axeitus_Headbanger():
    creatureNameImg, nameImg = getImages('Axeitus Headbanger')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Azure_Frog():
    creatureNameImg, nameImg = getImages('Azure Frog')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Baby_Dragon():
    creatureNameImg, nameImg = getImages('Baby Dragon')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Bad_Dream():
    creatureNameImg, nameImg = getImages('Bad Dream')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Badger():
    creatureNameImg, nameImg = getImages('Badger')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Baleful_Bunny():
    creatureNameImg, nameImg = getImages('Baleful Bunny')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Bandit():
    creatureNameImg, nameImg = getImages('Bandit')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Bane_Bringer():
    creatureNameImg, nameImg = getImages('Bane Bringer')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Banshee():
    creatureNameImg, nameImg = getImages('Banshee')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Barbaria():
    creatureNameImg, nameImg = getImages('Barbaria')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Barbarian_Bloodwalker():
    creatureNameImg, nameImg = getImages('Barbarian Bloodwalker')
    np.testing.assert_array_equal(creatureNameImg, nameImg)


def test_should_assert_Barbarian_Brutetamer():
    creatureNameImg, nameImg = getImages('Barbarian Brutetamer')
    np.testing.assert_array_equal(creatureNameImg, nameImg)

