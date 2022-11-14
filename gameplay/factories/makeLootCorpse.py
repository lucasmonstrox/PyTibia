from gameplay.tasks.lootCorpse import LootCorpseTask


def makeLootCorpseTask(corpse):
    task = LootCorpseTask(corpse)
    return ('lootCorpse', task)
