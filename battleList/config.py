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
        "topBar": utils.image.loadAsArray(f'{imagesPath}/containerTopBar.png'),
        "bottomBar": utils.image.loadAsArray(f'{imagesPath}/containerBottomBar.png'),
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


for creatureName in wiki.creatures.creatures:
    creatureNameImg = utils.image.loadAsArray(
        f'{imagesPath}/monsters/{creatureName}.png')
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatures["nameImgHashes"][creatureNameImgHash] = creatureName
