import manaPotionImg from '../../assets/potions/mana/manaPotion.gif';
import strongManaPotionImg from '../../assets/potions/mana/strongManaPotion.gif';
import greatManaPotionImg from '../../assets/potions/mana/greatManaPotion.gif';
import ultimateManaPotion from '../../assets/potions/mana/ultimateManaPotion.gif';
import { ManaPotions } from '../../types/mana.types';

export const MANA_POTIONS_OPTIONS = [
  {
    label: <img src={manaPotionImg} alt='Mana potion' />,
    value: ManaPotions.ManaPotion,
  },
  {
    label: <img src={strongManaPotionImg} alt='Strong mana potion' />,
    value: ManaPotions.StrongManaPotion,
  },
  {
    label: <img src={greatManaPotionImg} alt='Great mana potion' />,
    value: ManaPotions.GreatManaPotion,
  },
  {
    label: <img src={ultimateManaPotion} alt='Ultimate mana Potion' />,
    value: ManaPotions.UltimateManaPotion,
  },
];
