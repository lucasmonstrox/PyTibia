import os
from core import player

os.chdir('images')

while True:
    print(player.getHealth())
    print(player.getMana())