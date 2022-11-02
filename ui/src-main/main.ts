import 'reflect-metadata';
import { app, BrowserWindow, ipcMain } from 'electron';
import installExtension, {
  REACT_DEVELOPER_TOOLS,
} from 'electron-devtools-installer';
import path from 'path';
import { createConnection } from 'typeorm';
import HealthOptions from './models/HealthOptions';
import Player from './models/Player';

const isDev = process.env.NODE_ENV === 'development';

const createWindow = async () => {
  const connection = await createConnection({
    type: 'sqlite',
    database: './database.sql',
    entities: [HealthOptions, Player],
    synchronize: true,
  });

  const mainWindow = new BrowserWindow({
    height: 600,
    width: 800,
    webPreferences: {
      nodeIntegration: true,
      nodeIntegrationInWorker: true,
      nodeIntegrationInSubFrames: true,
      enableRemoteModule: true,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  ipcMain.handle('healthOptions', async () => {
    const result = await connection.getRepository(HealthOptions).find();
    return result;
  });

  if (isDev) {
    installExtension([REACT_DEVELOPER_TOOLS])
      .then(() => {
        mainWindow.loadURL('http://localhost:3000');
        mainWindow.webContents.openDevTools();
      })
      .catch((err) => console.log('An error occurred: ', err));
  } else {
    mainWindow.loadFile(path.join('build', 'index.html'));
  }
};

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
