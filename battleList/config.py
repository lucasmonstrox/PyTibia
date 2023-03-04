import numpy as np
import pathlib
import utils.core
import utils.image
import wiki.creatures


parentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{parentPath}/images'
container = {
    "dimensions": {
        "width": 156
    },
    "images": {
        "topBar": utils.image.loadAsGrey(f'{imagesPath}/containerTopBar.png'),
        "bottomBar": utils.image.loadAsGrey(f'{imagesPath}/containerBottomBar.png'),
    },
}
creatures = {
    "namePixelColor": 192,
    "highlightedNamePixelColor": 247,
    "nameImgHashes": {}
}
slot = {
    "dimensions": {
        "height": 20,
        "width": 156
    },
    "grid": {
        "gap": 2
    }
}
skulls = {
    'images': {
        'black': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/black.png'),
        'green': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/green.png'),
        'orange': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/orange.png'),
        'red': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/red.png'),
        'white': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/white.png'),
        'yellow': utils.image.loadFromRGBToGray(f'{imagesPath}/skulls/yellow.png'),
    }
}

for creatureName in wiki.creatures.creatures:
    creatureNameImg = utils.image.loadAsGrey(
        f'{imagesPath}/monsters/{creatureName}.png')
    creatureNameImg = np.ravel(creatureNameImg[8:9, 0:115])
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatures["nameImgHashes"][creatureNameImgHash] = creatureName
