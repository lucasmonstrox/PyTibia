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
    print('is bleeding', player.isBleeding())
    print('is burning', player.isBurning())
    print('is drunk', player.isDrunk())
    print('is haste', player.isHaste())
    print('is poisoned', player.isPoisoned())
    print('is slowed', player.isSlowed())
    print('has accessories equipped', player.hasAccessoriesEquiped())
    print('has armor equipped', player.hasArmorEquipped())
    print('has backpack equipped', player.hasBackpackEquipped())
    print('has boots equipped', player.hasBootsEquipped())
    print('has helmet equipped', player.hasHelmetEquipped())
    print('has legs equipped', player.hasLegsEquipped())
    print('has necklace equipped', player.hasNecklaceEquipped())
    print('has ring equipped', player.hasRingEquipped())
    print('has weapon equipped', player.hasWeaponEquipped())
    print('is inventory visible', player.isInventoryVisible())
    print('is ready for pvp', player.isReadyForPvp())
    