import { Box, MenuItem, Select, SelectProps, Stack } from '@mui/material';
import { MANA_POTIONS_NAMES } from './consts';
import { MANA_POTIONS_OPTIONS } from './ManaPotionsOptions';

type Props = {
  selectProps?: SelectProps;
};

export const ManaPotionsSelect = ({ selectProps }: Props) => {
  return (
    <Select fullWidth label='Mana potion' {...selectProps}>
      {MANA_POTIONS_OPTIONS.map((potion) => (
        <MenuItem key={potion.value} value={potion.value}>
          <Stack direction='row' alignItems='center' spacing={2}>
            <Box>{potion.label}</Box>
            <Box>{MANA_POTIONS_NAMES[potion.value]}</Box>
          </Stack>
        </MenuItem>
      ))}
    </Select>
  );
};
