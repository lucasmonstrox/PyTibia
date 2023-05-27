from src.gameplay.core.tasks.useHotkey import UseHotkeyVectorTask
from src.repositories.actionBar.core import slotIsAvailable
from ...typings import Context
from ..utils.potions import matchHpHealing, matchManaHealing


currentPotionHealingTask = None


# TODO: add unit tests
def healingByPotionsObserver(context: Context):
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
                currentPotionHealingTask = UseHotkeyVectorTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1)
                return
    for potionType in ['firstManaPotion', 'secondManaPotion', 'thirdManaPotion']:
        if context['healing']['potions'][potionType]['enabled']:
            if matchManaHealing(context['healing']['potions'][potionType], context['statusBar']) and slotIsAvailable(context['screenshot'], 1):
                currentPotionHealingTask = UseHotkeyVectorTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1)
                return
