import hud.creatures


def getWay(corpsesToLoot, hudCreatures, coordinate):
    hasCorpsesToLoot = len(corpsesToLoot) > 0
    if hasCorpsesToLoot:
        return 'lootCorpses'
    targetCreature = hud.creatures.getClosestCreature(
        hudCreatures, coordinate)
    hasTargetCreature = targetCreature != None
    if hasTargetCreature:
        return 'cavebot'
    return 'waypoint'
