import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
arrowsImagesPath = f'{imagesPath}/arrows'
waypointsImagesPath = f'{imagesPath}/waypoints'
images = {
    'arrows': {
        'leftGameWindow00': loadFromRGBToGray(f'{arrowsImagesPath}/leftGameWindow00.png'),
        'leftGameWindow01': loadFromRGBToGray(f'{arrowsImagesPath}/leftGameWindow01.png'),
        'leftGameWindow10': loadFromRGBToGray(f'{arrowsImagesPath}/leftGameWindow10.png'),
        'leftGameWindow11': loadFromRGBToGray(f'{arrowsImagesPath}/leftGameWindow11.png'),
        'rightGameWindow00': loadFromRGBToGray(f'{arrowsImagesPath}/rightGameWindow00.png'),
        'rightGameWindow01': loadFromRGBToGray(f'{arrowsImagesPath}/rightGameWindow01.png'),
        'rightGameWindow10': loadFromRGBToGray(f'{arrowsImagesPath}/rightGameWindow10.png'),
        'rightGameWindow11': loadFromRGBToGray(f'{arrowsImagesPath}/rightGameWindow11.png'),
    },
    720: {
        'holeOpen': loadFromRGBToGray(f'{waypointsImagesPath}/holeOpen720.png')
    },
    1080: {
        'holeOpen': loadFromRGBToGray(f'{waypointsImagesPath}/holeOpen1080.png')
    }
}
arrowsImagesHashes = {
    hashit(images['arrows']['leftGameWindow01']): 'leftGameWindow01',
    hashit(images['arrows']['leftGameWindow10']): 'leftGameWindow10',
    hashit(images['arrows']['leftGameWindow11']): 'leftGameWindow11',
    hashit(images['arrows']['leftGameWindow00']): 'leftGameWindow00',
    hashit(images['arrows']['rightGameWindow01']): 'rightGameWindow01',
    hashit(images['arrows']['rightGameWindow10']): 'rightGameWindow10',
    hashit(images['arrows']['rightGameWindow11']): 'rightGameWindow11',
    hashit(images['arrows']['rightGameWindow00']): 'rightGameWindow00',
}
gameWindowSizes = {
    720: (480, 352),
    1080: (960, 704)
}
gameWindowCache = {
    'left': {'arrow': None, 'position': None},
    'right': {'arrow': None, 'position': None},
}
