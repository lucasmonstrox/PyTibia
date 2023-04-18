from src.features.actionBar.core import hasCooldownByName, slotIsAvailable
from src.gameplay.core.tasks.usePotionTask import UsePotionGroupTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def didMatchHealthAndMana(statusBar, metadata):
    didMatchHitPoints = statusBar['hpPercentage'] <= metadata['hp']['percentage'] if metadata['hp']['comparator'] == 'lessThanOrEqual' else statusBar['hpPercentage'] >= metadata['hp']['percentage']
    didMatchMana = statusBar['manaPercentage'] <= metadata['mana']['percentage'] if metadata['mana']['comparator'] == 'lessThanOrEqual' else statusBar['manaPercentage'] >= metadata['mana']['percentage']
    didMatch = didMatchHitPoints and didMatchMana
    return didMatch


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def healingBySpellsObservable(context):
    if context['currentSpellHealing'] is not None:
        if context['currentSpellHealing'].status == 'completed':
            context['currentSpellHealing'] = None
        else:
            context = context['currentSpellHealing'].do(context)
            return
    if context['healing']['spells']['utura']['enabled']:
        if didMatchHealthAndMana(context['statusBar'], context['healing']['spells']['utura']):
            if slotIsAvailable(context['screenshot'], 13) and not hasCooldownByName(context['screenshot'], 'utura'):
                context['currentSpellHealing'] = UsePotionGroupTask(context['healing']['spells']['utura']['hotkey'])
                return
    # TODO: introduzir healing cooldown
    for spellHealing in ['criticalHealing', 'lightHealing']:
        if context['healing']['spells'][spellHealing]['enabled']:
            if context['statusBar']['mana'] > context['healing']['spells'][spellHealing]['metadata']['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells'][spellHealing]['metadata']['spellName']):
                context['currentSpellHealing'] = UsePotionGroupTask(context['healing']['spells'][spellHealing]['hotkey'])
                return
    # hasHealingCooldown = src.features.actionBar.core.hasHealingCooldown(context['screenshot'])
    # keysToPress = []
    # for healingItem in context['healing']['items']:
    #     if healingItem['enabled'] == False:
    #         continue
    #     if hasHealingCooldown and isHealingSpell(context['hotkeysV2'][healingItem['hotkey']]):
    #         continue
    #     category = healingItem['metadata']['category']
    #     isAmulet = category == 'amulet'
    #     if isAmulet and src.features.actionBar.core.slotIsEquipped(context['screenshot'], healingItem['metadata']['slot']):
    #         continue
    #     healingMatch = healingDidMatch(healingItem, hp, mana)
    #     slotIsAvailable = src.features.actionBar.core.slotIsAvailable(context['screenshot'], 2)
    #     if healingMatch and slotIsAvailable:
    #         keysToPress.append(healingItem['hotkey'])
    # if len(keysToPress) > 0:
    #     pyautogui.press(keysToPress)
    #     time.sleep(0.2)
