import { Box, CssBaseline } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { positions, Provider as AlertProvider } from 'react-alert';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import { AlertTemplate } from './components/AlertTemplate';
import { ContextProvider } from './components/Context';
import { Cavebot } from './modules/cavebot/pages/Cavebot';
import { Healing } from './modules/healing/pages/Healing';
import { Refill } from './modules/refill/pages/Refill';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export const App = () => (
  <ThemeProvider theme={darkTheme}>
    <CssBaseline />
    <ContextProvider>
      <AlertProvider
        template={AlertTemplate}
        position={positions.TOP_CENTER}
        timeout={2500}
      >
        <BrowserRouter>
          <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Link to='/cavebot'>Cavebot</Link>
            <Link to='/healing'>Healing</Link>
            <Link to='/refill'>refill</Link>
          </Box>
          <Routes>
            <Route index element={<Cavebot />} />
            <Route path='healing' element={<Healing />} />
            <Route path='refill' element={<Refill />} />
          </Routes>
        </BrowserRouter>
      </AlertProvider>
    </ContextProvider>
  </ThemeProvider>
);
