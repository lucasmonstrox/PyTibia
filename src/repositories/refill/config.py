import pathlib
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
# TODO: improve this
npcTradeBarImage = loadFromRGBToGray(
    f'{currentPath}/images/npcTradeBar.png')
# TODO: improve this
npcTradeOkImage = loadFromRGBToGray(
    f'{currentPath}/images/npcTradeOk.png')
images = {
    'Great Health Potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatHealthPotion.png'),
    'Great Mana Potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatManaPotion.png'),
    'Great spirit Potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatSpiritPotion.png'),
    'Health Potion': loadFromRGBToGray(f'{currentPath}/images/potions/healthPotion.png'),
    'Mana Potion': loadFromRGBToGray(f'{currentPath}/images/potions/manaPotion.png'),
    'Strong Health Potion': loadFromRGBToGray(f'{currentPath}/images/potions/strongHealthPotion.png'),
    'Strong Mana Potion': loadFromRGBToGray(f'{currentPath}/images/potions/strongManaPotion.png'),
    'Supreme Health Potion': loadFromRGBToGray(f'{currentPath}/images/potions/supremeHealthPotion.png'),
    'Ultimate Health Potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateHealthPotion.png'),
    'Ultimate Mana Potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateManaPotion.png'),
    'Ultimate Spirit Potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateSpiritPotion.png'),
}
