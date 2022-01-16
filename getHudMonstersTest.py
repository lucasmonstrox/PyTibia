from time import time
from hud import hud
from battleList import battleList
from utils import utils


def main():
    loop_time = time()
    screenshot = utils.loadImgAsArray('screenshot.png')
    while True:
        screenshot = utils.getScreenshot()
        hudCoordinates = hud.getCoordinates(screenshot)
        hudImg = screenshot[hudCoordinates[1]:hudCoordinates[1] +
                            352, hudCoordinates[0]:hudCoordinates[0] + 480]
        battleListCreatures = battleList.getCreatures(screenshot)
        hasNoBattleListCreatures = len(battleListCreatures) == 0
        if hasNoBattleListCreatures:
            print('There is no battle list creatures')
            continue
        hudImgFlattened = hudImg.flatten()
        creaturesBars = hud.getCreaturesBars(hudImgFlattened)
        hasNoHudCreaturesBars = len(creaturesBars) == 0
        if hasNoHudCreaturesBars:
            print('There is no hud creatures bars')
            continue
        creatures = hud.getCreatures(
            hudImg, creaturesBars, battleListCreatures)
        print(creatures)
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
