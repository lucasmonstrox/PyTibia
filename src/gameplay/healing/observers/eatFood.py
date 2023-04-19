from src.gameplay.core.tasks.useHotkey import UseHotkeyGroupTask
from src.repositories.actionBar.core import slotIsAvailable
from src.repositories.skills.core import getFood
from ...typings import Context


eatFoodTask = None


# TODO: add unit tests
def eatFoodObserver(context: Context):
    global eatFoodTask
    if eatFoodTask is not None:
        if eatFoodTask.status == 'completed':
            eatFoodTask = None
        else:
            eatFoodTask.do(context)
            return
    if not context['healing']['eatFood']['enabled']:
        return
    food = getFood(context['screenshot'])
    if food > context['healing']['eatFood']['eatWhenFoodIslessOrEqual']:
        return
    eatFoodTask = UseHotkeyGroupTask(context['healing']['eatFood']['hotkey'], delayAfterComplete=0.5)
