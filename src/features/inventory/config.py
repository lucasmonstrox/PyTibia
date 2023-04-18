import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
containersBarsImagesPath = f'{imagesPath}/containersBars'
slotsImagesPath = f'{imagesPath}/slots'
images = {
    'containersBars': {
        'backpack bottom': loadFromRGBToGray(f'{containersBarsImagesPath}/backpack bottom.png'),
        'beach backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/beach backpack.png'),
        'brocade backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/brocade backpack.png'),
        'fur backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/fur backpack.png'),
        'locker': loadFromRGBToGray(f'{containersBarsImagesPath}/locker.png'),
    },
    'slots': {
        'beach backpack': loadFromRGBToGray(f'{slotsImagesPath}/beach backpack.png'),
        'big empty potion flask': loadFromRGBToGray(f'{slotsImagesPath}/big empty potion flask.png'),
        'brocade backpack': loadFromRGBToGray(f'{slotsImagesPath}/brocade backpack.png'),
        'depot': loadFromRGBToGray(f'{slotsImagesPath}/depot.png'),
        'depot chest 1': loadFromRGBToGray(f'{slotsImagesPath}/depot chest 1.png'),
        'depot chest 2': loadFromRGBToGray(f'{slotsImagesPath}/depot chest 2.png'),
        'depot chest 3': loadFromRGBToGray(f'{slotsImagesPath}/depot chest 3.png'),
        'depot chest 4': loadFromRGBToGray(f'{slotsImagesPath}/depot chest 4.png'),
        'empty': loadFromRGBToGray(f'{slotsImagesPath}/empty.png'),
        'fur backpack': loadFromRGBToGray(f'{slotsImagesPath}/fur backpack.png'),
        'medium empty potion flask': loadFromRGBToGray(f'{slotsImagesPath}/medium empty potion flask.png'),
        'small empty potion flask': loadFromRGBToGray(f'{slotsImagesPath}/small empty potion flask.png'),
        'stash': loadFromRGBToGray(f'{slotsImagesPath}/stash.png')
    }
}
slotsImagesHashes = {
    hashit(images['slots']['big empty potion flask']): 'empty potion flask',
    hashit(images['slots']['medium empty potion flask']): 'empty potion flask',
    hashit(images['slots']['small empty potion flask']): 'empty potion flask',
    hashit(images['slots']['empty']): 'empty slot',
}
