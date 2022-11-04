import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('api', {
  getHealthOptions: async () => ipcRenderer.invoke('healthOptions'),
});
