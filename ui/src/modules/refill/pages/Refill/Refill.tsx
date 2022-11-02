import {
  Grid,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography,
} from '@mui/material';
import { ReactNode, useContext } from 'react';
import { Context } from '../../../../components/Context';
import { HealthPotionsSelect } from '../../../../components/HealthPotionsSelect';
import { ManaPotionsSelect } from '../../../../components/ManaPotionsSelect';
import { HealthPotions } from '../../../../types/health.types';
import { ManaPotions } from '../../../../types/mana.types';

export const Refill = () => {
  const {
    refill,
    setHealthPotion,
    setQuantityOfHealthPotionsToRefill,
    setManaPotion,
    setQuantityOfManaPotionsToRefill,
  } = useContext(Context);
  const handleHealthPotionChange = (
    event: SelectChangeEvent<unknown>,
    _: ReactNode
  ) => setHealthPotion(event.target.value as HealthPotions);
  const handleManaPotionChange = (
    event: SelectChangeEvent<unknown>,
    _: ReactNode
  ) => setManaPotion(event.target.value as ManaPotions);
  return (
    <Stack direction='column'>
      <Typography>Desired health potions quantity to refill</Typography>
      <Grid container spacing={2}>
        <Grid item xs={4}>
          <HealthPotionsSelect
            selectProps={{
              value: refill.health.item,
              onChange: handleHealthPotionChange,
            }}
          />
        </Grid>
        <Grid item xs={2}>
          <TextField
            label='Quantity'
            inputProps={{ type: 'number' }}
            value={refill.health.quantity}
            onChange={(evt) =>
              setQuantityOfHealthPotionsToRefill(+evt.target.value)
            }
          />
        </Grid>
      </Grid>
      <Typography sx={{ mt: 2 }}>
        Desired mana potions quantity to refill
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={4}>
          <ManaPotionsSelect
            selectProps={{
              value: refill.mana.item,
              onChange: handleManaPotionChange,
            }}
          />
        </Grid>
        <Grid item xs={2}>
          <TextField
            label='Quantity'
            inputProps={{ type: 'number' }}
            value={refill.mana.quantity}
            onChange={(evt) =>
              setQuantityOfManaPotionsToRefill(+evt.target.value)
            }
          />
        </Grid>
      </Grid>
    </Stack>
  );
};
