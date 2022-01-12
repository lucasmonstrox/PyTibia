from player import player
from utils import utils


def main():
    while True:
        screenshot = utils.getScreenshot()
        print('hp', player.getHp(screenshot))


if __name__ == '__main__':
    main()
