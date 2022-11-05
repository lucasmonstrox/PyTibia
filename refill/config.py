import pathlib
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()
npcTradeBarImage = utils.image.loadFromRGBToGray(
    f'{currentPath}/images/npcTradeBar.png')
npcTradeOkImage = utils.image.loadFromRGBToGray(
    f'{currentPath}/images/npcTradeOk.png')
potionsImages = {
    'great health potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/greatHealthPotion.png'),
    'great mana potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/greatManaPotion.png'),
    'great spirit potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/greatSpiritPotion.png'),
    'health potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/healthPotion.png'),
    'mana potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/manaPotion.png'),
    'strong health potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/strongHealthPotion.png'),
    'strong mana potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/strongManaPotion.png'),
    'supreme health potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/supremeHealthPotion.png'),
    'ultimate health potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/ultimateHealthPotion.png'),
    'ultimate mana potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/ultimateManaPotion.png'),
    'ultimate spirit potion': utils.image.loadFromRGBToGray(f'{currentPath}/images/potions/ultimateSpiritPotion.png'),
}
