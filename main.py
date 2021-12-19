from player import player
from utils import utils


def main():
    screenshot = utils.getScreenshot()
    print('hp', player.getHp(screenshot))


if __name__ == '__main__':
    main()
