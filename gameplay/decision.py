import hud.creatures


# TODO: add unit tests
def getWay(hudCreatures, radarCoordinate):
    targetCreature = hud.creatures.getClosestCreature(
        hudCreatures, radarCoordinate)
    print('targetCreature', targetCreature)
    hasTargetCreature = targetCreature != None
    way = 'cavebot' if hasTargetCreature else 'waypoint'
    return way
