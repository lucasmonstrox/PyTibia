import { Edit as EditIcon } from '@mui/icons-material';
import {
  Box,
  Button,
  IconButton,
  Grid,
  Modal,
  Paper,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from '@mui/material';
import { useState } from 'react';

export const Cavebot = () => {
  const [waypoints, setWaypoints] = useState<
    {
      action: string;
      coordinate: number[];
      options: any;
    }[]
  >([]);
  const editWaypointCoordinate = (index: number) => {
    handleOpen();
  };
  const makeSetActionWaypoint = (action: string) => () => {
    // TODO: obter a coordenada atual do game
    const coordinate = [1, 2, 3];
    const newWaypoints = [...waypoints];
    const walkWaypoint = {
      action,
      coordinate,
      options: {},
    };
    newWaypoints.push(walkWaypoint);
    setWaypoints(newWaypoints);
  };
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  return (
    <Stack direction='column'>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby='modal-modal-title'
        aria-describedby='modal-modal-description'
      >
        <Box>
          <Typography id='modal-modal-title' variant='h6' component='h2'>
            Text in a modal
          </Typography>
          <Typography id='modal-modal-description' sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
        </Box>
      </Modal>
      <Grid container>
        <Grid item xs={8}>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label='simple table'>
              <TableHead>
                <TableRow>
                  <TableCell></TableCell>
                  <TableCell align='right'>Action</TableCell>
                  <TableCell align='right'>Coordinate</TableCell>
                  <TableCell align='right'>Options</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {waypoints.map((waypoint, index) => (
                  <TableRow
                    key={index}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component='th' scope='row'>
                      {index}
                    </TableCell>
                    <TableCell component='th' scope='row'>
                      {waypoint.action}
                    </TableCell>
                    <TableCell align='right'>
                      {waypoint.coordinate[0]}, {waypoint.coordinate[1]},{' '}
                      {waypoint.coordinate[2]}
                      <IconButton
                        color='primary'
                        component='label'
                        onClick={() => editWaypointCoordinate(index)}
                      >
                        <EditIcon />
                      </IconButton>
                    </TableCell>
                    <TableCell align='right'>
                      {JSON.stringify(waypoint.options)}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>
        <Grid item xs={4}>
          <Stack>
            <Button>Deposit gold</Button>
            <Button>Deposit items</Button>
            <Button onClick={makeSetActionWaypoint('moveDownEast')}>
              Move down east
            </Button>
            <Button onClick={makeSetActionWaypoint('moveDownNorth')}>
              Move down north
            </Button>
            <Button onClick={makeSetActionWaypoint('moveDownSouth')}>
              Move down south
            </Button>
            <Button onClick={makeSetActionWaypoint('moveDownWest')}>
              Move down west
            </Button>
            <Button onClick={makeSetActionWaypoint('moveUpEast')}>
              Move up east
            </Button>
            <Button onClick={makeSetActionWaypoint('moveUpNorth')}>
              Move up north
            </Button>
            <Button onClick={makeSetActionWaypoint('moveUpSouth')}>
              Move up south
            </Button>
            <Button onClick={makeSetActionWaypoint('moveUpWest')}>
              Move up west
            </Button>
            <Button>Refill</Button>
            <Button>Refill checker</Button>
            <Button onClick={makeSetActionWaypoint('use')}>Use</Button>
            <Button>Use shovel</Button>
            <Button onClick={makeSetActionWaypoint('useRope')}>Use rope</Button>
            <Button onClick={makeSetActionWaypoint('walk')}>Walk</Button>
          </Stack>
        </Grid>
      </Grid>
    </Stack>
  );
};
