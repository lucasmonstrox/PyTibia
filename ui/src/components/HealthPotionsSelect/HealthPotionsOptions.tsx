import greatHealthPotionImg from '../../assets/potions/health/greatHealthPotion.gif';
import healthPotionImg from '../../assets/potions/health/healthPotion.gif';
import smallHealthPotionImg from '../../assets/potions/health/smallHealthPotion.gif';
import strongHealthPotionImg from '../../assets/potions/health/strongHealthPotion.gif';
import supremeHealthPotionImg from '../../assets/potions/health/supremeHealthPotion.gif';
import ultimateHealthPotion from '../../assets/potions/health/ultimateHealthPotion.gif';
import { HealthPotions } from '../../types/health.types';

export const HEALTH_POTIONS_OPTIONS = [
  {
    label: <img src={smallHealthPotionImg} alt='Small Health Potion' />,
    value: HealthPotions.SmallHealthPotion,
  },
  {
    label: <img src={healthPotionImg} alt='Health Potion' />,
    value: HealthPotions.HealthPotion,
  },
  {
    label: <img src={strongHealthPotionImg} alt='Strong Health Potion' />,
    value: HealthPotions.StrongHealthPotion,
  },
  {
    label: <img src={greatHealthPotionImg} alt='Great Health Potion' />,
    value: HealthPotions.GreatHealthPotion,
  },
  {
    label: <img src={ultimateHealthPotion} alt='Ultimate Health Potion' />,
    value: HealthPotions.UltimateHealthPotion,
  },
  {
    label: <img src={supremeHealthPotionImg} alt='Supreme Health Potion' />,
    value: HealthPotions.SupremeHealthPotion,
  },
];
