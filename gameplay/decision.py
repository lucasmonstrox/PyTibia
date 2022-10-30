import hud.creatures


# TODO: add unit tests
def getWay(corpsesToLoot, hudCreatures, radarCoordinate):
    hasCorpsesToLoot = len(corpsesToLoot) > 0
    if hasCorpsesToLoot:
        return 'lootCorpses'
    targetCreature = hud.creatures.getClosestCreature(
        hudCreatures, radarCoordinate)
    hasTargetCreature = targetCreature != None
    if hasTargetCreature:
        return 'cavebot'
    return 'waypoint'
