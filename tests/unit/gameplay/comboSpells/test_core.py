from src.gameplay.comboSpells.core import comboSpellDidMatch


context = {}

def test_should_return_True_using_lessThan_comparator_when_nearestCreaturesCount_is_less_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'lessThan',
            'value': 2
        }
    }
    nearestCreaturesCount = 1
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_False_using_lessThan_comparator_when_nearestCreaturesCount_is_not_less_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'lessThan',
            'value': 2
        }
    }
    nearestCreaturesCount = 3
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == False

def test_should_return_True_using_lessThanOrEqual_comparator_when_nearestCreaturesCount_is_less_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'lessThanOrEqual',
            'value': 2
        }
    }
    nearestCreaturesCount = 1
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_True_using_lessThanOrEqual_comparator_when_nearestCreaturesCount_is_less_than_or_equal_value():
    comboSpell = {
        'creatures': {
            'compare': 'lessThanOrEqual',
            'value': 2
        }
    }
    nearestCreaturesCount = 2
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_False_using_lessThanOrEqual_comparator_when_nearestCreaturesCount_is_not_less_than_or_equal_value():
    comboSpell = {
        'creatures': {
            'compare': 'lessThanOrEqual',
            'value': 2
        }
    }
    nearestCreaturesCount = 3
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == False

def test_should_return_True_using_greaterThan_comparator_when_nearestCreaturesCount_is_greater_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'greaterThan',
            'value': 2
        }
    }
    nearestCreaturesCount = 3
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_False_using_greaterThan_comparator_when_nearestCreaturesCount_is_not_greater_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'greaterThan',
            'value': 3
        }
    }
    nearestCreaturesCount = 2
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == False

def test_should_return_True_using_greaterThanOrEqual_comparator_when_nearestCreaturesCount_is_greater_than_value():
    comboSpell = {
        'creatures': {
            'compare': 'greaterThanOrEqual',
            'value': 3
        }
    }
    nearestCreaturesCount = 4
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_True_using_greaterThanOrEqual_comparator_when_nearestCreaturesCount_is_greater_than_or_equal_value():
    comboSpell = {
        'creatures': {
            'compare': 'greaterThanOrEqual',
            'value': 3
        }
    }
    nearestCreaturesCount = 3
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == True

def test_should_return_False_using_greaterThanOrEqual_comparator_when_nearestCreaturesCount_is_not_greater_than_or_equal_value():
    comboSpell = {
        'creatures': {
            'compare': 'greaterThanOrEqual',
            'value': 3
        }
    }
    nearestCreaturesCount = 2
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == False

def test_should_return_False_when_compare_does_not_exists():
    comboSpell = {
        'creatures': {
            'compare': 'invalidCompare',
            'value': 3
        }
    }
    nearestCreaturesCount = 2
    assert comboSpellDidMatch(comboSpell, nearestCreaturesCount) == False
