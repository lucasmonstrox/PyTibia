from src.features.actionBar.core import slotIsAvailable
from src.gameplay.core.tasks.useHotkey import UseHotkeyGroupTask
from ...typings import Context


currentPotionHealingTask = None


# TODO: add unit tests
def healingByPotionsObservable(context: Context):
    global currentPotionHealingTask
    if currentPotionHealingTask is not None:
        if currentPotionHealingTask.status == 'completed':
            currentPotionHealingTask = None
        else:
            currentPotionHealingTask.do(context)
            return
    for potionType in ['firstHealthPotion', 'secondHealthPotion', 'thirdHealthPotion']:
        if context['healing']['potions'][potionType]['enabled']:
            if matchHpHealing(context['healing']['potions'][potionType], context['statusBar']) and slotIsAvailable(context['screenshot'], 1):
                currentPotionHealingTask = UseHotkeyGroupTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1)
                return
    for potionType in ['firstManaPotion', 'secondManaPotion', 'thirdManaPotion']:
        if context['healing']['potions'][potionType]['enabled']:
            if matchManaHealing(context['healing']['potions'][potionType], context['statusBar']) and slotIsAvailable(context['screenshot'], 1):
                currentPotionHealingTask = UseHotkeyGroupTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1)
                return


# TODO: add typings
# TODO: add unit tests
def matchHpHealing(healing, statusBar):
    if healing['hpPercentageLessThanOrEqual'] is not None:
        if statusBar['hpPercentage'] > healing['hpPercentageLessThanOrEqual']:
            return False
    if healing['manaPercentageGreaterThanOrEqual'] is not None:
        if statusBar['hpPercentage'] < healing['manaPercentageGreaterThanOrEqual']:
            return False
    return True


# TODO: add typings
# TODO: add unit tests
def matchManaHealing(healing, statusBar):
    if healing['manaPercentageLessThanOrEqual'] is None:
        return False
    if statusBar['manaPercentage'] > healing['manaPercentageLessThanOrEqual']:
        return False
    return True
