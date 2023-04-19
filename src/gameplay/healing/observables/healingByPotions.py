from src.features.actionBar.core import slotIsAvailable
from src.gameplay.core.tasks.useHotkey import UseHotkeyGroupTask
from ...typings import Context


# TODO: add unit tests
def healingByPotionsObservable(context: Context):
    if context['currentPotionHealing'] is not None:
        if context['currentPotionHealing'].status == 'completed':
            context['currentPotionHealing'] = None
        else:
            context = context['currentPotionHealing'].do(context)
            return
    if context['healing']['potions']['firstPriority']['enabled']:
        if context['statusBar']['hpPercentage'] < context['healing']['potions']['firstPriority']['hpPercentage'] and slotIsAvailable(context['screenshot'], 1):
            context['currentPotionHealing'] = UseHotkeyGroupTask(context['healing']['potions']['firstPriority']['hotkey'], delayAfterComplete=1)
            return
