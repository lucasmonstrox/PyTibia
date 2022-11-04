import { Box, Tab, Tabs } from '@mui/material';
import { positions, Provider as AlertProvider } from 'react-alert';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { AlertTemplate } from './components/AlertTemplate';
import { ContextProvider } from './components/Context';
import { Cavebot } from './modules/cavebot/pages/Cavebot';
import { Healing } from './modules/healing/pages/Healing';
import { Refill } from './modules/refill/pages/Refill';

export const App = () => (
  <ContextProvider>
    <AlertProvider
      template={AlertTemplate}
      position={positions.TOP_CENTER}
      timeout={2500}
    >
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={0} aria-label='basic tabs example'>
          <Tab label='Cavebot' />
          <Tab label='Refill' />
          <Tab label='Target' />
        </Tabs>
      </Box>
      <BrowserRouter>
        <Routes>
          <Route index element={<Cavebot />} />
          <Route path='healing' element={<Healing />} />
          <Route path='refill' element={<Refill />} />
        </Routes>
      </BrowserRouter>
    </AlertProvider>
  </ContextProvider>
);
