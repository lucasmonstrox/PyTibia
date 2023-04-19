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