import os
from core import player

os.chdir('images')

while True:
    print('health', player.getHealthPercent())
    print('mana', player.getManaPercent())