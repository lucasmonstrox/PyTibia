spellsPath = {
    'exori': [[6, 4], [7, 4], [8, 4], [6, 5], [8, 5], [6, 6], [7, 6], [8, 6]],
    'exori gran': [[6, 4], [7, 4], [8, 4], [6, 5], [8, 5], [6, 6], [7, 6], [8, 6]],
    'exori mas': [
                    [6, 2], [7, 2], [8, 2],
            [5, 3], [6, 3], [7, 3], [8, 3], [9, 3],
    [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4],
    [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5],
    [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6], [10, 6],
            [5, 7], [6, 7], [7, 7], [8, 7], [9, 7],
                    [6, 8], [7, 8], [8, 8],
    ],
}


# TODO: add typings
def comboSpellDidMatch(comboSpell, nearestCreaturesCount: int) -> bool:
    if comboSpell['creatures']['compare'] == 'lessThan':
        return nearestCreaturesCount < comboSpell['creatures']['value']
    if comboSpell['creatures']['compare'] == 'lessThanOrEqual':
        return nearestCreaturesCount <= comboSpell['creatures']['value']
    if comboSpell['creatures']['compare'] == 'greaterThan':
        return nearestCreaturesCount > comboSpell['creatures']['value']
    if comboSpell['creatures']['compare'] == 'greaterThanOrEqual':
        return nearestCreaturesCount >= comboSpell['creatures']['value']
    return False
