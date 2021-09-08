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
    print('is in pz zone', player.isPz())