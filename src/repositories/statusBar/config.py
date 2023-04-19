import numpy as np
import pathlib
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
iconsPath = f'{currentPath}/images/icons'
images = {
    'icons': {
        'hp': loadFromRGBToGray(f'{iconsPath}/heart.png'),
        'mana': loadFromRGBToGray(f'{iconsPath}/mana.png')
    }
}
hpBarAllowedPixelsColors = np.array([79, 118, 121, 110, 62])
barSize = 94
manaBarAllowedPixelsColors = np.array([68, 95, 97, 89, 52])
