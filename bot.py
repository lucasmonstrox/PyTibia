import os
from core import player

os.chdir('images')

while True:
    print('health', player.getHealthPercent())
    print('mana', player.getManaPercent())
    print('full attack', player.hasFullAttack())
    print('balanced attack', player.hasBalancedAttack())
    print('defensive attack', player.hasDefensiveAttack())
    print('is holding attack', player.isHoldingAttack())
    print('is following attack', player.isFollowingAttack())
    print('is in pz zone', player.isInPz())
    print('is burning', player.isBurning())
    print('is drunk', player.isDrunk())
    print('is poisoned', player.isPoisoned())
    print('is slowed', player.isSlowed())