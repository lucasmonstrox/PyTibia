import {
  MenuItem,
  Paper,
  Select,
  Slider,
  Switch,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  Toolbar,
  Typography,
} from '@mui/material';
import { HealingPotionFormProps } from './types';

export const HealingPotionForm = ({
  title,
  potions,
  options,
  onChange,
}: HealingPotionFormProps) => {
  const isFormDisabled = !options.enabled;
  return (
    <Paper>
      <Toolbar>
        <Typography variant='h6'>{title}</Typography>
      </Toolbar>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Enabled</TableCell>
              <TableCell>Potion</TableCell>
              <TableCell>Percentage %</TableCell>
              <TableCell>Hotkey</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>
                <Switch
                  checked={options.enabled}
                  onChange={(_, enabled) => onChange({ ...options, enabled })}
                />
              </TableCell>
              <TableCell>
                <Select
                  disabled={isFormDisabled}
                  value={options.potion}
                  onChange={(evt) =>
                    onChange({ ...options, potion: evt.target.value })
                  }
                >
                  {potions.map((potion) => (
                    <MenuItem value={potion.value}>{potion.label}</MenuItem>
                  ))}
                </Select>
              </TableCell>
              <TableCell>
                <Slider
                  defaultValue={options.percentage}
                  disabled={isFormDisabled}
                  valueLabelDisplay='auto'
                  step={10}
                  marks
                  min={10}
                  max={100}
                  onChangeCommitted={(_, percentage) =>
                    onChange({ ...options, percentage: percentage as number })
                  }
                />
              </TableCell>
              <TableCell>
                <TextField
                  value={options.hotkey}
                  disabled={isFormDisabled}
                  onKeyDown={(evt) => evt.preventDefault()}
                  onKeyUp={(evt) => onChange({ ...options, hotkey: evt.key })}
                />
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
};
