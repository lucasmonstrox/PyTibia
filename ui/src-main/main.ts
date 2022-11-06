import 'reflect-metadata';
import { app, BrowserWindow, ipcMain } from 'electron';
import installExtension, {
  REACT_DEVELOPER_TOOLS,
} from 'electron-devtools-installer';
import path from 'path';
import { createConnection } from 'typeorm';
import { HealthOptions } from './models/HealthOptions';
import { Player } from './models/Player';
import { io } from 'socket.io-client';

const isDev = process.env.NODE_ENV === 'development';

const createWindow = async () => {
  const socket = io('http://0.0.0.0:5000');

  ipcMain.handle('getContext', async () => {
    return new Promise((resolve, reject) => {
      socket.emit('getContext', (err, res) => {
        if (err) return reject(err);
        resolve(res);
      });
    });
  });

  ipcMain.handle('setContext', async (_, data) => {
    return new Promise((resolve, reject) => {
      socket.emit('setContext', data, (err, res) => {
        if (err) return reject(err);
        resolve(res);
      });
    });
  });

  // const pythonProcess = require('child_process').spawn('python', [
  //   '../main.py',
  // ]);

  // pythonProcess.stdout.on('data', (data) => {
  //   console.log(`stdout: ${data}`);
  // });

  // pythonProcess.stderr.on('data', (data) => {
  //   console.error(`stderr: ${data}`);
  // });

  // pythonProcess.on('close', (code) => {
  //   console.log(`child process exited with code ${code}`);
  // });

  const connection = await createConnection({
    type: 'sqlite',
    database: './database.sql',
    entities: [HealthOptions, Player],
    synchronize: true,
  });

  const mainWindow = new BrowserWindow({
    height: 600,
    width: 800,
    darkTheme: true,
    webPreferences: {
      nodeIntegration: true,
      nodeIntegrationInWorker: true,
      nodeIntegrationInSubFrames: true,
      enableRemoteModule: true,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  // ipcMain.handle('healthOptions', async () => {
  //   const result = await connection.getRepository(HealthOptions).find();
  //   return result;
  // });

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
