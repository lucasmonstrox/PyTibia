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
        '25 Years Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/25 Years Backpack.png'),
        'Anniversary Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Anniversary Backpack.png'),
        'Beach Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Beach Backpack.png'),
        'Birthday Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Birthday Backpack.png'),
        'Brocade Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Brocade Backpack.png'),
        'Buggy Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Buggy Backpack.png'),
        'Cake Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Cake Backpack.png'),
        'Camouflage Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Camouflage Backpack.png'),
        'Crown Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Crown Backpack.png'),
        'Crystal Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Crystal Backpack.png'),
        'Deepling Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Deepling Backpack.png'),
        'Demon Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Demon Backpack.png'),
        'Dragon Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Dragon Backpack.png'),
        'Expedition Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Expedition Backpack.png'),
        'Fur Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Fur Backpack.png'),
        'Glooth Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Glooth Backpack.png'),
        'Heart Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Heart Backpack.png'),
        'locker': loadFromRGBToGray(f'{containersBarsImagesPath}/locker.png'),
        'Minotaur Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Minotaur Backpack.png'),
        'Moon Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Moon Backpack.png'),
        'Mushroom Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Mushroom Backpack.png'),
        'Pannier Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Pannier Backpack.png'),
        'Pirate Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Pirate Backpack.png'),
        'Raccoon Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Raccoon Backpack.png'),
        'Santa Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Santa Backpack.png'),
        'Wolf Backpack': loadFromRGBToGray(f'{containersBarsImagesPath}/Wolf Backpack.png'),
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
