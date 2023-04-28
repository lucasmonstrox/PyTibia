import pathlib
from src.repositories.battleList.core import getCreaturesNames
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def getCreatureNameFromCreatureNameImage(creatureName, highlight=False):
    resolvedCreatureName = f'{creatureName} Highlight' if highlight else creatureName
    slotImg = loadFromRGBToGray(
        f'{currentPath}/slotsImages/{resolvedCreatureName}.png')
    creatureName = [creature for creature in getCreaturesNames(slotImg, 1)][0]
    return creatureName


def test_should_assert_A_Greedy_Eye():
    expectedCreatureName = 'A Greedy Eye'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_A_Greedy_Eye_with_highlight():
    expectedCreatureName = 'A Greedy Eye'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_A_Shielded_Astral_Glyph():
    expectedCreatureName = 'A Shielded Astral Glyph'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_A_Shielded_Astral_Glyph_with_highlight():
    expectedCreatureName = 'A Shielded Astral Glyph'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Abyssador():
    expectedCreatureName = 'Abyssador'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Abyssador_with_highlight():
    expectedCreatureName = 'Abyssador'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Abyssal_Calamary():
    expectedCreatureName = 'Abyssal Calamary'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Abyssal_Calamary_with_highlight():
    expectedCreatureName = 'Abyssal Calamary'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Achad():
    expectedCreatureName = 'Achad'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Achad_with_highlight():
    expectedCreatureName = 'Achad'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Acid_Blob():
    expectedCreatureName = 'Acid Blob'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Acid_Blob_with_highlight():
    expectedCreatureName = 'Acid Blob'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Acolyte_Of_Darkness():
    expectedCreatureName = 'Acolyte Of Darkness'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Acolyte_Of_Darkness_with_highlight():
    expectedCreatureName = 'Acolyte Of Darkness'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Acolyte_Of_The_Cult():
    expectedCreatureName = 'Acolyte Of The Cult'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Acolyte_Of_The_Cult_with_highlight():
    expectedCreatureName = 'Acolyte Of The Cult'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Adept_Of_The_Cult():
    expectedCreatureName = 'Adept Of The Cult'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Adept_Of_The_Cult_with_highlight():
    expectedCreatureName = 'Adept Of The Cult'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Adult_Goanna():
    expectedCreatureName = 'Adult Goanna'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Adult_Goanna_with_highlight():
    expectedCreatureName = 'Adult Goanna'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Adventurer():
    expectedCreatureName = 'Adventurer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Adventurer_with_highlight():
    expectedCreatureName = 'Adventurer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Aftershock():
    expectedCreatureName = 'Aftershock'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Aftershock_with_highlight():
    expectedCreatureName = 'Aftershock'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Aggressive_Lava():
    expectedCreatureName = 'Aggressive Lava'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Agressive_Lava_with_highlight():
    expectedCreatureName = 'Aggressive Lava'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Aggressive_Matter():
    expectedCreatureName = 'Aggressive Matter'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Agressive_Matter_with_highlight():
    expectedCreatureName = 'Aggressive Matter'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Agrestic_Chicken():
    expectedCreatureName = 'Agrestic Chicken'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Agrestic_Chicken_with_highlight():
    expectedCreatureName = 'Agrestic Chicken'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Alptramun():
    expectedCreatureName = 'Alptramun'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Alptramun_with_highlight():
    expectedCreatureName = 'Alptramun'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Amazon():
    expectedCreatureName = 'Amazon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Amazon_with_highlight():
    expectedCreatureName = 'Amazon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_An_Observer_Eye():
    expectedCreatureName = 'An Observer Eye'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_An_Observer_Eye_with_highlight():
    expectedCreatureName = 'An Observer Eye'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Archer():
    expectedCreatureName = 'Ancient Lion Archer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Archer_with_highlight():
    expectedCreatureName = 'Ancient Lion Archer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Knight():
    expectedCreatureName = 'Ancient Lion Knight'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Knight_with_highlight():
    expectedCreatureName = 'Ancient Lion Knight'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Warlock():
    expectedCreatureName = 'Ancient Lion Warlock'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Lion_Warlock_with_highlight():
    expectedCreatureName = 'Ancient Lion Warlock'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Scarab():
    expectedCreatureName = 'Ancient Scarab'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Scarab_with_highlight():
    expectedCreatureName = 'Ancient Scarab'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Spawn_Of_Morgathla():
    expectedCreatureName = 'Ancient Spawn Of Morgathla'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ancient_Spawn_Of_Morgathla_with_highlight():
    expectedCreatureName = 'Ancient Spawn Of Morgathla'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Adventurer():
    expectedCreatureName = 'Angry Adventurer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Adventurer_with_highlight():
    expectedCreatureName = 'Angry Adventurer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Demon():
    expectedCreatureName = 'Angry Demon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Demon_with_highlight():
    expectedCreatureName = 'Angry Demon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Plant():
    expectedCreatureName = 'Angry Plant'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Angry_Plant_with_highlight():
    expectedCreatureName = 'Angry Plant'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Clomp():
    expectedCreatureName = 'Animated Clomp'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Clomp_with_highlight():
    expectedCreatureName = 'Animated Clomp'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Cyclops():
    expectedCreatureName = 'Animated Cyclops'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Cyclops_with_highlight():
    expectedCreatureName = 'Animated Cyclops'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Feather():
    expectedCreatureName = 'Animated Feather'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Feather_with_highlight():
    expectedCreatureName = 'Animated Feather'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Guzzlemaw():
    expectedCreatureName = 'Animated Guzzlemaw'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Guzzlemaw_with_highlight():
    expectedCreatureName = 'Animated Guzzlemaw'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Moohtant():
    expectedCreatureName = 'Animated Moohtant'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Moohtant_with_highlight():
    expectedCreatureName = 'Animated Moohtant'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Mummy():
    expectedCreatureName = 'Animated Mummy'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Mummy_with_highlight():
    expectedCreatureName = 'Animated Mummy'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Brute():
    expectedCreatureName = 'Animated Ogre Brute'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Brute_with_highlight():
    expectedCreatureName = 'Animated Ogre Brute'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Savage():
    expectedCreatureName = 'Animated Ogre Savage'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Savage_with_highlight():
    expectedCreatureName = 'Animated Ogre Savage'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Shaman():
    expectedCreatureName = 'Animated Ogre Shaman'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Ogre_Shaman_with_highlight():
    expectedCreatureName = 'Animated Ogre Shaman'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Rotworm():
    expectedCreatureName = 'Animated Rotworm'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Rotworm_with_highlight():
    expectedCreatureName = 'Animated Rotworm'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Skunk():
    expectedCreatureName = 'Animated Skunk'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Skunk_with_highlight():
    expectedCreatureName = 'Animated Skunk'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Snowman():
    expectedCreatureName = 'Animated Snowman'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Snowman_with_highlight():
    expectedCreatureName = 'Animated Snowman'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Sword():
    expectedCreatureName = 'Animated Sword'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Animated_Sword_with_highlight():
    expectedCreatureName = 'Animated Sword'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Annihilon():
    expectedCreatureName = 'Annihilon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Annihilon_with_highlight():
    expectedCreatureName = 'Annihilon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Anomaly():
    expectedCreatureName = 'Anomaly'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Anomaly_with_highlight():
    expectedCreatureName = 'Anomaly'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Apprentice_Sheng():
    expectedCreatureName = 'Apprentice Sheng'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Apprentice_Sheng_with_highlight():
    expectedCreatureName = 'Apprentice Sheng'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Arachir_The_Ancient_One():
    expectedCreatureName = 'Arachir The Ancient One'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Arachir_The_Ancient_One_with_highlight():
    expectedCreatureName = 'Arachir The Ancient One'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Arachnophobica():
    expectedCreatureName = 'Arachnophobica'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Arachnophobica_with_highlight():
    expectedCreatureName = 'Arachnophobica'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Arctic_Faun():
    expectedCreatureName = 'Arctic Faun'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Arctic_Faun_with_highlight():
    expectedCreatureName = 'Arctic Faun'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Armadile():
    expectedCreatureName = 'Armadile'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Armadile_with_highlight():
    expectedCreatureName = 'Armadile'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Armenius():
    expectedCreatureName = 'Armenius'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Armenius_with_highlight():
    expectedCreatureName = 'Armenius'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ascending_Ferumbras():
    expectedCreatureName = 'Ascending Ferumbras'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ascending_Ferumbras_with_highlight():
    expectedCreatureName = 'Ascending Ferumbras'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Ashmunrah():
    expectedCreatureName = 'Ashmunrah'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Ashmunrah_with_highlight():
    expectedCreatureName = 'Ashmunrah'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Demon():
    expectedCreatureName = 'Askarak Demon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Demon_with_highlight():
    expectedCreatureName = 'Askarak Demon'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Lord():
    expectedCreatureName = 'Askarak Lord'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Lord_with_highlight():
    expectedCreatureName = 'Askarak Lord'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Prince():
    expectedCreatureName = 'Askarak Prince'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Askarak_Prince_with_highlight():
    expectedCreatureName = 'Askarak Prince'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Assassin():
    expectedCreatureName = 'Assassin'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Assassin_with_highlight():
    expectedCreatureName = 'Assassin'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Avalanche():
    expectedCreatureName = 'Avalanche'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Avalanche_with_highlight():
    expectedCreatureName = 'Avalanche'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Axeitus_Headbanger():
    expectedCreatureName = 'Axeitus Headbanger'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Axeitus_Headbanger_with_highlight():
    expectedCreatureName = 'Axeitus Headbanger'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Azure_Frog():
    expectedCreatureName = 'Azure Frog'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Azure_Frog_with_highlight():
    expectedCreatureName = 'Azure Frog'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Xenia():
    expectedCreatureName = 'Xenia'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Xenia_with_highlight():
    expectedCreatureName = 'Xenia'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Xogixath():
    expectedCreatureName = 'Xogixath'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Xogixath_with_highlight():
    expectedCreatureName = 'Xogixath'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yaga_The_Crone():
    expectedCreatureName = 'Yaga The Crone'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yaga_The_Crone_with_highlight():
    expectedCreatureName = 'Yaga The Crone'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yakchal():
    expectedCreatureName = 'Yakchal'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yakchal_with_highlight():
    expectedCreatureName = 'Yakchal'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yalahari():
    expectedCreatureName = 'Yalahari'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yalahari_with_highlight():
    expectedCreatureName = 'Yalahari'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yalahari_Despoiler():
    expectedCreatureName = 'Yalahari Despoiler'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yalahari_Despoiler_with_highlight():
    expectedCreatureName = 'Yalahari Despoiler'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yeti():
    expectedCreatureName = 'Yeti'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yeti_with_highlight():
    expectedCreatureName = 'Yeti'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Yielothax():
    expectedCreatureName = 'Yielothax'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Yielothax_with_highlight():
    expectedCreatureName = 'Yielothax'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Goanna():
    expectedCreatureName = 'Young Goanna'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Goanna_with_highlight():
    expectedCreatureName = 'Young Goanna'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Sea_Serpent():
    expectedCreatureName = 'Young Sea Serpent'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Sea_Serpent_with_highlight():
    expectedCreatureName = 'Young Sea Serpent'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Troll():
    expectedCreatureName = 'Young Troll'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Young_Troll_with_highlight():
    expectedCreatureName = 'Young Troll'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zamulosh():
    expectedCreatureName = 'Zamulosh'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zamulosh_with_highlight():
    expectedCreatureName = 'Zamulosh'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zanakeph():
    expectedCreatureName = 'Zanakeph'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zanakeph_with_highlight():
    expectedCreatureName = 'Zanakeph'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zarabustor():
    expectedCreatureName = 'Zarabustor'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zarabustor_with_highlight():
    expectedCreatureName = 'Zarabustor'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zarcorix_Of_Yalahar():
    expectedCreatureName = 'Zarcorix Of Yalahar'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zarcorix_Of_Yalahar_with_highlight():
    expectedCreatureName = 'Zarcorix Of Yalahar'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zavarash():
    expectedCreatureName = 'Zavarash'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zavarash_with_highlight():
    expectedCreatureName = 'Zavarash'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zevelon_Duskbringer():
    expectedCreatureName = 'Zevelon Duskbringer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zevelon_Duskbringer_with_highlight():
    expectedCreatureName = 'Zevelon Duskbringer'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zomba():
    expectedCreatureName = 'Zomba'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zomba_with_highlight():
    expectedCreatureName = 'Zomba'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zombie():
    expectedCreatureName = 'Zombie'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zombie_with_highlight():
    expectedCreatureName = 'Zombie'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zorvorax():
    expectedCreatureName = 'Zorvorax'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zorvorax_with_highlight():
    expectedCreatureName = 'Zorvorax'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zugurosh():
    expectedCreatureName = 'Zugurosh'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zugurosh_with_highlight():
    expectedCreatureName = 'Zugurosh'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zulazza_The_Corruptor():
    expectedCreatureName = 'Zulazza The Corruptor'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zulazza_The_Corruptor_with_highlight():
    expectedCreatureName = 'Zulazza The Corruptor'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName


def test_should_assert_Zushuka():
    expectedCreatureName = 'Zushuka'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName)
    assert creatureName == expectedCreatureName


def test_should_assert_Zushuka_with_highlight():
    expectedCreatureName = 'Zushuka'
    creatureName = getCreatureNameFromCreatureNameImage(expectedCreatureName, highlight=True)
    assert creatureName == expectedCreatureName