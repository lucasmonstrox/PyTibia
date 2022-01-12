from player import player
from utils import utils


def main():
    while True:
        screenshot = utils.getScreenshot()
        print('health %', player.getHealthPercentage(screenshot))
        print('mana %', player.getManaPercentage(screenshot))


if __name__ == '__main__':
    main()
