import {
  Grid,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography,
} from '@mui/material';
import { set } from 'lodash';
import { ReactNode, useContext } from 'react';
import { Context } from '../../../../components/Context';
import { HealthPotionsSelect } from '../../../../components/HealthPotionsSelect';
import { ManaPotionsSelect } from '../../../../components/ManaPotionsSelect';
import { HealthPotions } from '../../../../types/health.types';

export const Refill = () => {
  const { context, setContext } = useContext(Context);
  const handleHealthPotionChange = async (
    event: SelectChangeEvent<unknown>,
    _: ReactNode
  ) => {
    try {
      const newContext = set(context, 'refill.health.item', event.target.value);
      console.log(`🚀 ~ event.target.value`, event.target.value);
      // @ts-ignore
      const res = await window.api.setContext(newContext);
      console.log(`🚀 ~ res`, res);
      setContext(res);
    } catch (err) {
      console.log(`🚀 ~ err`, err);
    }
  };
  const handleManaPotionChange = (
    event: SelectChangeEvent<unknown>,
    _: ReactNode
  ) => {
    // setManaPotion(event.target.value as ManaPotions);
  };
  return (
    <Stack direction='column'>
      <Typography>Desired health potions quantity to refill</Typography>
      <Grid container spacing={2}>
        <Grid item xs={4}>
          <HealthPotionsSelect
            selectProps={{
              value: context.refill.health.item,
              onChange: handleHealthPotionChange,
            }}
          />
        </Grid>
        <Grid item xs={2}>
          <TextField
            label='Quantity'
            inputProps={{ type: 'number' }}
            value={context.refill.health.quantity}
            // onChange={(evt) =>
            //   setQuantityOfHealthPotionsToRefill(+evt.target.value)
            // }
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
              value: context.refill.mana.item,
              onChange: handleManaPotionChange,
            }}
          />
        </Grid>
        <Grid item xs={2}>
          <TextField
            label='Quantity'
            inputProps={{ type: 'number' }}
            value={context.refill.mana.quantity}
            // onChange={(evt) =>
            //   setQuantityOfManaPotionsToRefill(+evt.target.value)
            // }
          />
        </Grid>
      </Grid>
    </Stack>
  );
};
