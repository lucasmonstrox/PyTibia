import { Stack } from '@mui/material';
import { useState } from 'react';
import { useAlert } from 'react-alert';
import { HealthPotions } from '../../../../types/health.types';
import { ManaPotions } from '../../../../types/mana.types';
import { HealingPotionForm } from '../../components/HealingPotionForm';
import { HealingPotionFormInput } from '../../components/HealingPotionForm/types';
import { HEALTH_POTIONS_OPTIONS } from '../../../../components/HealthPotionsSelect/HealthPotionsOptions';
import { setHealingHealthOptions } from './services/setHealingHealthOptions';
import { setHealingManaOptions } from './services/setHealingManaOptions';
import { MANA_POTIONS_OPTIONS } from '../../../../components/ManaPotionsSelect/ManaPotionsOptions';

export const Healing = () => {
  const alert = useAlert();
  const [healthOptions, setHealthOptions] = useState<HealingPotionFormInput>({
    potion: HealthPotions.HealthPotion,
    enabled: true,
    percentage: 70,
    hotkey: null,
  });
  const [manaOptions, setManaOptions] = useState<HealingPotionFormInput>({
    potion: ManaPotions.ManaPotion,
    enabled: true,
    percentage: 70,
    hotkey: null,
  });
  const onChangeHealthOptions = async (
    healthOptions: HealingPotionFormInput
  ) => {
    // @ts-ignore
    const res = await window.api.getHealthOptions();
    console.log('res', res);
    const isHotkeyAlreadyUsedByManaOptions =
      healthOptions.hotkey && healthOptions.hotkey === manaOptions.hotkey;
    if (isHotkeyAlreadyUsedByManaOptions) {
      alert.error('Hotkey already used by Mana options');
      return;
    }
    setHealingHealthOptions(healthOptions);
    setHealthOptions(healthOptions);
  };
  const onChangeManaOptions = (manaOptions: HealingPotionFormInput) => {
    const isHotkeyAlreadyUsedByHealthOptions =
      manaOptions.hotkey && manaOptions.hotkey === healthOptions.hotkey;
    if (isHotkeyAlreadyUsedByHealthOptions) {
      alert.error('Hotkey already used by Health options');
      return;
    }
    setHealingManaOptions(manaOptions);
    setManaOptions(manaOptions);
  };
  return (
    <Stack direction='column' spacing={3}>
      <HealingPotionForm
        title='Health'
        potions={HEALTH_POTIONS_OPTIONS}
        options={healthOptions}
        onChange={onChangeHealthOptions}
      />
      <HealingPotionForm
        title='Mana'
        potions={MANA_POTIONS_OPTIONS}
        options={manaOptions}
        onChange={onChangeManaOptions}
      />
    </Stack>
  );
};
