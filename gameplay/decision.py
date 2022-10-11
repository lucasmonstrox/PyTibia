import hud.creatures


# TODO: add unit tests
def getWay(corpsesToLoot, hudCreatures, radarCoordinate):
    if len(corpsesToLoot) > 0:
        return 'lootCorpses'
    targetCreature = hud.creatures.getClosestCreature(
        hudCreatures, radarCoordinate)
    print('targetCreature', targetCreature)
    hasTargetCreature = targetCreature != None
    way = 'cavebot' if hasTargetCreature else 'waypoint'
    return way
