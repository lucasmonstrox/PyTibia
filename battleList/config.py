import utils.core
import utils.image
import utils.mouse
import wiki.creatures


container = {
    "topBarImg": utils.image.loadAsArray('battleList/images/containerTopBar.png'),
    "bottomBarImg": utils.image.loadAsArray('battleList/images/containerBottomBar.png'),
    "width": 156
}
creatures = {
    "namePixelColor": 192,
    "highlightedNamePixelColor": 247,
    "nameImgHashes": {}
}
slot = {
    "height": 20,
    "gap": 2
}


# TODO: should load through .npy
for creatureName in wiki.creatures.creatures:
    creatureNameImg = utils.image.loadAsArray(
        'battleList/images/monsters/{}.png'.format(creatureName))
    creatureNameImgHash = utils.core.hashit(creatureNameImg)
    creatures["nameImgHashes"][creatureNameImgHash] = creatureName
