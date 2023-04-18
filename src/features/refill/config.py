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
    'great health potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatHealthPotion.png'),
    'great mana potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatManaPotion.png'),
    'great spirit potion': loadFromRGBToGray(f'{currentPath}/images/potions/greatSpiritPotion.png'),
    'health potion': loadFromRGBToGray(f'{currentPath}/images/potions/healthPotion.png'),
    'mana potion': loadFromRGBToGray(f'{currentPath}/images/potions/manaPotion.png'),
    'strong health potion': loadFromRGBToGray(f'{currentPath}/images/potions/strongHealthPotion.png'),
    'strong mana potion': loadFromRGBToGray(f'{currentPath}/images/potions/strongManaPotion.png'),
    'supreme health potion': loadFromRGBToGray(f'{currentPath}/images/potions/supremeHealthPotion.png'),
    'ultimate health potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateHealthPotion.png'),
    'ultimate mana potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateManaPotion.png'),
    'ultimate spirit potion': loadFromRGBToGray(f'{currentPath}/images/potions/ultimateSpiritPotion.png'),
}
