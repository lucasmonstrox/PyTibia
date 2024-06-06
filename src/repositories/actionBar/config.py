import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
arrowsImagesPath = f'{imagesPath}/arrows'
cooldownsImagesPath = f'{imagesPath}/cooldowns'
digitsImagesPath = f'{imagesPath}/digits'
hashes = {
    'cooldowns': {
        hashit(loadFromRGBToGray(f'{cooldownsImagesPath}/attack.png')): 'attack',
        hashit(loadFromRGBToGray(f'{cooldownsImagesPath}/healing.png')): 'healing',
        hashit(loadFromRGBToGray(f'{cooldownsImagesPath}/support.png')): 'support'
    }
}
images = {
    'arrows': {
        'left': loadFromRGBToGray(f'{arrowsImagesPath}/left.png'),
        'right': loadFromRGBToGray(f'{arrowsImagesPath}/right.png'),
    },
    # TODO: add exiva
    # TODO: add utito mas sio
    'cooldowns': {
        'attack': loadFromRGBToGray(f'{cooldownsImagesPath}/attack.png'),
        'exana kor': loadFromRGBToGray(f'{cooldownsImagesPath}/exanaKor.png'),
        'exana pox': loadFromRGBToGray(f'{cooldownsImagesPath}/exanaPox.png'),
        'exani hur down': loadFromRGBToGray(f'{cooldownsImagesPath}/exaniHur.png'),
        'exani hur up': loadFromRGBToGray(f'{cooldownsImagesPath}/exaniHur.png'),
        'exani tera': loadFromRGBToGray(f'{cooldownsImagesPath}/exaniTera.png'),
        'exeta amp res': loadFromRGBToGray(f'{cooldownsImagesPath}/exetaAmpRes.png'),
        'exeta res': loadFromRGBToGray(f'{cooldownsImagesPath}/exetaRes.png'),
        'exiva moe res': loadFromRGBToGray(f'{cooldownsImagesPath}/exivaMoeRes.png'),
        'exori': loadFromRGBToGray(f'{cooldownsImagesPath}/exori.png'),
        'exori gran': loadFromRGBToGray(f'{cooldownsImagesPath}/exoriGran.png'),
        'exori gran ico': loadFromRGBToGray(f'{cooldownsImagesPath}/exoriGranIco.png'),
        'exori mas': loadFromRGBToGray(f'{cooldownsImagesPath}/exoriMas.png'),
        'exori min': loadFromRGBToGray(f'{cooldownsImagesPath}/exoriMin.png'),
        'exura gran ico': loadFromRGBToGray(f'{cooldownsImagesPath}/exuraGranIco.png'),
        'exura ico': loadFromRGBToGray(f'{cooldownsImagesPath}/exuraIco.png'),
        'exura infir ico': loadFromRGBToGray(f'{cooldownsImagesPath}/healing.png'),
        'exura med ico': loadFromRGBToGray(f'{cooldownsImagesPath}/exuraMedIco.png'),
        'healing': loadFromRGBToGray(f'{cooldownsImagesPath}/healing.png'),
        'support': loadFromRGBToGray(f'{cooldownsImagesPath}/support.png'),
        'utamo tempo': loadFromRGBToGray(f'{cooldownsImagesPath}/utamoTempo.png'),
        'utani hur': loadFromRGBToGray(f'{cooldownsImagesPath}/utaniHur.png'),
        'utani tempo hur': loadFromRGBToGray(f'{cooldownsImagesPath}/utaniTempoHur.png'),
        'utevo gran lux': loadFromRGBToGray(f'{cooldownsImagesPath}/utevoGranLux.png'),
        'utevo gran res eq': loadFromRGBToGray(f'{cooldownsImagesPath}/utevoGranResEq.png'),
        'utevo lux': loadFromRGBToGray(f'{cooldownsImagesPath}/utevoLux.png'),
        'utito tempo': loadFromRGBToGray(f'{cooldownsImagesPath}/utitoTempo.png'),
        'utori kor': loadFromRGBToGray(f'{cooldownsImagesPath}/utoriKor.png'),
        'utura': loadFromRGBToGray(f'{cooldownsImagesPath}/utura.png'),
        'utura gran': loadFromRGBToGray(f'{cooldownsImagesPath}/uturaGran.png'),
    },
    'digits': {
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/0.png')): 0,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/1.png')): 1,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/2.png')): 2,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/3.png')): 3,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/4.png')): 4,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/5.png')): 5,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/6.png')): 6,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/7.png')): 7,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/8.png')): 8,
        hashit(loadFromRGBToGray(f'{digitsImagesPath}/9.png')): 9,
    },
}
