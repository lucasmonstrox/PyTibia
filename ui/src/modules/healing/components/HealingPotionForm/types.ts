export interface PotionOption {
  label: JSX.Element;
  value: string;
}

export interface HealingPotionFormInput {
  potion: PotionOption['value'];
  enabled: boolean;
  percentage: number;
  hotkey: null | string; // TODO: add enum of allowed hotkeys instead of "string"
}

export interface HealingPotionFormProps {
  title: string;
  potions: PotionOption[];
  options: HealingPotionFormInput;
  onChange: (value: HealingPotionFormInput) => void;
}
