import { HealthPotions } from '../../types/health.types';

export const HEALTH_POTIONS_NAMES: Record<HealthPotions, string> = {
  [HealthPotions.SmallHealthPotion]: 'Small health potion',
  [HealthPotions.HealthPotion]: 'Health potion',
  [HealthPotions.StrongHealthPotion]: 'Strong health potion',
  [HealthPotions.GreatHealthPotion]: 'Great health potion',
  [HealthPotions.UltimateHealthPotion]: 'Ultimate health potion',
  [HealthPotions.SupremeHealthPotion]: 'Supreme health potion',
};
