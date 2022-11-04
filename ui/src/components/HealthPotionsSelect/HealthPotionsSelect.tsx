import { Box, MenuItem, Select, SelectProps, Stack } from '@mui/material';
import { HEALTH_POTIONS_NAMES } from './consts';
import { HEALTH_POTIONS_OPTIONS } from './HealthPotionsOptions';

type Props = {
  selectProps?: SelectProps;
};

export const HealthPotionsSelect = ({ selectProps }: Props) => {
  return (
    <Select fullWidth label='Health potion' {...selectProps}>
      {HEALTH_POTIONS_OPTIONS.map((potion) => (
        <MenuItem key={potion.value} value={potion.value}>
          <Stack direction='row' alignItems='center' spacing={2}>
            <Box>{potion.label}</Box>
            <Box>{HEALTH_POTIONS_NAMES[potion.value]}</Box>
          </Stack>
        </MenuItem>
      ))}
    </Select>
  );
};
