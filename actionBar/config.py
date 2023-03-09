from pathlib import Path
from utils.image import loadFromRGBToGray


currentPath = Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
images = {
    'attackCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/attack.png'),
    'exoriCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/exori.png'),
    'exoriGranCooldown': loadFromRGBToGray(
        f'{imagesPath}/cooldowns/exoriGran.png'),
    'exoriMasCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/exoriMas.png'),
    'exoriMinCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/exoriMin.png'),
    'hasteCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/haste.png'),
    'healingCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/healing.png'),
    'supportCooldown': loadFromRGBToGray(f'{imagesPath}/cooldowns/support.png'),
  
}
