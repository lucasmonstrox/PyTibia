# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def healingDidMatch(healingItem, hp, mana):
    hpDidMatch = True
    manaDidMatch = True
    if healingItem['hp']['lessThan'] is not None:
        if hp > healingItem['hp']['lessThan']:
            hpDidMatch = False
    if healingItem['hp']['greaterThan'] is not None:
        if hp < healingItem['hp']['greaterThan']:
            hpDidMatch = False
    if healingItem['mana']['lessThan'] is not None:
        if mana > healingItem['mana']['lessThan']:
            manaDidMatch = False
    if healingItem['mana']['greaterThan'] is not None:
        if mana < healingItem['mana']['greaterThan']:
            manaDidMatch = False
    didMatch = hpDidMatch and manaDidMatch
    return didMatch
