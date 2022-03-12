from time import sleep
from player import player
from utils import utils


def healingThread():
    percentageToHealWithManaPotion = 65
    percentageToHealWithPotion = 50
    percentageToHealWithSpell = 75
    spellHotkey = 'f1'
    manaPotionHotkey = 'f2'
    healthPotionHotkey = 'f3'
    while True:
        screenshot = utils.getScreenshot()
        healthPercentage = player.getHealthPercentage(screenshot)
        shouldHealWithHealthPotion = healthPercentage < percentageToHealWithPotion
        if shouldHealWithHealthPotion:
            print('healing with health potion...')
            utils.press(healthPotionHotkey)
            sleep(0.25)
            continue
        manaPercentage = player.getManaPercentage(screenshot)
        shouldHealWithMana = manaPercentage < percentageToHealWithManaPotion
        if shouldHealWithMana:
            print('healing with mana potion...')
            utils.press(manaPotionHotkey)
            sleep(0.25)
            continue
        shouldHealWithSpell = healthPercentage < percentageToHealWithSpell or manaPercentage > 90
        if shouldHealWithSpell:
            print('healing with spell...')
            utils.press(spellHotkey)
            sleep(0.25)
            continue
